while True:
    try:
        num1 = float(input("První číslo: "))
        op = input("Operace(+ , - , * , /): ")
        num2 = float(input("Druhé číslo: "))
    except ValueError:
        print("Neplatný vstup.")
        continue
    
    if op == "+":
        print(f"{num1 + num2}")
    if op == "-":
        print(f"{num1 - num2}")
    if op == "*":
        print(f"{num1 * num2}")
    if op == "/":
        if num2 == 0:
            print("nelze dělit nulou")
        else:
            print(f"{num1 / num2}")
    else:
        print("Neplatný operátor")
        
    
    if input("pokračovat? (n = konec): ").lower() == "n":
        break
    
    
    
        