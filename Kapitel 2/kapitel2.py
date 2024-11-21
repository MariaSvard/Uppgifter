"""

Skapa ett username från ett namn

"""

# namn = " aNnA kaRlSsOn "
# str = " aNnA kaRlSsOn "
# print(str.strip()) # tar bort mellanslagen, innan och efter
# print(str.lower()) # alla bokstäver blir små
# print(str.title()) # första bokstaven i varje ord blir stor
# print(namn.replace(" ", "-")) # mellanslaget i namnet ersätts med -

# namn = namn.strip()
# namn = namn.title()
# namn = namn.replace(" ", "-")
# print(namn)

"""

Beställning på ICA

"""
# empty_tuple = ()

# varor = "bröd", "mjölk", "ägg", "smör", "ost", "yoghurt"
# print(varor[:3]) # skriver ut de tre första varorna
# print(varor[4:6]) # skriver ut de sista två varorna
# print(varor[::2]) # skriver ut varannan vara

"""

Topplista med filmer

"""

# empty_list = []

# movies = ["Inception", "The Matrix", "Interstellar", "The Prestige"]
# movies.append("Memento") # lägg till filmen Memento i slutet av listan VIKTIG!!
# print(movies)

# movies[1] = "The Lord of the Rings" # Byt ut filmen "The Matrix" mot "The Lord of the Rings".
# print(movies)

# movies.remove("The Prestige") # Ta bort filmen "The Prestige" från listan
# print(movies)

# movies.insert(2, "The Dark Knight") # Sätt in filmen "The Dark Knight" på position 2 i listan
# print(movies)

"""

Avancerad uppgift

● Extrahera en tuple med namn på alla aktiva studenter (de vars
"aktiv"-status är True).
● Skapa ett set med alla unika ämnen som de aktiva studenterna
studerar.
● Skapa en ordbok där nycklarna är kursnamnen och värdena är antalet
aktiva studenter som är inskrivna i respektive kurs.
● Skriv ut allt detta med print

"""
# Innehåller dictionary, Key = studenter, kurser
data = {
    "studenter": [ # allt som är i denna indentering är värdet i första key
        ("Alice", {"ålder": 25, "ämnen": ("Matematik", "Fysik"), "aktiv": True}), # en tuple, delar i varje
        ("Bob", {"ålder": 22, "ämnen": ("Biologi",), "aktiv": False}),
        ("Charlie", {"ålder": 23, "ämnen": ("Matematik", "Biologi"), "aktiv": True}),
        ("Diana", {"ålder": 24, "ämnen": ("Fysik",), "aktiv": False}),
        ("Eve", {"ålder": 21, "ämnen": ("Matematik", "Fysik", "Biologi"), "aktiv":True}),
    ], # en student per rad
    "kurser": {
        "Matematik": {"studenter": {"Alice", "Charlie", "Eve"}},
        "Fysik": {"studenter": {"Alice", "Diana", "Eve"}},
        "Biologi": {"studenter": {"Bob", "Charlie", "Eve"}},
    }
}

# en tuple går inte att ändra på så man behöver börja med att göra om den till en lista
# sedan gör man om listan till en tuple igen

# Extrahera en tuple med namn på alla aktiva studenter (de vars "aktiv"-status är True):
# skapa en lista
active_students = []
for student in data["studenter"]: # loopar igenom datan i listan "studenter"
    name = student[0]
    details = student[1]
    if details["aktiv"]:
        active_students.append(name)

active_students_tuple = tuple(active_students) # gör om listan till en tuple
print(active_students_tuple)

# Skapa ett set med alla unika ämnen som de aktiva studenterna studerar
# Eftersom ett set tar bort dubletter så kommer den endast ta med de unika ämnena, alltså inte dubbletter

active_subjects = set()
# plocka ut studenterna
for student in data["studenter"]:
    detals = student[1]
    if details["aktiv"]: # kontrollerar om den är true
        subjects = details["ämnen"]
        for subject in subjects: # behöver göra en till forloop eftersom det är flera ämnen i en tuple
            active_subjects.add(subject) # add för att det är ett set

print(active_subjects)

# Skapa en ordbok där nycklarna är kursnamnen och värdena är antalet aktiva studenter som är inskrivna i respektive kurs.
# Nu ska vi gå in på "kurserna"
active_per_course = {}
active_students_set = set(active_students)

for course_name, course_info in data["kurser"].items():
    course_students = course_info["studenter"]
    active_in_course = course_students.intersection(active_students_set)
    active = len(active_in_course) # hur många det är
    active_per_course[course_name] = active

print(active_per_course)


# student1 = data["studenter"][0]
# student2 = data["studenter"][1]
# student3 = data["studenter"][2]
# student4 = data["studenter"][3]
# student5 = data["studenter"][4]

# print(student1)
# print(student2)
# print(student3)
# print(student4)
# print(student5)

# subject1 = student1[1]["ämnen"]
# print(subject1)