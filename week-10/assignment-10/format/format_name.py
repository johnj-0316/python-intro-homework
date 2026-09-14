def format_name(name: str, num_spacing: int = 20):    
    if num_spacing - len(name) % 2 != 0:
            num_spacing += 1
            
    space_length = (num_spacing - len(name)) // 2
    return f"{" " * space_length}{name}{" " * space_length}" 