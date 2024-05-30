import os
from dotenv import load_dotenv
from flask import Flask, render_template, request, jsonify
import gerador_user
import mapeamento

app = Flask(__name__)
load_dotenv()
api_key = os.getenv('API_KEY')
raio = os.getenv('RAIO')

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

    gerador_user.gerar_usuario_txt(coordenadas, tipos_de_estabelecimentos_disponiveis, 'usuario.txt', api_key)

    coordenadas, tipos_de_estabelecimentos, locais_visitados = mapeamento.ler_informacoes_usuario('usuario.txt')
    locais_encontrados = mapeamento.mapeamento_de_estabelecimentos(coordenadas, tipos_de_estabelecimentos, locais_visitados, raio, api_key)
    mapeamento.salvar_locais_mapeados('locais_mapeados.txt', locais_encontrados)

    return jsonify(locais_encontrados)

if __name__ == '__main__':
    app.run(debug=True)
