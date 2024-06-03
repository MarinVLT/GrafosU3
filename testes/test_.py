import unittest
from mapeamento import ler_informacoes_usuario, mapeamento_de_estabelecimentos
from criar_grafo import criar_grafo_euleriano
from hierholzer_modificado import *
import os
import time

api_key = os.getenv('API_KEY')

class TestCases(unittest.TestCase):

    def test_ct001(self):
        start_time = time.time()

        try:
            arq_usuario = 'testes/usuario/usuario1-2.txt'
            coordenadas, tipos_de_estabelecimentos, locais_visitados = ler_informacoes_usuario(arq_usuario)
            locais_encontrados = mapeamento_de_estabelecimentos(coordenadas, tipos_de_estabelecimentos, locais_visitados, 1000, api_key) # raio = 1000
            grafo = criar_grafo_euleriano(locais_encontrados)
            locais = hierholzer_modificado(grafo,5, 3.5,tipos_de_estabelecimentos) # media score = 3.5
            salvar_resultado_txt(grafo, locais, 'testes/resultados/resultado_ct001.txt')
        except:
            pass

        end_time = time.time()
        print(f"Tempo de execução para test_ct001: {end_time - start_time} segundos")

    def test_ct002(self):
        start_time = time.time()

        try:
            arq_usuario = 'testes/usuario/usuario1-2.txt'
            coordenadas, tipos_de_estabelecimentos, locais_visitados = ler_informacoes_usuario(arq_usuario)
            locais_encontrados = mapeamento_de_estabelecimentos(coordenadas, tipos_de_estabelecimentos, locais_visitados, 1000, api_key) # raio = 1000
            grafo = criar_grafo_euleriano(locais_encontrados)
            locais = hierholzer_modificado(grafo,5, 7,tipos_de_estabelecimentos) # media score = 7
            salvar_resultado_txt(grafo, locais, 'testes/resultados/resultado_ct002.txt')
        except:
            pass

        end_time = time.time()
        print(f"Tempo de execução para test_ct002: {end_time - start_time} segundos\n"+ "-" * 100)

if __name__ == '__main__':
    unittest.main()
