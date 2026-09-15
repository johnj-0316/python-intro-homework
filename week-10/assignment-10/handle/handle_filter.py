from get.get_by_type import get_by_type
from handle.handle_yes import handle_yes

def handle_filter(type: str):
    type = type.lower()
    res = get_by_type(type)
    
    if not res:
        return
    
    pokemon = res["pokemon"]
    limit = 10
    offset = 0
    
    while True:
        for i in range(offset * limit, min(limit * (offset + 1), len(pokemon))):
            p = pokemon[i]
            slot_type = "st" if p["slot"] == 1 else "nd"
            print(f"{p["pokemon"]["name"].capitalize()} | {p["slot"]}{slot_type} slot")
            
        if not handle_yes("looking through the pokemon"):
            break
        
        offset += 1