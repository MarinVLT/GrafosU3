import googlemaps
import os
from dotenv import load_dotenv
import networkx as nx


# Jaccard, interseçãos/uniao (varia de 0 a 1, quão mais proximo de 1, mais similar)
def jaccard_similarity(conjunto1, conjunto2):
    intersecao = len(conjunto1.intersection(conjunto2))
    uniao = len(conjunto1.union(conjunto2))
    return intersecao / uniao if uniao > 0 else 0

def ler_informacoes_usuario(arquivo):
    with open(arquivo, 'r', encoding='latin-1') as file:
        # Lê as coordenadas da primeira linha e as converte para float
        coordenadas = tuple(map(float, file.readline().strip().split(',')))

        # Lê os tipos de estabelecimentos da segunda linha e os separa por vírgula
        tipos_de_estabelecimentos = file.readline().strip().split(',')

        # Inicializa uma lista para armazenar os locais visitados
        locais_visitados = []

        # Lê cada linha restante do arquivo
        for line in file:
            # Divide a linha em partes separadas por vírgula
            partes = line.strip().split(',')

            # Extrai o nome do local, os tipos de estabelecimentos e a avaliação
            nome = partes[0]
            tipos = partes[1:-1]  # Tipos de estabelecimentos são todos os itens, exceto o primeiro e o último
            avaliacao = float(partes[-1]) if partes[-1] else 'N/A'

            # Adiciona as informações do local visitado à lista de locais visitados
            locais_visitados.append({
                'nome': nome,
                'tipos': tipos,
                'avaliacao': avaliacao
            })

    # Retorna as coordenadas, os tipos de estabelecimentos e os locais visitados
    return coordenadas, tipos_de_estabelecimentos, locais_visitados



def mapeamento_de_estabelecimentos(coordenadas, tipos_de_estabelecimentos, locais_visitados, radius, api_key):
    # Inicializa o cliente da API do Google Maps com a chave fornecida
    gmaps = googlemaps.Client(key=api_key)
    # Dicionário para armazenar todos os estabelecimentos encontrados
    todos_estabelecimentos = {}

    # Itera sobre cada tipo de estabelecimento desejado
    for tipo in tipos_de_estabelecimentos:
         # Busca lugares próximos com base no tipo de estabelecimento (radius é em metros)
        resultados = gmaps.places_nearby(location=coordenadas, radius=radius, type=tipo)
        
        # Se há resultados na busca
        if resultados['results']:
             # Itera sobre cada resultado
            for resultado in resultados['results']:
                 # Obtém o ID do lugar
                place_id = resultado['place_id']
                # Busca detalhes adicionais do lugar usando o place_id
                detalhes = gmaps.place(place_id=place_id)
                 # Inicializa o score do lugar (logica do score, se o lugar tiver o tipo desejado -> score + 1)
                # score = 0
                

                # Se há detalhes do resultado
                if detalhes.get('result'):
                    lugar = detalhes['result']
                     # Obtém os tipos do local
                    tipos_do_local = lugar.get('types')
                    
                    # Similaridade entre o tipo do local atual e os tipos pedidos ao usuario

                    sim_entreTipos = jaccard_similarity(set(tipos_de_estabelecimentos), set(tipos_do_local))
                    
                    # Media de similaridade entre tipos do local atual e tipos dos locais ja visitados
                    similaridades = [jaccard_similarity(set(tipo_local['tipos']), set(tipos_do_local)) for tipo_local in locais_visitados]
                    sim_HistoricoVisitados = sum(similaridades) / len(similaridades) if similaridades else 0
                    
                    # Armazena os detalhes do estabelecimento no dicionário
                    todos_estabelecimentos[place_id] = {
                        'nome': lugar.get('name'),
                        'endereco': lugar.get('formatted_address'),
                        'tipos': tipos_do_local,
                        'avaliacao_geral': lugar.get('rating'),
                        #'score': score,
                        #'sim_locais_locais': max([jaccard_similarity(set(tipo_local['tipos']), tipos_do_local) for tipo_local in locais_visitados]),
                        'score_final': sim_entreTipos + sim_HistoricoVisitados
                    }
    
    # Retorna o dicionário com todos os estabelecimentos encontrados e seus scores
    return todos_estabelecimentos

