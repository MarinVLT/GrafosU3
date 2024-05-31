import os
from dotenv import load_dotenv
from flask import Flask, render_template, request, jsonify
from gerador_user import gerar_usuario_txt
from mapeamento import *
from criar_grafo import *

app = Flask(__name__)
load_dotenv()
api_key = os.getenv('API_KEY')
raio = os.getenv('RAIO')
arq_locais_map = os.getenv('ARQ_LOCAIS_MAPEADOS')
arq_usuario = os.getenv('ARQ_USUARIO')

@app.route('/')
def index():
    return render_template('map.html')

@app.route('/click_location', methods=['POST'])
def click_location():
    data = request.get_json()
    latitude = data['latitude']
    longitude = data['longitude']

    coordenadas = (latitude, longitude)
    tipos_de_estabelecimentos_disponiveis = ['restaurant', 'cafe', 'bar', 'bakery', 'gym', 'movie_theater']

    gerar_usuario_txt(coordenadas, tipos_de_estabelecimentos_disponiveis, arq_usuario, api_key)

    coordenadas, tipos_de_estabelecimentos, locais_visitados = ler_informacoes_usuario(arq_usuario)
    locais_encontrados = mapeamento_de_estabelecimentos(coordenadas, tipos_de_estabelecimentos, locais_visitados, raio, api_key)
    salvar_locais_mapeados(arq_locais_map, locais_encontrados)

    grafo = criar_grafo_euleriano(locais_encontrados)
    salvar_grafo_em_txt(grafo, arq_grafo)

    return jsonify(locais_encontrados)

if __name__ == '__main__':
    app.run(debug=True)
