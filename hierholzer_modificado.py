from funcoes_auxiliares import *
from criar_grafo import *

def hierholzer_modificado(grafo, num_locais=5):

    if len (grafo.nodes) < num_locais:
        tam = le(grafo.nodes)
        print("Número de vértices no grafo é menor que o número de locais desejado.")
    else:
        tam = num_locais

    # Encontrar o vértice com o maior 'score_final'
    vertice_inicial = max(grafo.nodes, key=lambda x: grafo.nodes[x]['score_final'])
    caminho = [vertice_inicial]
    
    while len(caminho) < tam:
        ultimo_vertice = caminho[-1]
        # Encontrar o vértice adjacente mais próximo
        vizinhos = sorted(grafo[ultimo_vertice].items(), key=lambda x: (x[1]['distancia'], -grafo.nodes[x[0]]['score_final'] if grafo.nodes[x[0]]['score_final'] > 5 else float('inf')))
        #vizinhos = sorted(grafo[ultimo_vertice].items(), key=lambda x: x[1]['distancia'])
        #vizinhos = sorted(grafo[ultimo_vertice].items(), key=lambda x: grafo.nodes[x[0]]['score_final'], reverse=True)
        for vizinho, data in vizinhos:
            if vizinho not in caminho:
                caminho.append(vizinho)
                break
    return caminho

def salvar_ranking_em_txt(grafo, caminho, filename):
    with open(filename, 'w') as f:
        f.write("\nRanking:\n")
        for i, vertice in enumerate(caminho, 1):
            f.write(f"{i}: {grafo.nodes[vertice]['nome']} - {grafo.nodes[vertice]['endereco']} ({vertice}) ({grafo.nodes[vertice]['tipos']})({grafo.nodes[vertice]['score_final']})\n")
    print("Ranking salvo!")

arq_ranking = os.getenv('ARQ_RANKING')

caminho = hierholzer_modificado(grafo)
salvar_ranking_em_txt(grafo, caminho, arq_ranking)
