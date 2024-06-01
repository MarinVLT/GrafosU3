from funcoes_auxiliares import *
from criar_grafo import *


def hierholzer_modificado(grafo, num_locais=5):
    # Verifica se o grafo está vazio
    if len(grafo.nodes) == 0:
        raise ValueError("Nenhum local mapeado")

    # Encontra o vértice com o maior 'score_final'
    vertice_inicial = max(grafo.nodes, key=lambda x: grafo.nodes[x]['score_final'])
    locais = []

    # Se o número de locais desejado for menor que o número total de nós no grafo,
    # continua adicionando nós ao caminho até que todos os nós sejam visitados
    if len(grafo.nodes) <= num_locais:
        locais = list(grafo.nodes)
        print('Numero de locais pedidos é igual ou maior ao numero de locais mapeados!')
    else:
        locais = []
        while True:
            vertice_atual = vertice_inicial
            aux = 5

            while True:
                for vizinho in grafo.neighbors(vertice_atual):
                    if grafo.nodes[vizinho]['score_final'] > aux and vizinho not in locais:
                        locais.append(vizinho)
                        vertice_atual = vizinho
                        print('vizinho add')
                        break
                
                aux -= 0.1


                if vertice_atual == vertice_inicial and len(locais) >= num_locais:
                    # Se voltamos para o ponto inicial e o número de locais é suficiente, saia do loop e retorne os locais
                    return locais
                
                if  len(locais) >= num_locais:
                    # Se o número de locais é suficiente, saia do loop e retorne os locais
                    return locais


                if vertice_atual == vertice_inicial:
                    # Se voltamos para o ponto inicial mas o número de locais não é suficiente, continue no tour
                    break

    # Verifica se a lista de locais mapeados está vazia
    if len(locais) <= 0:
        raise ValueError("Nenhum local listado")

    return locais


def salvar_ranking_em_txt(grafo, caminho, arquivo):
    if not grafo.nodes:
        with open(arquivo, 'w') as file:
            file.write(f"Nenhum local mapeado!")
        return ValueError("Nenhum local mapeado")
    else:
        with open(arquivo, 'w') as f:
            f.write("\nRanking:\n")
            for i, vertice in enumerate(caminho, 1):
                f.write(f"{i}: {grafo.nodes[vertice]['nome']} - {grafo.nodes[vertice]['endereco']} ({vertice}) ({grafo.nodes[vertice]['tipos']})({grafo.nodes[vertice]['score_final']})\n")
        print("Ranking salvo!")

#arq_ranking = os.getenv('ARQ_RANKING')

#locais_encontrados = mapeamento_de_estabelecimentos(coordenadas, tipos_de_estabelecimentos, locais_visitados, raio, api_key)

#locais = hierholzer_modificado(grafo)
#salvar_ranking_em_txt(grafo, locais, arq_ranking)
