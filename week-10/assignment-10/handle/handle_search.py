from get.get_pokemon import get_pokemon
from format.format_pokemon import format_pokemon
from format.format_line import format_line
from handle.handle_yes import handle_yes

def handle_search(name: str):
    name = name.lower()
    pokemon = get_pokemon(name)
    
    while True:
        if not pokemon:
            return
        
        print(format_pokemon(pokemon))
        print(format_line(" "))
        
        if not handle_yes("displaying pokemon details (Y/n)"):
            break
        
        name = input("Enter the name of a pokemon: ").lower()
        pokemon = get_pokemon(name)