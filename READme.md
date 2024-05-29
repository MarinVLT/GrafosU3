# GOOGLE MAPS (PLACES API)

teste usando a API places para pegar os locais mais proximo de uma cordenada passada.
(A chave de API funcionando no meu endereço de IP)

obs: entrar no venv para rodar (linux: source myenv/bin/activate)

# TIPOS DE ESTABELECIMENTOS

    1. Estabelecimentos gerais:
        accounting
        airport
        amusement_park
        aquarium
        art_gallery
        atm
        bakery
        bank
        bar
        beauty_salon
        bicycle_store
        book_store
        bowling_alley
        bus_station
        cafe
        campground
        car_dealer
        car_rental
        car_repair
        car_wash
        casino
        cemetery
        church
        city_hall
        clothing_store
        convenience_store
        courthouse
        dentist
        department_store
        doctor
        drugstore
        electrician
        electronics_store
        embassy
        fire_station
        florist
        funeral_home
        furniture_store
        gas_station
        gym
        hair_care
        hardware_store
        hindu_temple
        home_goods_store
        hospital
        insurance_agency
        jewelry_store
        laundry
        lawyer
        library
        light_rail_station
        liquor_store
        local_government_office
        locksmith
        lodging
        meal_delivery
        meal_takeaway
        mosque
        movie_rental
        movie_theater
        moving_company
        museum
        night_club
        painter
        park
        parking
        pet_store
        pharmacy
        physiotherapist
        plumber
        police
        post_office
        real_estate_agency
        restaurant
        roofing_contractor
        rv_park
        school
        shoe_store
        shopping_mall
        spa
        stadium
        storage
        store
        subway_station
        supermarket
        synagogue
        taxi_stand
        train_station
        transit_station
        travel_agency
        university
        veterinary_care
        zoo

    2. Tipos de comida e bebida:
        bakery
        bar
        cafe
        meal_delivery
        meal_takeaway
        restaurant

    3. Compras e serviços:
        clothing_store
        convenience_store
        department_store
        electronics_store
        furniture_store
        hardware_store
        home_goods_store
        jewelry_store
        liquor_store
        pet_store
        shoe_store
        shopping_mall
        store
        supermarket

    4. Infraestrutura e transporte:
        airport
        bus_station
        car_rental
        car_repair
        car_wash
        gas_station
        light_rail_station
        parking
        subway_station
        taxi_stand
        train_station
        transit_station

    5. Saúde e serviços médicos:
        dentist
        doctor
        hospital
        pharmacy
        physiotherapist
        veterinary_care

    6. Serviços públicos e locais de interesse:
        atm
        bank
        church
        city_hall
        courthouse
        embassy
        fire_station
        library
        local_government_office
        mosque
        police
        post_office
        school
        synagogue
        university

    7. Recreação e entretenimento:
        amusement_park
        aquarium
        art_gallery
        bowling_alley
        casino
        movie_theater
        museum
        night_club
        park
        spa
        stadium
        zoo


import googlemaps
import math

locais_visitados = [
    {
        'nome': 'Restaurante X',
        'tipos': ['restaurant', 'establishment', 'meal_takeaway', 'point_of_interest', 'food'],
        'avaliacao': 4.5  # Avaliação do usuário para o local visitado
    },
    {
        'nome': 'Café Y',
        'tipos': ['cafe', 'establishment', 'food', 'point_of_interest'],
        'avaliacao': 4.2  # Avaliação do usuário para o local visitado
    },
    {
        'nome': 'Bar Z',
        'tipos': ['bar', 'establishment', 'point_of_interest', 'food'],
        'avaliacao': 4.0  # Avaliação do usuário para o local visitado
    }
]

#Jaccard varia de 0 a 1, sendo 1 a similaridade perfeita (se for usar tem que achar um artigo/documento bom)
def jaccard_similarity(conjunto1, conjunto2):
    intersecao = len(conjunto1.intersection(conjunto2))
    uniao = len(conjunto1.union(conjunto2))
    return intersecao / uniao if uniao > 0 else 0

#cosseno ajustado leva em conta o tamnho dos conjuntos (Aqui: o quao mais proximo de 0, mais similar)
# def cosseno_ajustado(conjunto1, conjunto2):
#    intersecao = len(conjunto1.intersection(conjunto2))
#    tamanho_conjunto1 = len(conjunto1)
#    tamanho_conjunto2 = len(conjunto2)
#    denominador = math.sqrt((tamanho_conjunto1 + 1) * (tamanho_conjunto2 + 1))
#    return (intersecao - (tamanho_conjunto1 + tamanho_conjunto2 - intersecao)) / denominador

def mapeamento_de_estabelecimentos(tipos_de_estabelecimentos, radius, coordenadas, api_key):
    gmaps = googlemaps.Client(key=api_key)
    todos_estabelecimentos = {}

    for tipo in tipos_de_estabelecimentos:
        resultados = gmaps.places_nearby(location=coordenadas, radius=radius, type=tipo)
        
        if resultados['results']:
            for resultado in resultados['results']:
                place_id = resultado['place_id']
                detalhes = gmaps.place(place_id=place_id)
                score = 0
                
                if detalhes.get('result'):
                    lugar = detalhes['result']
                    tipos_do_local = lugar.get('types')
                    
                    for tipo_desejado in tipos_de_estabelecimentos:
                        if tipo_desejado in tipos_do_local:
                            score += 1
                    
                    todos_estabelecimentos[place_id] = {
                        'nome': lugar.get('name'),
                        'endereco': lugar.get('formatted_address'),
                        'tipos': tipos_do_local,
                        'avaliacao_geral': lugar.get('rating'),
                        'atributos': lugar.get('attributes', []),
                        'score': score,
                        # 'sim_locais_locais': max([cosseno_ajustado(set(tipo_local['tipos']), tipos_do_local) for tipo_local in locais_visitados])
                        'sim_locais_locais': max([jaccard_similarity(set(tipo_local['tipos']), tipos_do_local) for tipo_local in locais_visitados])
                    }
    
    return todos_estabelecimentos

# Exemplo de uso da função
coordenadas = (-5.800040515341294, -35.221718181711076)  # Exemplo: Local qualquer no alecrim
tipos_de_estabelecimentos = ['restaurant', 'cafe', 'bar']
radius = 1000
api_key = 'AIzaSyDTFAqbj8RFJUTeA_Mqb4Wu0ZCf6TULHR4'

locais_encontrados = mapeamento_de_estabelecimentos(tipos_de_estabelecimentos, radius, coordenadas, api_key)

# Exibir os locais encontrados com o campo 'sim_locais_tipos' adicionado
print("Locais encontrados:")
for local_id, local in locais_encontrados.items():
    print(f"Nome: {local['nome']}")
    print(f"Endereço: {local['endereco']}")
    print(f"Tipos: {', '.join(local['tipos'])}")
    print(f"Avaliação Geral: {local['avaliacao_geral']}" if local['avaliacao_geral'] is not None else "Avaliação Geral: Não disponível")
    print(f"Sim_locais_locais: {local['sim_locais_locais']}")
    print(f"Score: {local['score']}") 
    print(f"Score_final: {local['sim_locais_locais'] + local['score']}")
    print("-" * 40)

# similaridade esta sendo calculado com base nos tipos 
# obs:No cosseno ajustado a similaridade esta ficando bem proxima de -1 pois os locais possuem muitas categorias, como o cosseno ajustado leva em conta o tamanho dos conjuntos no calculo isso pesa no resultado
