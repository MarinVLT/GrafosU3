import unittest
from mapeamento import ler_informacoes_usuario, mapeamento_de_estabelecimentos
from criar_grafo import criar_grafo_euleriano
from hierholzer_modificado import *
import os
import time

api_key = os.getenv('API_KEY')
path_usuario = 'testes/usuario/'
path_resultados = 'testes/resultados/'

#Configurando o nome dos arquivos de usuário
US1_RN_4 = 'US1_RN_4.txt'
US2_RN_10 = 'US2_RN_10.txt'
US3_RN_30 = 'US3_RN_30.txt'

US1_SP_4 = 'US1_SP_4.txt'
US2_SP_10 = 'US2_SP_10.txt'
US3_SP_30 = 'US3_SP_30.txt'

class TestCases(unittest.TestCase):

    def perfil_teste(self, arquivo_usuario, raio, media_score, arquivo_resultado):
        arq_usuario = arquivo_usuario
        coordenadas, tipos_de_estabelecimentos, locais_visitados = ler_informacoes_usuario(arq_usuario)
        locais_encontrados = mapeamento_de_estabelecimentos(coordenadas, tipos_de_estabelecimentos, locais_visitados,raio, api_key)  # raio = 1000
        grafo = criar_grafo_euleriano(locais_encontrados)
        locais = hierholzer_modificado(grafo, 5, media_score, tipos_de_estabelecimentos)  # media score = 3.5
        salvar_resultado_txt(grafo, locais, arquivo_resultado)

    def test_ct001_rn(self):
        arq_usuario = path_usuario + US1_RN_4
        arq_resultado = path_resultados + 'resultado_' + __name__ + '.txt'
        raio = 1000
        media_score = 3.5

        start_time = time.time()

        try:
             self.perfil_teste(arq_usuario, raio, media_score, arq_resultado)
        except:
            pass

        end_time = time.time()
        tempo_execucao = end_time - start_time

        with open(arq_resultado, 'a') as file:
            string = '\n' + __name__ + ':\n' + tempo_execucao + '\n'
            file.write(string)

        print(f"Tempo de execução para {__name__}: {tempo_execucao} segundos")

    def test_ct002_rn(self):
        arq_usuario = path_usuario + US1_RN_4
        arq_resultado = path_resultados + 'resultado_{}.txt'.format(__name__)
        raio = 1000
        media_score = 7

        start_time = time.time()

        try:
            self.perfil_teste(arq_usuario, raio, media_score, arq_resultado)
        except:
            pass

        end_time = time.time()
        tempo_execucao = end_time - start_time

        with open(arq_resultado, 'a') as file:
            string = '\n' + __name__ + ':\n' + tempo_execucao + '\n'
            file.write(string)

        print(f"Tempo de execução para {__name__}: {tempo_execucao} segundos")

    def test_ct003_rn(self):
        arq_usuario = path_usuario + US2_RN_10
        arq_resultado = path_resultados + 'resultado_{}.txt'.format(__name__)
        raio = 1000
        media_score = 3.5

        start_time = time.time()

        try:
            self.perfil_teste(arq_usuario, raio, media_score, arq_resultado)
        except:
            pass

        with open(arq_resultado, 'a') as file:
            file.write('\n{__name__}:\n {end_time - start_time}\n')

        end_time = time.time()
        print(f"Tempo de execução para {__name__}: {end_time - start_time} segundos\n" + "-" * 100)

    def test_ct004_rn(self):
        arq_usuario = path_usuario + US2_RN_10
        arq_resultado = path_resultados + 'resultado_{}.txt'.format(__name__)
        raio = 1000
        media_score = 7

        start_time = time.time()

        try:
            self.perfil_teste(arq_usuario, raio, media_score, arq_resultado)
        except:
            pass

        with open(arq_resultado, 'a') as file:
            file.write('\n{__name__}:\n {end_time - start_time}\n')

        end_time = time.time()
        print(f"Tempo de execução para {__name__}: {end_time - start_time} segundos\n" + "-" * 100)

    def test_ct005_rn(self):
        arq_usuario = path_usuario + US3_RN_30
        arq_resultado = path_resultados + 'resultado_{}.txt'.format(__name__)
        raio = 1000
        media_score = 3.5

        start_time = time.time()

        try:
            self.perfil_teste(arq_usuario, raio, media_score, arq_resultado)
        except:
            pass

        with open(arq_resultado, 'a') as file:
            file.write('\n{__name__}:\n {end_time - start_time}\n')

        end_time = time.time()
        print(f"Tempo de execução para {__name__}: {end_time - start_time} segundos\n" + "-" * 100)

    def test_ct006_rn(self):
        arq_usuario = path_usuario + US3_RN_30
        arq_resultado = path_resultados + 'resultado_{}.txt'.format(__name__)
        raio = 1000
        media_score = 7
        start_time = time.time()

        try:
            self.perfil_teste(arq_usuario, raio, media_score, arq_resultado)
        except:
            pass

        with open(arq_resultado, 'a') as file:
            file.write('\n{__name__}:\n {end_time - start_time}\n')

        end_time = time.time()
        print(f"Tempo de execução para {__name__}: {end_time - start_time} segundos\n" + "-" * 100)

    def test_ct007_rn(self):
        arq_usuario = path_usuario + US1_RN_4
        arq_resultado = path_resultados + 'resultado_' + __name__ + '.txt'
        raio = 5000
        media_score = 3.5

        start_time = time.time()

        try:
             self.perfil_teste(arq_usuario, raio, media_score, arq_resultado)
        except:
            pass

        end_time = time.time()
        tempo_execucao = end_time - start_time

        with open(arq_resultado, 'a') as file:
            string = '\n' + __name__ + ':\n' + tempo_execucao + '\n'
            file.write(string)

        print(f"Tempo de execução para {__name__}: {tempo_execucao} segundos")

    def test_ct008_rn(self):
        arq_usuario = path_usuario + US1_RN_4
        arq_resultado = path_resultados + 'resultado_{}.txt'.format(__name__)
        raio = 5000
        media_score = 7

        start_time = time.time()

        try:
            self.perfil_teste(arq_usuario, raio, media_score, arq_resultado)
        except:
            pass

        end_time = time.time()
        tempo_execucao = end_time - start_time

        with open(arq_resultado, 'a') as file:
            string = '\n' + __name__ + ':\n' + tempo_execucao + '\n'
            file.write(string)

        print(f"Tempo de execução para {__name__}: {tempo_execucao} segundos")

    def test_ct009_rn(self):
        arq_usuario = path_usuario + US2_RN_10
        arq_resultado = path_resultados + 'resultado_{}.txt'.format(__name__)
        raio = 5000
        media_score = 3.5

        start_time = time.time()

        try:
            self.perfil_teste(arq_usuario, raio, media_score, arq_resultado)
        except:
            pass

        with open(arq_resultado, 'a') as file:
            file.write('\n{__name__}:\n {end_time - start_time}\n')

        end_time = time.time()
        print(f"Tempo de execução para {__name__}: {end_time - start_time} segundos\n" + "-" * 100)

    def test_ct010_rn(self):
        arq_usuario = path_usuario + US2_RN_10
        arq_resultado = path_resultados + 'resultado_{}.txt'.format(__name__)
        raio = 5000
        media_score = 7

        start_time = time.time()

        try:
            self.perfil_teste(arq_usuario, raio, media_score, arq_resultado)
        except:
            pass

        with open(arq_resultado, 'a') as file:
            file.write('\n{__name__}:\n {end_time - start_time}\n')

        end_time = time.time()
        print(f"Tempo de execução para {__name__}: {end_time - start_time} segundos\n" + "-" * 100)

    def test_ct011_rn(self):
        arq_usuario = path_usuario + US3_RN_30
        arq_resultado = path_resultados + 'resultado_{}.txt'.format(__name__)
        raio = 5000
        media_score = 3.5

        start_time = time.time()

        try:
            self.perfil_teste(arq_usuario, raio, media_score, arq_resultado)
        except:
            pass

        with open(arq_resultado, 'a') as file:
            file.write('\n{__name__}:\n {end_time - start_time}\n')

        end_time = time.time()
        print(f"Tempo de execução para {__name__}: {end_time - start_time} segundos\n" + "-" * 100)

    def test_ct012_rn(self):
        arq_usuario = path_usuario + US3_RN_30
        arq_resultado = path_resultados + 'resultado_{}.txt'.format(__name__)
        raio = 5000
        media_score = 7
        start_time = time.time()

        try:
            self.perfil_teste(arq_usuario, raio, media_score, arq_resultado)
        except:
            pass

        with open(arq_resultado, 'a') as file:
            file.write('\n{__name__}:\n {end_time - start_time}\n')

        end_time = time.time()
        print(f"Tempo de execução para {__name__}: {end_time - start_time} segundos\n" + "-" * 100)

    def test_ct013_rn(self):
        arq_usuario = path_usuario + US1_RN_4
        arq_resultado = path_resultados + 'resultado_' + __name__ + '.txt'
        raio = 5000
        media_score = 3.5

        start_time = time.time()

        try:
             self.perfil_teste(arq_usuario, raio, media_score, arq_resultado)
        except:
            pass

        end_time = time.time()
        tempo_execucao = end_time - start_time

        with open(arq_resultado, 'a') as file:
            string = '\n' + __name__ + ':\n' + tempo_execucao + '\n'
            file.write(string)

        print(f"Tempo de execução para {__name__}: {tempo_execucao} segundos")

    def test_ct008_rn(self):
        arq_usuario = path_usuario + US1_RN_4
        arq_resultado = path_resultados + 'resultado_{}.txt'.format(__name__)
        raio = 5000
        media_score = 7

        start_time = time.time()

        try:
            self.perfil_teste(arq_usuario, raio, media_score, arq_resultado)
        except:
            pass

        end_time = time.time()
        tempo_execucao = end_time - start_time

        with open(arq_resultado, 'a') as file:
            string = '\n' + __name__ + ':\n' + tempo_execucao + '\n'
            file.write(string)

        print(f"Tempo de execução para {__name__}: {tempo_execucao} segundos")

    def test_ct009_rn(self):
        arq_usuario = path_usuario + US2_RN_10
        arq_resultado = path_resultados + 'resultado_{}.txt'.format(__name__)
        raio = 5000
        media_score = 3.5

        start_time = time.time()

        try:
            self.perfil_teste(arq_usuario, raio, media_score, arq_resultado)
        except:
            pass

        with open(arq_resultado, 'a') as file:
            file.write('\n{__name__}:\n {end_time - start_time}\n')

        end_time = time.time()
        print(f"Tempo de execução para {__name__}: {end_time - start_time} segundos\n" + "-" * 100)

    def test_ct010_rn(self):
        arq_usuario = path_usuario + US2_RN_10
        arq_resultado = path_resultados + 'resultado_{}.txt'.format(__name__)
        raio = 5000
        media_score = 7

        start_time = time.time()

        try:
            self.perfil_teste(arq_usuario, raio, media_score, arq_resultado)
        except:
            pass

        with open(arq_resultado, 'a') as file:
            file.write('\n{__name__}:\n {end_time - start_time}\n')

        end_time = time.time()
        print(f"Tempo de execução para {__name__}: {end_time - start_time} segundos\n" + "-" * 100)

    def test_ct011_rn(self):
        arq_usuario = path_usuario + US3_RN_30
        arq_resultado = path_resultados + 'resultado_{}.txt'.format(__name__)
        raio = 5000
        media_score = 3.5

        start_time = time.time()

        try:
            self.perfil_teste(arq_usuario, raio, media_score, arq_resultado)
        except:
            pass

        with open(arq_resultado, 'a') as file:
            file.write('\n{__name__}:\n {end_time - start_time}\n')

        end_time = time.time()
        print(f"Tempo de execução para {__name__}: {end_time - start_time} segundos\n" + "-" * 100)

    def test_ct012_rn(self):
        arq_usuario = path_usuario + US3_RN_30
        arq_resultado = path_resultados + 'resultado_{}.txt'.format(__name__)
        raio = 5000
        media_score = 7
        start_time = time.time()

        try:
            self.perfil_teste(arq_usuario, raio, media_score, arq_resultado)
        except:
            pass

        with open(arq_resultado, 'a') as file:
            file.write('\n{__name__}:\n {end_time - start_time}\n')

        end_time = time.time()
        print(f"Tempo de execução para {__name__}: {end_time - start_time} segundos\n" + "-" * 100)


if __name__ == '__main__':
    unittest.main()
