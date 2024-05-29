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



# obs:No cosseno ajustado a similaridade esta ficando bem proxima de -1 pois os locais possuem muitas categorias, como o cosseno ajustado leva em conta o tamanho dos conjuntos no calculo isso pesa no resultado
