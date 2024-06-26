import os
from dotenv import load_dotenv
from flask import Flask, render_template, request, jsonify
from folium import folium


from gerador_usuario import gerar_usuario_txt
from mapeamento import *
from criar_grafo import *
from hierholzer_modificado import *

app = Flask(__name__)
load_dotenv()
arq_locais_map = os.getenv('ARQ_LOCAIS_MAPEADOS')
arq_usuario = os.getenv('ARQ_USUARIO')
arq_resultado = os.getenv('ARQ_RESULTADOS')
arq_grafo = os.getenv('ARQ_GRAFO')

@app.route('/', methods=['GET', 'POST'])
def index():
    return render_template('index.html')

@app.route('/places-location', methods=['POST'])
def places_location():
    data = request.get_json()
    latitude = data['latitude']
    longitude = data['longitude']
    tipo_locais = data['locais']
    raio = data['raio']
    num_locais = int(data['num_locais'])

    coordenadas = (latitude, longitude)
    gerar_usuario_txt(coordenadas, tipo_locais, arq_usuario)

    coordenadas, tipos_de_estabelecimentos, locais_visitados = ler_informacoes_usuario(arq_usuario)
    locais_encontrados = mapeamento_de_estabelecimentos(coordenadas, tipos_de_estabelecimentos, locais_visitados, raio)
    #salvo para controle
    salvar_locais_mapeados(arq_locais_map, locais_encontrados)

    grafo = criar_grafo_euleriano(locais_encontrados)
    #salvo para controle
    salvar_grafo_txt(grafo, arq_grafo)

    locais = hierholzer_modificado(grafo,num_locais, 5,tipo_locais)
    #salvo para controle
    salvar_resultado_txt(grafo, locais, arq_resultado)

    return jsonify(locais)

if __name__ == '__main__':
    app.run(debug=True)
