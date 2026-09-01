import requests

try:
    res = requests.get("https://thisurldoesnotexist.example.com")
    
    if res.status_code != 200:
        print("Error: Could not reach the server. Check your connection and try again.")
    
except requests.exceptions.RequestException as request_error:
    print("Error: Could not reach the server. Check your connection and try again.")