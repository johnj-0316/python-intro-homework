import requests

res = requests.get("https://api.agify.io/?name=michael")
content = res.json()
print(f"Name: {content.get('name')}")
print(f"Predicted age: {content.get('age')}")
print(f"Birthday: {content.get('birthday', 'Not available')}")