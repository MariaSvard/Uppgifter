"""
Uppgift 1:

Skapa en klass Person med attributen name och age.
Använd en while-loop med input för att ta emot användarens namn och ålder.
Validera att åldern är ett heltal
Skapa och skriv ut ett Person-objekt om inputen är giltig.

"""
class Person:
    def __init__(self, name, age):
        self.name = name
        self.age = age

    def __str__(self):
        return f"{self.name}: {self.age}"
    
while True:
    name = input("Ange ditt namn: ")
    try:
        age_input = int(input("Ange din ålder: "))
        person = Person(name, age_input)
        print(person)
        break
    except ValueError:
        print("Ogiltig ålder, ange ett heltal")

"""

Uppgift 2:

Skapa en klass Rectangle med attributen length och width.
Implementera metoder för att beräkna arean och omkretsen.
Ta emot och validera input för length och width.
Skriv ut arean och omkretsen

"""
"""
Avancerad:

Skapa ett Python-program som hanterar en enkel dagbok där användaren kan lägga till, läsa
och ta bort inlägg. Programmet ska vara objektorienterat och bestå av minst två klasser.
Exempel på dessa skulle kunna vara Diary och Entry.
Klasser och Objektorienterad Struktur:
Skapa en klass som hanterar dagboken.
Skapa en annan klass som representerar ett enskilt dagboksinlägg.
Dagbokens Funktionalitet:
Dagboken ska kunna:
Läsa in tidigare inlägg från en fil.
Låta användaren skapa nya inlägg.
Visa alla inlägg.
Söka efter ett inlägg med hjälp av en sökterm.
Radera ett inlägg.

"""