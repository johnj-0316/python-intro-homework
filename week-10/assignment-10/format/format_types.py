import functools

def format_types(types: list[dict], num_spacing: int = 20):    
    type_names         = [type_name["type"]["name"].capitalize() for type_name in types]
    type_names_count   = functools.reduce(lambda x, y: x + len(y), type_names, 0)
    type_names_spacing = 2
    
    if type_names_count % 2 == 1:
        type_names_spacing += 1
    
    formatted_types = (" " * type_names_spacing).join(type_names)
    
    if num_spacing - len(formatted_types) % 2 != 0:
        num_spacing += 1
    
    space_length    = (num_spacing - len(formatted_types)) // 2
    return f"{" " * space_length}{formatted_types}{" " * space_length}"