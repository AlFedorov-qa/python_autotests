import requests

URL = 'https://api.pokemonbattle.ru/v2/'
TOKEN = '673a4814b71e3b5094df7558db68433c'
HEADER = {'Content-Type' : 'application/json', 'trainer_token' : TOKEN}

body_create = {
    "name": "Кубон",
    "photo_id": 32
}

body_change = {
    "pokemon_id": "65664",
    "name": "Слоупок",
    "photo_id": 32
}

body_pokeball = {
    "pokemon_id": "65664"
}

'''response_create = requests.post(url = f'{URL}pokemons', headers = HEADER, json = body_create) 
print(response_create.text)''' # Запрос на создание покемона

'''response_change = requests.put(url = f'{URL}pokemons', headers = HEADER, json = body_change)
print(response_change.text)''' # Запрос на изменение покемона

'''response_pokeball = requests.post(url = f'{URL}trainers/add_pokeball', headers = HEADER, json = body_pokeball) 
print(response_pokeball.text)''' # Запрос поймать покемона в покебол