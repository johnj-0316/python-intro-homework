import get_pokemon

def main():
    pokemon=get_pokemon.get_pokemon("pikachu")
    print(pokemon["stats"])
    
if __name__ == "__main__":
    main()