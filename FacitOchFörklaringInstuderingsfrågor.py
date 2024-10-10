# 1.

# 1.1 // är heltalsdivition
print(f"5 Heltalsdivition 2 är: {5//2}")

# 1.2 ** är upphöjt till
print(f"5 Upphöjt till 2 är: {5**2}")

# 1.3 % är modulo och visar hur många som blir över i en divition
print(f"5 Modulo 2 är: {5%2}")

# 2.

# 2.1 Du kan använda alla bokstäver och siffror i variabelnamn men du kan inte börja med en siffra eller använda mellanslag samt specialtecken

# 2.2 Man kan inte använda ord som är reserverade i Python som exempelvis "if" eller "else"

# 2.3 CamelCase är när man skriver variabelnamn med stora bokstäver i början av varje ord som exempelvis "MyVariableName"

# 3. Man konverterar en sträng till en int med int() och en int till en sträng med str()
print(f"Konvertera '5' till en int: {int('5')}")
print(f"Konvertera 5 till en sträng: {str(5)}")

# 4. Man matar in värden från tangentbordet med input() och kan kovertera det till en int med int(input()) eller till float med float(input()) osv.
inputValue = int(input("Skriv in ett heltal: "))
print(f"Du skrev in: {inputValue}")
floatValue = float(input("Skriv in ett decimaltal: "))
print(f"Du skrev in: {floatValue}")
stringValue = input("Skriv in en sträng: ")
print(f"Du skrev in: {stringValue}")

# 5. Man ökar och minskar en variabel med += och -=
value = 5
value += 2
print(f"5 += 2 är: {value}")
value -= 2
print(f"7 -= 2 är: {value}")

# 6. En kommentar i Python skrivs med # och allt efter # ignoreras

# 7. I Python har vi flera jämföringsoperatorer som ==, !=, <, >, <=, >= där == är lika med, != är inte lika med, < är mindre än, > är större än, <= är mindre än eller lika med och >= är större än eller lika med
print(f"5 == 5 är: {5 == 5}")
print(f"5 != 5 är: {5 != 5}")

# 8. Pythons logiska operatorer är and, or och not
print(f"True and False är: {True and False}")
print(f"True or False är: {True or False}")
print(f"not True är: {not True}")

# 9. och 10. En if-sats används för att köra kod beroende på om ett villkor är sant eller falskt och fungerar som följande:
# if villkor: kod
# elif villkor: kod
# else: kod
# elif och else är valfria där elif är en förkortning för else if och används för att kolla flera villkor efter varandra och else används för att köra kod om inget annat villkor är sant
# skillnaden mellan if och elif är att if körs oavsett om ett tidigare villkor är sant eller falskt medan elif körs bara om ett tidigare villkor är falskt

# 11. Match-case används för att kolla flera olika villkor efter varandra och fungerar som följande:
# match variabel: 
#     case villkor: kod
#     case villkor: kod
#     case _: kod

# case _ används för att köra kod om inget annat villkor är sant
# case | används för att kolla flera villkor samtidigt (samma sak som or i en if-sats)

match 5:
    case 1:
        print("1")
    case 2:
        print("2")
    case 5 | 2:
        print("5 eller 2")
    case _:
        print("Inget")

# match-case används för att ersätta flera if-satser och är mer lättläst och effektivt

# 12.

#12.1-2 Man kommer åt första tecknet i en sträng med [0] och sista tecknet med [-1]
print(f"Första tecknet i 'Hej' är: {'Hej'[0]}")
print(f"Sista tecknet i 'Hej' är: {'Hej'[-1]}")

# 12.3 Man ser strängens längd med len(sträng)
print(f"Längden på 'Hej' är: {len('Hej')}")

# 12.4 Att stränar är immutabla betyder att de inte kan ändras efter att de har skapats utan man måste skapa en ny sträng

# Exempel:
# string = "Hej"
# string -= " på dig"
# print(f"string är: {string}")

# Detta kommer ge ett felmeddelande

# 12.5 Man kan göra så att en sträng bara har små eller stora bokstäver med lower() och upper()
print(f"Hej".upper())
print(f"Hej".lower())

# 12.6 Man kan hitta en del av en sträng med find() och rfind()
print(f"Hej på dig".find("p"))
print(f"Hej på dig".rfind(" "))
# skillnaden mellan find() och rfind() är att find() hittar första förekomsten av en del av en sträng medan rfind() hittar sista förekomsten

# 13. När man lägger ihop två strängar med + så kallas det för konkatenering
print(f"Hej" + " på dig")

# 14. slicing används för att ta ut en del av en sträng och fungerar som följande:
# sträng[start:stop:steg]
# start är var slicingen börjar, stop är var den slutar och steg är hur många tecken som hoppas över
print(f"Hej på dig"[0:3])

# 15. f-strängar används för att skriva ut variabler i en sträng och fungerar som följande:
# f"Text {variabel} text"
name = "John"
print(f"Hej {name}")

# 16. Hur loopar man genom sträng i for- respektive while-loop
# For-loop
for char in "Hej på dig":
    print(char)

# While-loop
s = "Hej på dig"
i = 0
while i < len(s):
    print(s[i])
    i += 1

# 17. Hur gör man om en sträng baklänges (med whileloop resp slice)
# While-loop
s = "Hej på dig"
reversed_s = ""
i = len(s) - 1
while i >= 0:
    reversed_s += s[i]
    i -= 1
print(reversed_s)

