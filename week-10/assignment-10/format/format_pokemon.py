from format.format_line import format_line
from format.format_name import format_name
from format.format_types import format_types

def format_pokemon(pokemon_data: dict) -> str:
    name = str(pokemon_data["name"]).capitalize()
    stats = pokemon_data["stats"]
    types = pokemon_data["types"]
    
    num_spacing = len(name) + 14
    
    return (
f"""
{format_line("#", num_spacing)}
{format_name(name, num_spacing)}
{format_line("-", num_spacing)}
{format_types(types, num_spacing)}
{format_line("#", num_spacing)}
"""
    )