# Salvar locais mapeados em locais_mapeados.txt
def salvar_locais_mapeados(arquivo, locais_mapeados):
    with open(arquivo, 'w') as file:
        for local_id, local in locais_mapeados.items():
            file.write(f"{local['nome']}\n{local['endereco']}\n{','.join(local['tipos'])}\n{local['avaliacao_geral'] 
            if local['avaliacao_geral'] is not None else 'N/A'}\n{local['score_final']}\n\n")
            print("Locais mapeados foram salvos no arquivo 'locais_mapeados.txt'.")


def criar_grafo(locs_mapeados):
    grafo = nx.Graph()
    for place_id, local in locs_mapeados.items():
        grafo.add_node(place_id, nome=local['nome'], endereco=local['endereco'], tipos=local['tipos'], avaliacao_geral=local['avaliacao_geral'], score_final=local['score_final'])
    
    # Adiciona arestas com base na similaridade entre os locais
    for u, u_data in grafo.nodes(data=True):
        for v, v_data in grafo.nodes(data=True):
            if u != v:
                # Calcula a similaridade entre os tipos dos locais
                sim_tipo = jaccard_similarity(set(u_data['tipos']), set(v_data['tipos']))
                # Adiciona uma aresta ponderada com base na similaridade
                grafo.add_edge(u, v, similaridade=sim_tipo)
    
    # Garante que o grafo seja conectado
    if not nx.is_connected(grafo):
        # Encontra as componentes conectadas
        componentes_conectadas = list(nx.connected_components(grafo))
        # Conecta as componentes conectadas adicionando uma aresta entre dois vértices de componentes diferentes
        for i in range(len(componentes_conectadas) - 1):
            u = min(componentes_conectadas[i], key=lambda x: grafo.degree[x])
            v = min(componentes_conectadas[i + 1], key=lambda x: grafo.degree[x])
            grafo.add_edge(u, v)

    # Verifica e adiciona arestas para garantir que cada vértice tenha grau par
    for node, degree in grafo.degree:
        if degree % 2 != 0:
            # Encontra um vértice com grau ímpar para conectar
            for other_node, other_degree in grafo.degree:
                if other_degree % 2 != 0 and node != other_node and not grafo.has_edge(node, other_node):
                    grafo.add_edge(node, other_node)
                    break

    return grafo


# Função para salvar o grafo em um arquivo de texto
def salvar_grafo_em_txt(grafo, arquivo):
    with open(arquivo, 'w') as file:
        # Escrever informações sobre os vértices
        file.write("Vértices:\n")
        for node, data in grafo.nodes(data=True):
            nome_local = data['nome']
            file.write(f"{nome_local}: {data}\n")
        
        # Escrever informações sobre as arestas
        file.write("\nArestas:\n")
        for u, v, data in grafo.edges(data=True):
            nome_local_u = grafo.nodes[u]['nome']
            nome_local_v = grafo.nodes[v]['nome']
            file.write(f"{nome_local_u} - {nome_local_v}: Similaridade entre tipos = {data['similaridade']}\n")


# Atribuir as configurações do .env a uma variável
load_dotenv()
api_key = os.getenv('API_KEY')

# Ler as informações do usuário do arquivo de texto
coordenadas, tipos_de_estabelecimentos, locais_visitados = ler_informacoes_usuario('usuario.txt')

# Exemplo de uso da função
radius = 1000

locais_encontrados = mapeamento_de_estabelecimentos(coordenadas, tipos_de_estabelecimentos, locais_visitados, radius, api_key)

# Salvar os locais mapeados em um arquivo de texto
salvar_locais_mapeados('locais_mapeados.txt', locais_encontrados)

print("Locais mapeados foram salvos no arquivo 'locais_mapeados.txt'.")

# Criar o grafo
grafo = criar_grafo(locais_encontrados)

# Salvar o grafo em um arquivo de texto
salvar_grafo_em_txt(grafo, "grafo.txt")
