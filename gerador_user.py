import os
import googlemaps
import random
from dotenv import load_dotenv

def gerar_usuario_txt(coordenadas, tipos_de_estabelecimentos, arquivo_saida, api_key):
    gmaps = googlemaps.Client(key=api_key)
    with open(arquivo_saida, 'w') as file:
        # Escreve as coordenadas no arquivo
        file.write(','.join(map(str, coordenadas)) + '\n')

        # Escolhe aleatoriamente os tipos de estabelecimentos
        tipos_escolhidos = random.sample(tipos_de_estabelecimentos, k=2)
        # Escreve os tipos de estabelecimentos no arquivo
        file.write(','.join(tipos_escolhidos) + '\n')

        # Escolhe aleatoriamente a quantidade de locais a serem gerados (de 0 a 5)
        quantidade_locais = random.randint(1, 5)
        for _ in range(quantidade_locais):
            # Escolhe aleatoriamente um tipo de estabelecimento da lista
            tipo_estabelecimento = random.choice(tipos_escolhidos)

            # Busca um local próximo do tipo escolhido
            resultados = gmaps.places_nearby(location=coordenadas, radius=1000, type=tipo_estabelecimento)

            # Se houver resultados, escolhe aleatoriamente um local e escreve suas informações no arquivo
            if resultados['results']:
                local = random.choice(resultados['results'])
                nome = local.get('name', 'N/A')
                tipos = ','.join(local.get('types', []))
                avaliacao = local.get('rating', -1) # -1 -> N/A
                file.write(f"{nome},{tipos},{avaliacao}\n")
        print("Usuario.txt gerado com sucesso!")


# Atribuir as configurações do .env a uma variável
load_dotenv()
api_key = os.getenv('API_KEY')

# Coordenadas de exemplo (Alecrim, Natal, RN, Brasil)
coordenadas = (-5.800040515341294, -35.221718181711076)

# Lista de tipos de estabelecimentos disponíveis
tipos_de_estabelecimentos_disponiveis = ['restaurant', 'cafe', 'bar', 'bakery', 'gym', 'movie_theater'] # aumentar essa lista?

# Nome do arquivo de saída
arquivo_saida = 'usuario.txt'


# Gera o arquivo usuario.txt
# gerar_usuario_txt(coordenadas, tipos_de_estabelecimentos_disponiveis, arquivo_saida, api_key)
