"""

FizzBuzz

Loopa genom 1-100 med följande regler:
● Om talet är delbart med 3, skriv ut "Fizz".
● Om talet är delbart med 5, skriv ut "Buzz".
● Om talet är delbart med både 3 och 5, skriv ut "FizzBuzz".
● Annars, skriv ut talet självt.

"""
"""

Logganalys

Öppna filen log.txt och läs in den
Skriv ut varje rad i filen som innehåller "Failed login attempt" (utan tomrader)

"""
"""

Password spraying
password_spraying.py

Kontrollera om någon utav lösenorden i password_list matchar lösenordet för en
user i user_credentials
Skriv resultatet till fil (och i konsolen) med varje lösenord per user och om det
lyckades eller inte.
Exempel:
user1: 123456 -> failed
user1: Welcome123 -> failed

"""
# Lista över användarnamn och deras korrekta lösenord
# user_credentials = {
#     "user1": "Password123",
#     "admin": "Admin@2023",
#     "user2": "Welcome123",
#     "guest": "Guest1234"
}

# En lista över vanligt använda lösenord
# password_list = ["Password123", "123456", "Welcome123", "Guest1234", "password"]

# with open("spray.txt", "w") as file: # öppnar filen som vi vill skriva till
#     for username in user_credentials.keys():
#         for password in password_list: # loopar igenom varje keys, lösenord
#             if password == user_credentials[username]:
#                 result = "success" # kontrollerar om de är likadana
#             else:
#                 result = "failed"
            
#             file.write(f"{username}: {password} => {result}\n")
#             print(f"{username}: {password} => {result}")

"""

IP pinger

Lägg till IP-adresser i en text fil (en ip-adress per rad).
Öppna filen och pinga varje ip-adress. Skriv ut resultatet till terminalen och till en fil.
Använd följande i toppen av ditt skript:
import os
Os-funktion för att pinga en adress (en funktion för win och en för linux):
os.system(f"ping -c 1 {ip_address} > /dev/null 2>&1") # Linux
os.popen(f"ping -n 1 {ip_address}").read() # Windows

"""

