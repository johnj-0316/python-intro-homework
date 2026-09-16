from format.format_name import format_name
from format.format_line import format_line

def menu_display():
    return input(
f"""
{format_name("PokéWeb")}
{format_line("'")}
{format_name("What would you like to do?")}
{" 1. Search for a pokemon by name and display its info"}
{" 2. Search for pokemon by a specific type"}
{" 3. Quit"}

Choice: """)