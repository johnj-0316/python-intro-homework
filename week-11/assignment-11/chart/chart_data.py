from collections import Counter
from get.get_by_type import get_by_type

def chart_data(pokemon: list):
    count = Counter(p["slot"] for p in pokemon)
            
    return {
        "categories": ["Slot 1", "Slot 2"],
        "quantities": [count[1], count[2]]
    }