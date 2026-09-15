from format.format_line import format_line
from format.format_name import format_name
from format.format_types_and_abilities import format_types_and_abilities
from format.format_stats import format_stats

def format_pokemon(pokemon_data: dict, spacing: int = 40) -> str:
    name        = str(pokemon_data["name"]).capitalize()
    stats       = pokemon_data["stats"]
    types       = pokemon_data["types"]
    abilities   = pokemon_data["abilities"]
    num_spacing = len(name) + spacing
    
    return (
f"""
{format_line('#', num_spacing)}
{format_name(name, num_spacing)}
{format_line('-', num_spacing)}
{format_types_and_abilities(types, num_spacing)}
{format_line(' ', num_spacing)}
{format_types_and_abilities(abilities, num_spacing)}
{format_line('#', num_spacing)}
{format_stats(stats, num_spacing)}
"""
    )