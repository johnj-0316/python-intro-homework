fahrenheit_input = float(input("Enter a temperature in Fahrenheit: "))
celsius = (fahrenheit_input - 32) * 5 / 9
print(f"{round(fahrenheit_input, 1)}°F is {round(celsius, 1)}°C") 