import requests

res = requests.get(
  f'https://restcountries.com/v3.1/region/europe?fields=name,population',
)
content = res.json()
names = content

for i in range(min(10, len(names))):
    print(names[i]["name"]["common"])