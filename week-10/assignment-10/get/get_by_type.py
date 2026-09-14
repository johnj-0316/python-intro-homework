import requests
from get.get_api_endpoint import get_api_endpoint

API_TYPE_BASE = get_api_endpoint("type")

def get_by_type(type: str):
    try:
        res = requests.get(f"{API_TYPE_BASE}{type}")
        
        if res.status_code != 200:
            raise requests.exceptions.HTTPError("Invalid status code")
        
        json = res.json()
        return json
        
    except requests.exceptions.HTTPError as http_err:
        print(f"The request returned a bad status code: {http_err}")
        
    except requests.exceptions.RequestException as req_err:
        print(f"There was an error: {req_err}")