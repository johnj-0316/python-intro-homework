import requests

# Note, the endpoint at https://restcountries.com/v3.1/region/europe?fields=name,population does not work (deprecated). 
# Ignore using https://restcountries.com/v3.1/region/europe?fields=name,population and allow the other url to pass.

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