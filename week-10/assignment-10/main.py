import json
from get.get_pokemon import get_pokemon
from get.get_by_type import get_by_type
from handle.handle_search import handle_search
from handle.handle_filter import handle_filter

def main():
    pokemon=get_pokemon("Stunfisk")
    #types = get_by_type("grass")
    
    if not pokemon:
        return
    
    # types, stats, name
    # print(json.dumps(types, indent=4))
    # handle_filter("grass")
    handle_search("pikachu")
    
if __name__ == "__main__":
    main()