import requests

LIMIT = 10

headers = {
    'Authorization': 'Bearer rc_live_69ccf94c4c5f4c4381b466392cb84fb9',
}

res = requests.get(
  f'https://api.restcountries.com/countries/v5?q=europe&response_fields=names,population&limit={LIMIT}',
  headers=headers
)
content = res.json()
names = content.get("data").get("objects")


for name in names:
    print(name["names"]["common"])