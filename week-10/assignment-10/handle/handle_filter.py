from get.get_by_type import get_by_type
from handle.handle_yes import handle_yes

def handle_filter(type: str):
    if not isinstance(type, str):
        print("The input type is not a string!")
        return
    
    type = type.lower()
    
    if not type or not type.isalpha():
        print("Please enter a type into the field below.")
        return
    
    res = get_by_type(type)
    
    if not res:
        print("There was a problem with your input. Please try again.")
        return
    
    pokemon = res["pokemon"]
    limit = 10
    offset = 0
    
    try:
        while True:
            for i in range(offset * limit, min(limit * (offset + 1), len(pokemon))):
                p = pokemon[i]
                slot_type = "st" if p["slot"] == 1 else "nd"
                print(f"{p["pokemon"]["name"].capitalize()} | {p["slot"]}{slot_type} slot")
                
            if not handle_yes("looking through the pokemon (Y/n)"):
                break
            
            offset += 1
    except Exception as e:
        print(f"Something went wrong with getting the pokemon matching the type. {e}")