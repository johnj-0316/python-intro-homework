language_list_1 = ["Python", "JavaScript", "Java", "Go"]
language_list_2 = ["Rust", "JavaScript", "SQL", "Go"]

language_set_1 = set(language_list_1)
language_set_2 = set(language_list_2)

print(f"Union: {language_set_1 | language_set_2}")
print(f"Intersection: {language_set_1 & language_set_2}")
print(f"Difference: {language_set_1 - language_set_2}")