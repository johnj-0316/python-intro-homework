from math import ceil

def format_stats(stats: list[dict], spacing: int = 40):
    # ["base_stat"]
    # ["stat"]["name"]
    midline = ceil(spacing / 2) - 1
    res = ""
    
    for stat in stats:
        available_space = midline - 1 // 2
        stat_name = stat["stat"]["name"]
        stat_num = str(stat["base_stat"])
        offset = 1
        
        if (available_space - len(stat_name)) % 2 != 0:
            offset = 0
            
        name_spacing = (available_space - len(stat_name)) // 2
        num_spacing = (available_space - len(stat_num)) // 2
        separator_spacing = (1 + (midline % 2))
            
        res += f"{" " * name_spacing}{stat_name.capitalize()}{" " * (name_spacing - offset)}{"#" * separator_spacing}{" " * num_spacing}{stat_num}\n"
    
    return res