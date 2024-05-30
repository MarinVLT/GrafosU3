import googlemaps
import os
from dotenv import load_dotenv


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

# similaridade esta sendo calculado com base nos tipos 