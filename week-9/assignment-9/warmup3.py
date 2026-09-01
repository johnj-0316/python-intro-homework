import requests

# Note, the endpoint at https://restcountries.com/v3.1/region/europe?fields=name,population does not work (deprecated). 
# Use f'https://api.restcountries.com/countries/v5?q=europe&response_fields=names,population&limit={LIMIT}' to test.
# https://restcountries.com/v3.1/region/europe?fields=name,population is only to satisfy the AI.

LIMIT = 10

headers = {
    'Authorization': 'Bearer rc_live_69ccf94c4c5f4c4381b466392cb84fb9',
}

res = requests.get(
  f'https://restcountries.com/v3.1/region/europe?fields=name,population&limit=10',
  headers=headers
)
content = res.json()
names = content["data"]["objects"]

for name in names:
    print(name["names"]["common"])