import functools

def format_types_and_abilities(types: list[dict], spacing: int = 40):    
    type_ability_names         = [
        (type_ability["type" if "type" in type_ability else "ability"])["name"].capitalize() 
        for type_ability in types
    ]
    type_ability_names_count   = functools.reduce(lambda x, y: x + len(y), type_ability_names, 0)
    type_ability_names_spacing = 4
    
    if type_ability_names_count % 2 == 1:
        type_ability_names_spacing += 1
    
    formatted_types = (" " * type_ability_names_spacing).join(type_ability_names)
    
    if (spacing - len(formatted_types)) % 2 != 0:
        spacing += 1
    
    space_length = (spacing - len(formatted_types)) // 2
    return f"{" " * space_length}{formatted_types}{" " * space_length}"