from menu.menu_display import menu_display
from handle.handle_search import handle_search
from handle.handle_filter import handle_filter

def menu_loop():
    user_input = menu_display()
    
    while True:
        match user_input:
            case "1":
                search_input = input("Enter the name of a pokemon: ")
                handle_search(search_input)
            
            case "2":
                filter_input = input("Enter a valid pokemon type: ")
                handle_filter(filter_input)
                
            case "3":
                break
            
            case _:
                print("Please enter a valid value for the menu to work.")
                
        user_input = menu_display()