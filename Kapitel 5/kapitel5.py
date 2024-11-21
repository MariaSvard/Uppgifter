"""
Uppgift 1:

Skriv en funktion calculate som kan ta ett obegränsat antal numeriska argument och en valfri
parameter operation som kan vara 'add', 'subtract', 'multiply' eller 'divide'.
Funktionen ska utföra den specificerade operationen på alla numeriska argument.

"""
def calculate(*args, **kwargs): # skapa en funktion. *args gör att man kan ha hur många siffror som helst
    operation = kwargs.get("operation", "add")

    if not args:
        return None

    if operation == "add":
        result = sum(args)
    elif operation == "substract":
        result = args[0]
        for num in args[1:]:
            result -= num
    elif operation == "multiply":
        result = 1
        for num in args:
            result *= num
    elif operation == "devide":
        result = args[0]
        for num in args[1:]:
            if num == 0:
                return "Error: Zero division not allowed"
        result /= num
    else:
        return "Error: operation not allowed"
    return result

print(calculate(1,2,3,4,5,6, operation="add"))
print(calculate(1,2,3,4,5,6, operation="substract"))
print(calculate(1,2,3,4,5,6, operation="multiply"))

"""
Uppgift 2:

Skriv ett program som använder lambda-uttryck tillsammans med map och filter för att
bearbeta en lista av tal.
Programmet ska först kvadrera alla tal i listan och sedan filtrera ut de tal som är större än ett
angivet värde.
Krav:
Använd map för att kvadrera alla tal i listan.
Använd filter för att behålla endast de tal som är större än ett specificerat värde.
Använd lambda-uttryck för både map och
filter.

"""

