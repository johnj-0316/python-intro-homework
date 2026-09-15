from get.get_pokemon import get_pokemon
from format.format_pokemon import format_pokemon
from format.format_line import format_line
from handle.handle_yes import handle_yes

def handle_search(name: str):
    name = name.lower()
    pokemon = get_pokemon(name)
    
    try:
        while True:
            if not isinstance(name, str):
                    print("The input type is not a string!")
                    return
                
            if not name:
                print("Please enter a name into the field below.")
                return
            
            if not pokemon:
                print("There was a problem with your input. Please try again.")
                return
            
            print(format_pokemon(pokemon[0]))
            print(format_line(" "))
            
            if not handle_yes("displaying pokemon details (Y/n)"):
                break
            
            name = input("Enter the name of a pokemon: ").lower()
            pokemon = get_pokemon(name)
    except Exception as e:
        print(f"Something went wrong with searching for the pokemon. {e}")