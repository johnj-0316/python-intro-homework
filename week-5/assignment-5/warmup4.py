for i in range(1, 31):
    out = ""
    
    if not i % 3:
        out += "Fizz"
    
    if not i % 5:
        out += "Buzz"
        
    print(out if out else i)
    
