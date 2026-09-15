import json
from get.get_pokemon import get_pokemon
from get.get_by_type import get_by_type
from format.format_pokemon import format_pokemon
from handle.handle_filter import handle_filter

def main():
    pokemon=get_pokemon("Stunfisk")
    #types = get_by_type("grass")
    
    if not pokemon:
        return
    
    # types, stats, name
    # print(json.dumps(types, indent=4))
    # print(format_pokemon(pokemon))
    handle_filter("grass")
    
if __name__ == "__main__":
    main()