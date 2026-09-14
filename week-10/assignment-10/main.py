from get_pokemon import get_pokemon

def main():
    pokemon=get_pokemon("pikachu")
    
    if not pokemon:
        return
    
    # types, stats, name
    print(pokemon["types"])
    
if __name__ == "__main__":
    main()