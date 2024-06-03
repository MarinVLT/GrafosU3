# Como rodar o projeto

Com o python instalado, instalar o gerenciador de pacotes pipenv:

```
pip install pipenv
```

Com o pipenv instalado, fazer o download das dependências do projeto:

```
pipenv install
```

## Testes
```
python -m unittest discover -s testes -p 'test_*.py'
```
## Etapas de Execução
### 1. Gerar usuário
### 2. Gerar mapa
### 

# Google Maps
📌🗺 [Places API](https://console.cloud.google.com/marketplace/product/google/places.googleapis.com?hl=en&project=level-epoch-424911-t1)

Usando a API places para pegar os locais mais proximo de uma cordenada passada.
(É necessário configurar sua própria chave da API para o seu endereço de IP)

Obs: entrar no venv para rodar (linux: source myenv/bin/activate)



# Tipos de Estabelecimentos
| Categoria            | Tipos de Comida e Bebida | Compras e Serviços | Infraestrutura e Transporte | Saúde e Serviços Médicos | Serviços Públicos e Locais de Interesse | Recreação e Entretenimento |
|----------------------|--------------------------|-------------------|-----------------------------|--------------------------|-----------------------------------------|----------------------------|
| **(1)**              | bakery                   | clothing_store    | airport                     | dentist                  | atm                                     | amusement_park             |
| **(2)**              | bar                      | convenience_store | bus_station                 | doctor                   | bank                                    | aquarium                   |
| **(3)**              | cafe                     | department_store  | car_rental                  | hospital                 | church                                  | art_gallery                |
| **(4)**              | meal_delivery            | electronics_store | car_repair                  | pharmacy                 | city_hall                               | bowling_alley              |
| **(5)**              | meal_takeaway            | furniture_store   | car_wash                    | physiotherapist          | courthouse                              | casino                     |
| **(6)**              | restaurant               | hardware_store    | gas_station                 | veterinary_care          | embassy                                 | movie_theater              |
| **(7)**              |                          | home_goods_store  | light_rail_station          |                          | fire_station                            | museum                     |
| **(8)**              |                          | jewelry_store     | parking                     |                          | library                                 | night_club                 |
| **(9)**              |                          | liquor_store      | subway_station              |                          | local_government_office                 | park                       |
| **(10)**             |                          | pet_store         | taxi_stand                  |                          | mosque                                  | spa                        |
| **(11)**             |                          | shoe_store        | train_station               |                          | police                                  | stadium                    |
| **(12)**             |                          | shopping_mall     | transit_station             |                          | post_office                             | zoo                        |
| **(13)**             |                          | store             |                             |                          | school                                  |                            |
| **(14)**             |                          | supermarket       |                             |                          | synagogue                               |                            |
| **(15)**             |                          |                   |                             |                          | university                              |                            |
| **Total por coluna** | **6**                    | **14**            | **12**                      | **6**                    | **15**                                  | **12**                     |
| **Total geral**      | **65**                   |                   |                             |                          |                                         |                            |
