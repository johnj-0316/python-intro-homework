import requests

API_BASE = "https://pokeapi.co/api/v2/pokemon/"

def get_pokemon(name: str):
    res = requests.get(f"{API_BASE}{name}")
    
    if res.status_code != 200:
        raise requests.exceptions.HTTPError("There was an error making the request")
    
    json = res.json()
    return json
    
    