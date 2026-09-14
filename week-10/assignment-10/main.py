from get.get_pokemon import get_pokemon
from get.get_by_type import get_by_type

def main():
    pokemon=get_pokemon("pikachu")
    types = get_by_type("grass")
    
    if not types:
        return
    
    # types, stats, name
    print(types["pokemon"])
    
if __name__ == "__main__":
    main()