# Slice
print(s[::-1])

# 18. Hur omvandlar man sträng -> int?
s = "123"
i = int(s)
print(i)
# eller se fråga 3

# 19. Hur vet man vilka rader som ingår i en loop/eller if-sats?
# Indentering visar vilka rader som ingår i en loop eller if-sats
if True:
    print("Denna rad ingår i if-satsen")
    print("Denna också")
print("Denna rad ingår inte i if-satsen")

# 20. Hur kan man bryta en loop?
for i in range(10):
    if i == 5:
        break
    print(i)

# 21. Skillnad på break och continue?
# break avslutar loopen helt
# continue hoppar över resten av koden i loopen och fortsätter med nästa iteration
for i in range(10):
    if i == 5:
        continue
    print(i)

# 22. Vad menas med iteration
# Iteration är processen att gå igenom varje element i en samling, t.ex. en lista eller sträng

# 23. Hur fungerar range (med en, två eller tre parametrar)
# En parameter: stop
print(list(range(5)))  # [0, 1, 2, 3, 4]

# Två parametrar: start, stop
print(list(range(1, 5)))  # [1, 2, 3, 4]

# Tre parametrar: start, stop, step
print(list(range(1, 10, 2)))  # [1, 3, 5, 7, 9]

# 24. Skillnad på Listor och Tuples?
# Listor är mutabla (kan ändras), tuples är immutabla (kan inte ändras)
lista = [1, 2, 3]
tuple = (1, 2, 3)

# 25. Hur gör man följande med Listor?
# 25.1 Skapa tom, och med några världen
tom_lista = []
lista_med_varden = [1, 2, 3]

# 25.2 Lägger till ett värde (finns flera varianter)
lista_med_varden.append(4)

# 25.3 Tar bort ett värde (finns flera varianter)
lista_med_varden.remove(2)

# 25.4 uppdaterar värde
lista_med_varden[0] = 10

# 25.5 Läser visst värde
print(lista_med_varden[1])
# 1 är indexet för det andra värdet i listan

# 25.6 Hur många värden den har
print(len(lista_med_varden))

# 25.7 Sorterar man den
lista_med_varden.sort()

# 25.8 Lägger man ihop två listor?
lista1 = [1, 2]
lista2 = [3, 4]
lista3 = lista1 + lista2

# 26. Hur kopierar men en Lista? (finns flera sätt)
lista_kopia = lista_med_varden.copy()
lista_kopia2 = lista_med_varden[:]
# i exemplen ovan kopieras listan med hjälp av copy() och slicing och är då helt separata från originalet
lista_kopia = lista_med_varden
# i exemplet ovan pekar båda variablerna på samma lista och om den ena ändras ändras den andra också

# 27. Hur fungerar List comprehensions?
# List comprehensions är ett sätt att skapa listor på ett kompakt sätt
squares = [x**2 for x in range(10)]

# 28. Hur gör man följande med dictionaries
# 28.1 Skapa med några världen
dict = {"a": 1, "b": 2}

# 28.2 Lägger till ett värde
dict["c"] = 3

# 28.3 loopar genom
for key, value in dict.items():
    print(key, value)

# 28.4 uppdaterar värde
dict["a"] = 10

# 28.5 ta bort ett värde
del dict["b"]
dict.pop("b")

# 28.6 Läser visst värde
print(dict["a"])

# 28.7 *Sorterar man den
# Dictionaries är osorterade, men man kan sortera nycklarna
sorted_keys = sorted(dict.keys()) # ger en lista med nycklarna sorterade [a, b, c]
sorted_dict_by_keys = sorted(dict.items(), key=lambda item: item[0]) # ger en lista med tuple sorterade efter nycklarna [("a", 2), ("b", 3), ("c", 1)]

# sortera efter värden
sorted_values = sorted(dict.values()) # ger en lista med värdena sorterade [1, 2, 3]
sorted_dict_by_values = sorted(dict.items(), key=lambda item: item[1]) # ger en lista med tuple sorterade efter värdena [("b", 1), ("c", 2), ("a", 3)]

# sortera en dict som är koverterad till en lista
dict_as_list = list(dict.items())
dict_as_list.sort(key=lambda item: item[0]) # samma som sorted_dict_by_keys
# blir sorterad efter nycklarna

dict_as_list.sort(key=lambda item: item[1]) # samma som sorted_dict_by_values
# blir sorterad efter värdena

# 28.8 *göra om till lista
dict_as_list = list(dict.items())
# konertera dict till lista med tuple i [(key, value), (key, value), ...] 

# 29. Lägger man ihop två listor?
lista1 = [1, 2]
lista2 = [3, 4]
lista3 = lista1 + lista2

# 30. Hur skapar man en funktion
def min_funktion():
    # denna skriver ut "Hej" när den anropas
    print("Hej")

# 31. Hur returnerar man ett eller flera värden?
def returnera_varden():
    return 1, 2
# man sparar värdena i en variabel genom att skriva:
var1, var2 = returnera_varden()

# 32. vad kallas de värden som finns mellan ( och )
# De kallas parametrar eller argument

# 33. Hur anropar man en funktion?
min_funktion()

# 34. Hur importerar man moduler?
import math
import random as rnd
from math import sqrt
from random import *
# as används för att ge modulen ett alias
# from används för att importera en specifik funktion från en modul
# * används för att importera alla funktioner från en modul

# 35. Hur fungerar default-värde
def funktion_med_default_varde(param=10):
    print(param)