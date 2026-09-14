import json
from get.get_pokemon import get_pokemon
from get.get_by_type import get_by_type
from format.format_pokemon import format_pokemon

def main():
    pokemon=get_pokemon("stunfisk")
    types = get_by_type("grass")
    
    if not pokemon:
        return
    
    # types, stats, name
    # print(json.dumps(pokemon["types"], indent=4))
    print(format_pokemon(pokemon))
    
if __name__ == "__main__":
    main()