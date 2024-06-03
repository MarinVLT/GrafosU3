from funcoes_auxiliares import *
from criar_grafo import *


def hierholzer_modificado(grafo, num_locais, k, lista_tipos_pedido=[]):
    # Verifica se o grafo está vazio
    if len(grafo.nodes) == 0:
        raise ValueError("Nenhum local mapeado")

    # Encontra o vértice com o maior 'score_final'
    vertice_inicial = max(grafo.nodes, key=lambda x: grafo.nodes[x]['score_final'])
    locais = []
    

    tipos_restantes = set(lista_tipos_pedido)

    # Se o número de locais desejado for menor que o número total de nós no grafo,
    # continua adicionando nós ao caminho até que todos os nós sejam visitados
    if len(grafo.nodes) <= num_locais:
        locais = list(grafo.nodes)
        print('Numero de locais pedidos é igual ou maior ao numero de locais mapeados!')
    else:
        aux = k
        locais = []
        while True:
            vertice_atual = vertice_inicial
            #contador
            countPiorCaso = 0

            while True:
                
                for vizinho in grafo.neighbors(vertice_atual):
                    countPiorCaso += 1
                    vizinho_tipos = set(grafo.nodes[vizinho].get('tipos', []))
                    if grafo.nodes[vizinho].get('score_final', 0) > aux and vizinho not in locais:
                    
                        #Se tipos_restantes estiver vazio ja foi garantido que existe pelo menos um local de cada tipo no resultado
                        if len(tipos_restantes) <= 0:
                            locais.append(vizinho)
                            vertice_atual = vizinho

                            countPiorCaso = 0
                            break
                        elif vizinho_tipos.intersection(tipos_restantes):
                            locais.append(vizinho)
                            vertice_atual = vizinho
                            # Remove tipos encontrados dos tipos restantes
                            tipos_restantes -= vizinho_tipos.intersection(tipos_restantes)

                            countPiorCaso = 0
                            break
                        elif countPiorCaso > len(list(grafo.neighbors(vertice_atual))) and vizinho_tipos.intersection(tipos_restantes) == set() and len(tipos_restantes) > 0:
                            locais.append(vizinho)
                            vertice_atual = vizinho
                        
                            countPiorCaso = 0
                            break
                        #print(vizinho_tipos.intersection(tipos_restantes) == set() and len(tipos_restantes) < 0)

                aux -= 0.1

                if vertice_atual == vertice_inicial and len(locais) >= num_locais:
                    # Se voltamos para o ponto inicial e o número de locais é suficiente, saia do loop e retorne os locais
                     return [{
                        'place_id': local,
                        'avaliacao_geral': grafo.nodes[local].get('avaliacao_geral'),
                        'coordenadas': grafo.nodes[local].get('coordenadas'),
                        'endereco': grafo.nodes[local].get('endereco'),
                        'latitude': grafo.nodes[local].get('latitude'),
                        'longitude': grafo.nodes[local].get('longitude'),
                        'nome': grafo.nodes[local].get('nome'),
                        'score_final': grafo.nodes[local].get('score_final'),
                        'tipos': grafo.nodes[local].get('tipos')
                    } for local in locais]
                
                if  len(locais) >= num_locais:
                    # Se o número de locais é suficiente, saia do loop e retorne os locais
                    return [{
                        'place_id': local,
                        'avaliacao_geral': grafo.nodes[local].get('avaliacao_geral'),
                        'coordenadas': grafo.nodes[local].get('coordenadas'),
                        'endereco': grafo.nodes[local].get('endereco'),
                        'latitude': grafo.nodes[local].get('latitude'),
                        'longitude': grafo.nodes[local].get('longitude'),
                        'nome': grafo.nodes[local].get('nome'),
                        'score_final': grafo.nodes[local].get('score_final'),
                        'tipos': grafo.nodes[local].get('tipos')
                    } for local in locais]


                if vertice_atual == vertice_inicial:
                    aux -= 0.1
                    # Se voltamos para o ponto inicial mas o número de locais não é suficiente, continue no tour
                    break

    # Verifica se a lista de locais mapeados está vazia
    if len(locais) <= 0:
        raise ValueError("Nenhum local listado")

    #return locais
    return [{
        'place_id': local,
        'avaliacao_geral': grafo.nodes[local].get('avaliacao_geral'),
        'coordenadas': grafo.nodes[local].get('coordenadas'),
        'endereco': grafo.nodes[local].get('endereco'),
        'latitude': grafo.nodes[local].get('latitude'),
        'longitude': grafo.nodes[local].get('longitude'),
        'nome': grafo.nodes[local].get('nome'),
        'score_final': grafo.nodes[local].get('score_final'),
        'tipos': grafo.nodes[local].get('tipos')
    } for local in locais]


def salvar_resultado_txt(grafo, locais, arquivo):
    if not grafo.nodes:
        with open(arquivo, 'w', encoding='utf-8') as file:
            file.write(f"Nenhum local mapeado!")
        return ValueError("Nenhum local mapeado")
    else:
        with open(arquivo, 'w', encoding='utf-8') as f:
            f.write("\nResultado:\n")
            for i, local in enumerate(locais, 1):
                f.write(f"{i}: {local['nome']} - {local['endereco']} ({local['place_id']}) ({local['tipos']})({local['score_final']})\n")
        print("Resultado salvo!")


#arq_ranking = os.getenv('ARQ_RANKING')

#locais_encontrados = mapeamento_de_estabelecimentos(coordenadas, tipos_de_estabelecimentos, locais_visitados, raio, api_key)

#locais = hierholzer_modificado(grafo)
#salvar_ranking_em_txt(grafo, locais, arq_ranking)
