"""

Multiplikationstabellen

Skapa ett program som genererar och skriver ut en multiplikationstabell för ett tal
som användaren matar in.
Krav:
● En funktion för att skapa en multiplikationstabell.
● Programmet ska fråga användaren vilket tal som ska multipliceras och till
vilket maxvärde.
● En funktion för att kontrollera om den inmatade strängen bara innehåller
siffror. Använd funktionen isdigit()
● Skriv ut tabellen

"""
"""

Miniräknare

Skapa en enkel miniräknare som kan utföra addition, subtraktion, multiplikation och
division.
Krav:
● Funktioner för varje matematiskt operation.
● Programmet ska ta in två tal från användaren och en operation som input.
● Hantera felaktig inmatning och division med 0.

"""
"""

Shoppinglista

Skapa ett program som hanterar en inköpslista. Programmet ska kunna:
● Lägga till, ta bort och visa alla varor till inköpslistan.
● Spara inköpslistan till en textfil (användaren får välja filnamn).
Krav:
● Programmet ska ha en meny där användaren kan välja att lägga till varor, visa
listan, ta bort varor, spara listan eller avsluta programmet.
● Använd funktioner för att strukturera koden och hantera varje menyval.

"""
# skapa en funtion

def add_item(shopping_list):
    item = input("Enter the item you want to add: ")
    shopping_list.append(item)
    print(f"{item} was added to shopping list")

def display_list(shopping_list): # kontrollerar att den finns
    if shopping_list:
        print("Shopping list:")
        for i, item in enumerate(shopping_list, 1):
            print(f"{i}. {item}") # loopar igenom för att få fram index
    else:
        print("Shoppinglist is empty!")

def remove_item(shopping_list):
    display_list(shopping_list) # visa användaren listan så att man vet vad som ska tas bort
    if shopping_list:
        item_number = input("Enter the number to remove: ")
        if item_number.isdigit() and 1 <= int(item_number) <= len(shopping_list):
        # kontrollera att det är en suffra som anges, större eller lika med 1, mindre än shoppinglistan
            removed_item = shopping_list.pop(int(item_number) - 1) # ta bort
            print(f"{removed_item} has been removed") # skriva vad vi vill ta bort
        else:
            print("Invalid item number")

def save_list(shopping_list):
    if shopping_list:
        filename = input("Enter filename: ")
        with open(filename, "w") as file:
            for item in shopping_list:
                file.write(item + "\n")
        print(f"Shopping list has been saved to: {filename}")
    else:
        print("List is empty!")

# börja med att göra menyn så att man vet vad man vill ha

def main():
    shopping_list = [] # skapa en tom lista och definera den

    while True:
        print("\nMenu:")
        print("1. Add an item")
        print("2. Display shopping list")
        print("3. Remove item")
        print("4. Save as file")
        print("5. Exit")
        choice = input("Choose an option: ")

        if choice == "1":
            add_item(shopping_list)
        if choice == "2":
            display_list(shopping_list)
        if choice == "3":
            remove_item(shopping_list)
        if choice == "4":
            save_list(shopping_list)
        if choice == "5":
            break

main()

# dela sedan upp så att man kan välja
