def format_name(name: str, spacing: int = 40):    
    if (spacing - len(name)) % 2 != 0:
            spacing += 1
            
    space_length = (spacing - len(name)) // 2
    return f"{" " * space_length}{name}{" " * space_length}" 