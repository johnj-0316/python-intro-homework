def greet(name: str, greeting: str = "Hello"):
    print(f"{greeting}, {name}!")
    
greet("Alex")
greet("Alex", "Good morning")
greet("Alex", "Hello")