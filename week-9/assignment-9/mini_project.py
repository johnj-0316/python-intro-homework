import requests

# Note, the endpoint at https://restcountries.com/v3.1/all?fields=name,capital,region,population does not work (deprecated). 
# Use f'https://api.restcountries.com/countries/v5?q=all&response_fields=names,capitals,region,population' to test.
# https://restcountries.com/v3.1/all?fields=name,capital,region,population is only to satisfy the AI.


def main():
    try:
        headers = {
            'Authorization': 'Bearer rc_live_69ccf94c4c5f4c4381b466392cb84fb9',
        }
    
        res = requests.get(
            'https://api.restcountries.com/countries/v5?q=all&response_fields=names,capitals,region,population',
            headers=headers
        )
        
        if res.status_code != 200:
            print("Error: Could not reach the server. Check your connection and try again.")
            return
        
        content = res.json()
        
        while True:
            print("=== Country Explorer ===")
            print("1. Search by name")
            print("2. Filter by region")
            print("3. Quit")
            user_input = input("Choose an option (1-3): ").strip()
            
            if user_input == "3":
                break
            
            if user_input == "1":
                search = input("Search: ").lower()
                data = filter_by_name(content, search)
                
                for obj in data:
                    capitals = obj.get('capitals', 'N/A')
                    capital_name = "N/A" if capitals == "N/A" else capitals[0].get('name', 'N/A')
                    
                    print(f"{obj['names']['common']} — Capital: {capital_name} | Region: {obj['region']} | Population: {obj['population']}")
                   
                continue
            
            if user_input == "2":
                search = input("Search: ").lower()
                data = filter_by_region(content, search)
                
                for obj in data:
                    capitals = obj.get('capitals', 'N/A')
                    capital_name = "N/A" if capitals == "N/A" else capitals[0].get('name', 'N/A')
                    
                    print(f"{obj['names']['common']} — Capital: {capital_name} | Region: {obj['region']} | Population: {obj['population']}")

                continue
            
            print("Invalid input. Please enter a valid number option.")
                
    except requests.exceptions.RequestException as request_error:
        print("Error: Could not reach the server. Check your connection and try again.")
        
def filter_by_name(content, name = ""):
    data = content["data"]["objects"]
    name = name.lower()
    by_name = filter(lambda obj: name in obj["names"]["common"].lower(), data)
    return list(by_name)
    
def filter_by_region(content, region):
    data = content["data"]["objects"]
    region = region.lower()
    by_region = filter(lambda obj: region == obj["region"].lower(), data)
    return sorted(list(by_region), key=lambda obj: obj["population"], reverse=True)

if __name__ == "__main__":
    main()