import inspect
import unittest
from mapeamento import ler_informacoes_usuario, mapeamento_de_estabelecimentos
from criar_grafo import criar_grafo_euleriano
from hierholzer_modificado import *
import os
import time

api_key = os.getenv('API_KEY')
path_usuario = 'testes/usuario/'
path_resultados = 'testes/resultados/'

# Configurando o nome dos arquivos de usuário
US1_SP_4 = 'US1_SP_4.txt'
US2_SP_10 = 'US2_SP_10.txt'
US3_SP_30 = 'US3_SP_30.txt'


class TestCases(unittest.TestCase):

    def perfil_teste(self, arquivo_usuario, raio, media_score, arquivo_resultado, qtd_locais):
        start_time = time.time()
        coordenadas, tipos_de_estabelecimentos, locais_visitados = ler_informacoes_usuario(arquivo_usuario)
        locais_encontrados = mapeamento_de_estabelecimentos(coordenadas, tipos_de_estabelecimentos, locais_visitados,
                                                            raio)
        grafo = criar_grafo_euleriano(locais_encontrados)
        locais = hierholzer_modificado(grafo, qtd_locais, media_score, tipos_de_estabelecimentos)
        salvar_resultado_txt(grafo, locais, arquivo_resultado)
        end_time = time.time()

        return str(end_time - start_time)

    def output(self, arq_resultado, teste_atual, tempo_execucao):
        with open(arq_resultado, 'a', encoding='utf-8') as file:
            string = '\n' + teste_atual + ':\n' + tempo_execucao + '\n'
            file.write(string)
        print(f"Tempo de execução para {teste_atual}: {tempo_execucao} segundos")

    def test_ct001_sp(self):
        raio = 1000
        arq_usuario = path_usuario + US1_SP_4
        media_score = 3.5
        qtd_locais = 5

        teste_atual = inspect.currentframe().f_code.co_name
        arq_resultado = path_resultados + 'resultado_' + teste_atual + '.txt'

        try:
            tempo_execucao = self.perfil_teste(arq_usuario, raio, media_score, arq_resultado, qtd_locais)
            self.output(arq_resultado, teste_atual, tempo_execucao)
        except Exception as e:
            self.fail(teste_atual + ' falhou na execução: ' + str(e))

    def test_ct002_sp(self):
        raio = 1000
        arq_usuario = path_usuario + US1_SP_4
        media_score = 3.5
        qtd_locais = 10

        teste_atual = inspect.currentframe().f_code.co_name
        arq_resultado = path_resultados + 'resultado_' + teste_atual + '.txt'

        try:
            tempo_execucao = self.perfil_teste(arq_usuario, raio, media_score, arq_resultado, qtd_locais)
            self.output(arq_resultado, teste_atual, tempo_execucao)
        except Exception as e:
            self.fail(teste_atual + ' falhou na execução: ' + str(e))

    def test_ct003_sp(self):
        raio = 1000
        arq_usuario = path_usuario + US1_SP_4
        media_score = 7
        qtd_locais = 5

        teste_atual = inspect.currentframe().f_code.co_name
        arq_resultado = path_resultados + 'resultado_' + teste_atual + '.txt'

        try:
            tempo_execucao = self.perfil_teste(arq_usuario, raio, media_score, arq_resultado, qtd_locais)
            self.output(arq_resultado, teste_atual, tempo_execucao)
        except Exception as e:
            self.fail(teste_atual + ' falhou na execução: ' + str(e))

    def test_ct004_sp(self):
        raio = 1000
        arq_usuario = path_usuario + US1_SP_4
        media_score = 7
        qtd_locais = 10

        teste_atual = inspect.currentframe().f_code.co_name
        arq_resultado = path_resultados + 'resultado_' + teste_atual + '.txt'

        try:
            tempo_execucao = self.perfil_teste(arq_usuario, raio, media_score, arq_resultado, qtd_locais)
            self.output(arq_resultado, teste_atual, tempo_execucao)
        except Exception as e:
            self.fail(teste_atual + ' falhou na execução: ' + str(e))

    def test_ct005_sp(self):
        raio = 1000
        arq_usuario = path_usuario + US2_SP_10
        media_score = 3.5
        qtd_locais = 5

        teste_atual = inspect.currentframe().f_code.co_name
        arq_resultado = path_resultados + 'resultado_' + teste_atual + '.txt'

        try:
            tempo_execucao = self.perfil_teste(arq_usuario, raio, media_score, arq_resultado, qtd_locais)
            self.output(arq_resultado, teste_atual, tempo_execucao)
        except Exception as e:
            self.fail(teste_atual + ' falhou na execução: ' + str(e))

    def test_ct006_sp(self):
        raio = 1000
        arq_usuario = path_usuario + US2_SP_10
        media_score = 3.5
        qtd_locais = 10

        teste_atual = inspect.currentframe().f_code.co_name
        arq_resultado = path_resultados + 'resultado_' + teste_atual + '.txt'

        try:
            tempo_execucao = self.perfil_teste(arq_usuario, raio, media_score, arq_resultado, qtd_locais)
            self.output(arq_resultado, teste_atual, tempo_execucao)
        except Exception as e:
            self.fail(teste_atual + ' falhou na execução: ' + str(e))

    def test_ct007_sp(self):
        raio = 1000
        arq_usuario = path_usuario + US2_SP_10
        media_score = 7
        qtd_locais = 5

        teste_atual = inspect.currentframe().f_code.co_name
        arq_resultado = path_resultados + 'resultado_' + teste_atual + '.txt'

        try:
            tempo_execucao = self.perfil_teste(arq_usuario, raio, media_score, arq_resultado, qtd_locais)
            self.output(arq_resultado, teste_atual, tempo_execucao)
        except Exception as e:
            self.fail(teste_atual + ' falhou na execução: ' + str(e))

    def test_ct008_sp(self):
        raio = 1000
        arq_usuario = path_usuario + US2_SP_10
        media_score = 7
        qtd_locais = 10

        teste_atual = inspect.currentframe().f_code.co_name
        arq_resultado = path_resultados + 'resultado_' + teste_atual + '.txt'

        try:
            tempo_execucao = self.perfil_teste(arq_usuario, raio, media_score, arq_resultado, qtd_locais)
            self.output(arq_resultado, teste_atual, tempo_execucao)
        except Exception as e:
            self.fail(teste_atual + ' falhou na execução: ' + str(e))

    def test_ct009_sp(self):
        raio = 1000
        arq_usuario = path_usuario + US3_SP_30
        media_score = 3.5
        qtd_locais = 5

        teste_atual = inspect.currentframe().f_code.co_name
        arq_resultado = path_resultados + 'resultado_' + teste_atual + '.txt'

        try:
            tempo_execucao = self.perfil_teste(arq_usuario, raio, media_score, arq_resultado, qtd_locais)
            self.output(arq_resultado, teste_atual, tempo_execucao)
        except Exception as e:
            self.fail(teste_atual + ' falhou na execução: ' + str(e))

    def test_ct010_sp(self):
        raio = 1000
        arq_usuario = path_usuario + US3_SP_30
        media_score = 3.5
        qtd_locais = 10

        teste_atual = inspect.currentframe().f_code.co_name
        arq_resultado = path_resultados + 'resultado_' + teste_atual + '.txt'

        try:
            tempo_execucao = self.perfil_teste(arq_usuario, raio, media_score, arq_resultado, qtd_locais)
            self.output(arq_resultado, teste_atual, tempo_execucao)
        except Exception as e:
            self.fail(teste_atual + ' falhou na execução: ' + str(e))

    def test_ct011_sp(self):
        raio = 1000
        arq_usuario = path_usuario + US3_SP_30
        media_score = 7
        qtd_locais = 5

        teste_atual = inspect.currentframe().f_code.co_name
        arq_resultado = path_resultados + 'resultado_' + teste_atual + '.txt'

        try:
            tempo_execucao = self.perfil_teste(arq_usuario, raio, media_score, arq_resultado, qtd_locais)
            self.output(arq_resultado, teste_atual, tempo_execucao)
        except Exception as e:
            self.fail(teste_atual + ' falhou na execução: ' + str(e))

    def test_ct012_sp(self):
        raio = 1000
        arq_usuario = path_usuario + US3_SP_30
        media_score = 7
        qtd_locais = 10

        teste_atual = inspect.currentframe().f_code.co_name
        arq_resultado = path_resultados + 'resultado_' + teste_atual + '.txt'

        try:
            tempo_execucao = self.perfil_teste(arq_usuario, raio, media_score, arq_resultado, qtd_locais)
            self.output(arq_resultado, teste_atual, tempo_execucao)
        except Exception as e:
            self.fail(teste_atual + ' falhou na execução: ' + str(e))

    def test_ct013_sp(self):
        raio = 5000
        arq_usuario = path_usuario + US1_SP_4
        media_score = 3.5
        qtd_locais = 5

        teste_atual = inspect.currentframe().f_code.co_name
        arq_resultado = path_resultados + 'resultado_' + teste_atual + '.txt'

        try:
            tempo_execucao = self.perfil_teste(arq_usuario, raio, media_score, arq_resultado, qtd_locais)
            self.output(arq_resultado, teste_atual, tempo_execucao)
        except Exception as e:
            self.fail(teste_atual + ' falhou na execução: ' + str(e))

    def test_ct014_sp(self):
        raio = 5000
        arq_usuario = path_usuario + US1_SP_4
        media_score = 3.5
        qtd_locais = 10

        teste_atual = inspect.currentframe().f_code.co_name
        arq_resultado = path_resultados + 'resultado_' + teste_atual + '.txt'

        try:
            tempo_execucao = self.perfil_teste(arq_usuario, raio, media_score, arq_resultado, qtd_locais)
            self.output(arq_resultado, teste_atual, tempo_execucao)
        except Exception as e:
            self.fail(teste_atual + ' falhou na execução: ' + str(e))

    def test_ct015_sp(self):
        raio = 5000
        arq_usuario = path_usuario + US1_SP_4
        media_score = 7
        qtd_locais = 5

        teste_atual = inspect.currentframe().f_code.co_name
        arq_resultado = path_resultados + 'resultado_' + teste_atual + '.txt'

        try:
            tempo_execucao = self.perfil_teste(arq_usuario, raio, media_score, arq_resultado, qtd_locais)
            self.output(arq_resultado, teste_atual, tempo_execucao)
        except Exception as e:
            self.fail(teste_atual + ' falhou na execução: ' + str(e))

    def test_ct016_sp(self):
        raio = 5000
        arq_usuario = path_usuario + US1_SP_4
        media_score = 7
        qtd_locais = 10

        teste_atual = inspect.currentframe().f_code.co_name
        arq_resultado = path_resultados + 'resultado_' + teste_atual + '.txt'

        try:
            tempo_execucao = self.perfil_teste(arq_usuario, raio, media_score, arq_resultado, qtd_locais)
            self.output(arq_resultado, teste_atual, tempo_execucao)
        except Exception as e:
            self.fail(teste_atual + ' falhou na execução: ' + str(e))

    def test_ct017_sp(self):
        raio = 5000
        arq_usuario = path_usuario + US2_SP_10
        media_score = 3.5
        qtd_locais = 5

        teste_atual = inspect.currentframe().f_code.co_name
        arq_resultado = path_resultados + 'resultado_' + teste_atual + '.txt'

        try:
            tempo_execucao = self.perfil_teste(arq_usuario, raio, media_score, arq_resultado, qtd_locais)
            self.output(arq_resultado, teste_atual, tempo_execucao)
        except Exception as e:
            self.fail(teste_atual + ' falhou na execução: ' + str(e))

    def test_ct018_sp(self):
        raio = 5000
        arq_usuario = path_usuario + US2_SP_10
        media_score = 3.5
        qtd_locais = 10

        teste_atual = inspect.currentframe().f_code.co_name
        arq_resultado = path_resultados + 'resultado_' + teste_atual + '.txt'

        try:
            tempo_execucao = self.perfil_teste(arq_usuario, raio, media_score, arq_resultado, qtd_locais)
            self.output(arq_resultado, teste_atual, tempo_execucao)
        except Exception as e:
            self.fail(teste_atual + ' falhou na execução: ' + str(e))

    def test_ct019_sp(self):
        raio = 5000
        arq_usuario = path_usuario + US2_SP_10
        media_score = 7
        qtd_locais = 5

        teste_atual = inspect.currentframe().f_code.co_name
        arq_resultado = path_resultados + 'resultado_' + teste_atual + '.txt'

        try:
            tempo_execucao = self.perfil_teste(arq_usuario, raio, media_score, arq_resultado, qtd_locais)
            self.output(arq_resultado, teste_atual, tempo_execucao)
        except Exception as e:
            self.fail(teste_atual + ' falhou na execução: ' + str(e))

    def test_ct020_sp(self):
        raio = 5000
        arq_usuario = path_usuario + US2_SP_10
        media_score = 7
        qtd_locais = 10

        teste_atual = inspect.currentframe().f_code.co_name
        arq_resultado = path_resultados + 'resultado_' + teste_atual + '.txt'

        try:
            tempo_execucao = self.perfil_teste(arq_usuario, raio, media_score, arq_resultado, qtd_locais)
            self.output(arq_resultado, teste_atual, tempo_execucao)
        except Exception as e:
            self.fail(teste_atual + ' falhou na execução: ' + str(e))

    def test_ct021_sp(self):
        raio = 5000
        arq_usuario = path_usuario + US3_SP_30
        media_score = 3.5
        qtd_locais = 5

        teste_atual = inspect.currentframe().f_code.co_name
        arq_resultado = path_resultados + 'resultado_' + teste_atual + '.txt'

        try:
            tempo_execucao = self.perfil_teste(arq_usuario, raio, media_score, arq_resultado, qtd_locais)
            self.output(arq_resultado, teste_atual, tempo_execucao)
        except Exception as e:
            self.fail(teste_atual + ' falhou na execução: ' + str(e))

    def test_ct022_sp(self):
        raio = 5000
        arq_usuario = path_usuario + US3_SP_30
        media_score = 3.5
        qtd_locais = 10

        teste_atual = inspect.currentframe().f_code.co_name
        arq_resultado = path_resultados + 'resultado_' + teste_atual + '.txt'

        try:
            tempo_execucao = self.perfil_teste(arq_usuario, raio, media_score, arq_resultado, qtd_locais)
            self.output(arq_resultado, teste_atual, tempo_execucao)
        except Exception as e:
            self.fail(teste_atual + ' falhou na execução: ' + str(e))

    def test_ct023_sp(self):
        raio = 5000
        arq_usuario = path_usuario + US3_SP_30
        media_score = 7
        qtd_locais = 5

        teste_atual = inspect.currentframe().f_code.co_name
        arq_resultado = path_resultados + 'resultado_' + teste_atual + '.txt'

        try:
            tempo_execucao = self.perfil_teste(arq_usuario, raio, media_score, arq_resultado, qtd_locais)
            self.output(arq_resultado, teste_atual, tempo_execucao)
        except Exception as e:
            self.fail(teste_atual + ' falhou na execução: ' + str(e))

    def test_ct024_sp(self):
        raio = 5000
        arq_usuario = path_usuario + US3_SP_30
        media_score = 7
        qtd_locais = 10

        teste_atual = inspect.currentframe().f_code.co_name
        arq_resultado = path_resultados + 'resultado_' + teste_atual + '.txt'

        try:
            tempo_execucao = self.perfil_teste(arq_usuario, raio, media_score, arq_resultado, qtd_locais)
            self.output(arq_resultado, teste_atual, tempo_execucao)
        except Exception as e:
            self.fail(teste_atual + ' falhou na execução: ' + str(e))

    def test_ct025_sp(self):
        raio = 10000
        arq_usuario = path_usuario + US1_SP_4
        media_score = 3.5
        qtd_locais = 5

        teste_atual = inspect.currentframe().f_code.co_name
        arq_resultado = path_resultados + 'resultado_' + teste_atual + '.txt'

        try:
            tempo_execucao = self.perfil_teste(arq_usuario, raio, media_score, arq_resultado, qtd_locais)
            self.output(arq_resultado, teste_atual, tempo_execucao)
        except Exception as e:
            self.fail(teste_atual + ' falhou na execução: ' + str(e))

    def test_ct026_sp(self):
        raio = 10000
        arq_usuario = path_usuario + US1_SP_4
        media_score = 3.5
        qtd_locais = 10

        teste_atual = inspect.currentframe().f_code.co_name
        arq_resultado = path_resultados + 'resultado_' + teste_atual + '.txt'

        try:
            tempo_execucao = self.perfil_teste(arq_usuario, raio, media_score, arq_resultado, qtd_locais)
            self.output(arq_resultado, teste_atual, tempo_execucao)
        except Exception as e:
            self.fail(teste_atual + ' falhou na execução: ' + str(e))

    def test_ct027_sp(self):
        raio = 10000
        arq_usuario = path_usuario + US1_SP_4
        media_score = 7
        qtd_locais = 5

        teste_atual = inspect.currentframe().f_code.co_name
        arq_resultado = path_resultados + 'resultado_' + teste_atual + '.txt'

        try:
            tempo_execucao = self.perfil_teste(arq_usuario, raio, media_score, arq_resultado, qtd_locais)
            self.output(arq_resultado, teste_atual, tempo_execucao)
        except Exception as e:
            self.fail(teste_atual + ' falhou na execução: ' + str(e))

    def test_ct028_sp(self):
        raio = 10000
        arq_usuario = path_usuario + US1_SP_4
        media_score = 7
        qtd_locais = 10

        teste_atual = inspect.currentframe().f_code.co_name
        arq_resultado = path_resultados + 'resultado_' + teste_atual + '.txt'

        try:
            tempo_execucao = self.perfil_teste(arq_usuario, raio, media_score, arq_resultado, qtd_locais)
            self.output(arq_resultado, teste_atual, tempo_execucao)
        except Exception as e:
            self.fail(teste_atual + ' falhou na execução: ' + str(e))

    def test_ct029_sp(self):
        raio = 10000
        arq_usuario = path_usuario + US2_SP_10
        media_score = 3.5
        qtd_locais = 5

        teste_atual = inspect.currentframe().f_code.co_name
        arq_resultado = path_resultados + 'resultado_' + teste_atual + '.txt'

        try:
            tempo_execucao = self.perfil_teste(arq_usuario, raio, media_score, arq_resultado, qtd_locais)
            self.output(arq_resultado, teste_atual, tempo_execucao)
        except Exception as e:
            self.fail(teste_atual + ' falhou na execução: ' + str(e))

    def test_ct030_sp(self):
        raio = 10000
        arq_usuario = path_usuario + US2_SP_10
        media_score = 3.5
        qtd_locais = 10

        teste_atual = inspect.currentframe().f_code.co_name
        arq_resultado = path_resultados + 'resultado_' + teste_atual + '.txt'

        try:
            tempo_execucao = self.perfil_teste(arq_usuario, raio, media_score, arq_resultado, qtd_locais)
            self.output(arq_resultado, teste_atual, tempo_execucao)
        except Exception as e:
            self.fail(teste_atual + ' falhou na execução: ' + str(e))

    def test_ct031_sp(self):
        raio = 10000
        arq_usuario = path_usuario + US2_SP_10
        media_score = 7
        qtd_locais = 5

        teste_atual = inspect.currentframe().f_code.co_name
        arq_resultado = path_resultados + 'resultado_' + teste_atual + '.txt'

        try:
            tempo_execucao = self.perfil_teste(arq_usuario, raio, media_score, arq_resultado, qtd_locais)
            self.output(arq_resultado, teste_atual, tempo_execucao)
        except Exception as e:
            self.fail(teste_atual + ' falhou na execução: ' + str(e))

    def test_ct032_sp(self):
        raio = 10000
        arq_usuario = path_usuario + US2_SP_10
        media_score = 7
        qtd_locais = 10

        teste_atual = inspect.currentframe().f_code.co_name
        arq_resultado = path_resultados + 'resultado_' + teste_atual + '.txt'

        try:
            tempo_execucao = self.perfil_teste(arq_usuario, raio, media_score, arq_resultado, qtd_locais)
            self.output(arq_resultado, teste_atual, tempo_execucao)
        except Exception as e:
            self.fail(teste_atual + ' falhou na execução: ' + str(e))

    def test_ct033_sp(self):
        raio = 10000
        arq_usuario = path_usuario + US3_SP_30
        media_score = 3.5
        qtd_locais = 5

        teste_atual = inspect.currentframe().f_code.co_name
        arq_resultado = path_resultados + 'resultado_' + teste_atual + '.txt'

        try:
            tempo_execucao = self.perfil_teste(arq_usuario, raio, media_score, arq_resultado, qtd_locais)
            self.output(arq_resultado, teste_atual, tempo_execucao)
        except Exception as e:
            self.fail(teste_atual + ' falhou na execução: ' + str(e))

    def test_ct034_sp(self):
        raio = 10000
        arq_usuario = path_usuario + US3_SP_30
        media_score = 3.5
        qtd_locais = 10

        teste_atual = inspect.currentframe().f_code.co_name
        arq_resultado = path_resultados + 'resultado_' + teste_atual + '.txt'

        try:
            tempo_execucao = self.perfil_teste(arq_usuario, raio, media_score, arq_resultado, qtd_locais)
            self.output(arq_resultado, teste_atual, tempo_execucao)
        except Exception as e:
            self.fail(teste_atual + ' falhou na execução: ' + str(e))

    def test_ct035_sp(self):
        raio = 10000
        arq_usuario = path_usuario + US3_SP_30
        media_score = 7
        qtd_locais = 5

        teste_atual = inspect.currentframe().f_code.co_name
        arq_resultado = path_resultados + 'resultado_' + teste_atual + '.txt'

        try:
            tempo_execucao = self.perfil_teste(arq_usuario, raio, media_score, arq_resultado, qtd_locais)
            self.output(arq_resultado, teste_atual, tempo_execucao)
        except Exception as e:
            self.fail(teste_atual + ' falhou na execução: ' + str(e))

    def test_ct036_sp(self):
        raio = 10000
        arq_usuario = path_usuario + US3_SP_30
        media_score = 7
        qtd_locais = 10

        teste_atual = inspect.currentframe().f_code.co_name
        arq_resultado = path_resultados + 'resultado_' + teste_atual + '.txt'

        try:
            tempo_execucao = self.perfil_teste(arq_usuario, raio, media_score, arq_resultado, qtd_locais)
            self.output(arq_resultado, teste_atual, tempo_execucao)
        except Exception as e:
            self.fail(teste_atual + ' falhou na execução: ' + str(e))


if __name__ == '__main__':
    unittest.main()
