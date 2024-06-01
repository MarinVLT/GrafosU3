import networkx as nx
from funcoes_auxiliares import *
from mapeamento import *


def criar_grafo_euleriano(locs_mapeados):
    grafo = nx.Graph()

    # Verifica se o número de locais é impar
    num_locais = len(locs_mapeados)
    if num_locais % 2 == 0:
        print("Número de locais é par. Removendo um local com menor score_final...")
        menor_score_vertice = min(locs_mapeados.values(), key=lambda x: x['score_final'])
        del locs_mapeados[menor_score_vertice['place_id']]
        print(f"Local removido: {menor_score_vertice['nome']}")
    
    # Adiciona os locais ao grafo
    for place_id, local in locs_mapeados.items():
        grafo.add_node(place_id, nome=local['nome'], endereco=local['endereco'], tipos=local['tipos'], avaliacao_geral=local['avaliacao_geral'], score_final=local['score_final'], coordenadas=local['coordenadas'])


   # Adiciona as arestas ponderadas com base na distância entre os locais
    for u, u_data in grafo.nodes(data=True):
        for v, v_data in grafo.nodes(data=True):
            if u != v:
                # Calcula a distância entre as coordenadas dos locais
                distancia = distancia_euclidiana(u_data['coordenadas'], v_data['coordenadas'])
                # Adiciona uma aresta ponderada com base na distância
                grafo.add_edge(u, v, distancia=distancia)

    # Verifica se o grafo é euleriano
    if not nx.is_eulerian(grafo):
        raise ValueError("O grafo não é euleriano.")
    
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
            file.write(f"{nome_local_u} - {nome_local_v}: Distancia entre os locais = {data['distancia']}\n")


# Para testar
# Criar o grafo
grafo = criar_grafo_euleriano(locais_encontrados)

# Salvar o grafo em um arquivo de texto
salvar_grafo_em_txt(grafo, arq_grafo)