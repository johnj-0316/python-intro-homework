def celsius_to_fahrenheit(c: float) -> str:
    return f"{c}°C = {(c * 9 / 5) + 32:.1f}°F"

def fahrenheit_to_celsius(f: float) -> str:
    return f"{f}°F = {(f - 32) * 5 / 9:.1f}°C"

print(celsius_to_fahrenheit(0))
print(celsius_to_fahrenheit(100))
print(fahrenheit_to_celsius(72))