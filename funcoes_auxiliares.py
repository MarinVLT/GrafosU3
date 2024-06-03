import math

# Uma medida de distância "reta" entre dois pontos em um espaço euclidiano
def distancia_euclidiana(coord1, coord2):
    return math.sqrt((coord1[0] - coord2[0]) ** 2 + (coord1[1] - coord2[1]) ** 2)

# Jaccard, interseçãos/uniao (varia de 0 a 1, quão mais proximo de 1, mais similar)
def jaccard_similaridade(conjunto1, conjunto2):
    intersecao = len(conjunto1.intersection(conjunto2))
    uniao = len(conjunto1.union(conjunto2))
    return intersecao / uniao if uniao > 0 else 0

