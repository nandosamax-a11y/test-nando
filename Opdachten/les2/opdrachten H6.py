# ==========================================
# Voorbeeld Opdracht
# Maak een lijst aan met daarin de volgende getallen: 10, 20 en 30
#
# Voer de volgende opdrachten uit:
# - Voeg het getal 40 toe aan (het einde van) de lijst
#
# Aan het einde print je de lijst 'getallen'.
# ==========================================
from operator import index

# Maak de lijst tafel_van_drie = [3, 6, 9, 12, 16, 18, 24, 27, 32] aan. Je ziet al dat er een aantal waardes niet kloppen.
#
# Gebruik een toekenning om 16 in 15 te veranderen
# Gebruik de methode remove() om 32 te verwijderen
# Gebruik de methode append() om 30 toe te voegen aan het eind van de lijst
# Gebruik de methode insert() om 21 toe te voegen tussen 18 en 24
#
# tafel_van_drie = [3, 6, 9, 12, 16, 18, 24, 27, 32]
# tafel_van_drie[4] = 15
# tafel_van_drie.remove(32)
# tafel_van_drie.append(30)
# tafel_van_drie.insert(6,21)
#
# print(tafel_van_drie)



# getallen = [10, 20, 30]
#
# # Voeg het getal 40 toe aan (het einde van) de lijst
# getallen.append(40)
# print('list na toevoeging 40 aan het einde van de lijst: ', getallen)  # Het resultaat is: [10, 20, 30, 40]


# ==========================================
# Opdracht 1:
# Maak een lijst met daarin de volgende getallen: 2, 4, 7, 11 en 19
# Voer de volgende opdrachten uit:
# - Voeg het getal 22 toe aan (het einde van) de lijst
# - Voeg het getal 6 toe tussen 4 en 7
# - Vervang het getal 4 door het getal 5
# - Print de lijst 'getallen'
#
#
# getallen = [2, 4, 7, 11 ,19]
# getallen.append(22)
# getallen.insert(2,6)
# getallen[1] = 5
# print(getallen)


# Verwachte uitkomst: [2, 5, 6, 7, 11, 19, 22]
# ==========================================

# list5 = [getal for getal in range(1,21)if getal % 2 == 0]
# print(list5)


# ==========================================
# Opdracht 2:
# In de Fibonacci rij bestaat elk getal uit de som van de twee voorgaande getallen: 1, 1, 2, 3, 5, 8 enzovoorts
# De som van 1 en 1 is 2, de som van 1 en 2 is 3, enzovoorts. Implementeer de functie ‘fibonacci’ die een lijst als parameter meekrijgt.
# Voer de volgende opdrachten uit:
# - Maak een variabele aan genaamd 'fibonacci_start_reeks' en geef  die de eerste twee elementen van de Fibonacci reeks.
# - Maak een functie genaamd fibonacci die de fibonacci_reeks uitbreidt met een nieuw element.
# - Roep de functie 5 keer aan (Bijvoorbeeld met een for-loop).
# - Print de waarde van de fibonacci_reeks
#
# Verwachte uitkomst:   [1, 1, 2, 3, 5, 8, 13]
# ==========================================
#
#
# reeks = [0,1,1,2,3]
# while reeks[-1] < 0:
#     getal1 = reeks[-1]
#     getal2 = reeks[-2]
#     add = getal1 + getal2
#     reeks.append(add)
#
# print(reeks)



# ==========================================
# Opdracht 3:
# Maak een lijst ‘kwadraten’ die de kwadraten bevat van de getallen 1 tot en met 10. Gebruik een for loop.
#
# Verwachte uitkomst:  [1, 4, 9, 16, 25, 36, 49, 64, 81, 100]
# ==========================================

# lijst22 = [getal ** 2 for getal in range(1,11)]
# print(lijst22)



# ==========================================
# Voorbeeld opdracht:
# Declareer twee tuples met de namen ‘tuple_een’ en ‘tuple_twee’.
# tuple_een krijgt de waarden 1, 2 en 3. tuple_twee krijgt de waarden 4, 5 en 6.
# Zorg dat je een tuple krijgt met de waarden 1, 2, 3, 4, 5 en 6. Onthoud dat tuples onveranderlijk zijn.
# # ==========================================
#
# tuple_een = (1, 2, 3)
# tuple_twee = (4, 5, 6)
#
# # je zal een nieuwe tuple variabele moeten declareren. De tuples die al gedeclareerd zijn kunnen niet worden aangepast
# # (zoals een list kan worden aangepast met append, insert en remove).
# combined_tuple = tuple_een + tuple_twee
# print('combined tuple: ', combined_tuple)  # Het resultaat is: (1, 2, 3, 4, 5, 6
#


# ==========================================
# Opdracht 1:
# maak een tuple aan met de waarden 'b', 'c', 'a'
# print de waarden van de tuple in de alfabetische volgorde (a, b, c)
# Tip: maak gebruik van de indexen van de tuple
#
# Verwachte uitkomst:  a b c
# ==========================================

acb_lijst = 'b', 'c', 'a'
print(acb_lijst)
print(type(acb_lijst))
sorteer_acb_lijst = sorted(acb_lijst)
print(sorteer_acb_lijst)

# ==========================================
# Opdracht 2:
# Maak de lijst ‘getal_kwadraat_paar’ aan voor getallen 1 tot en met 5 waarin elk element bestaat uit een tuple die het getal en het bijbehorende kwadraat bevat.
# Gebruik een list comprehension.
#
# Verwachte uitkomst: [(1, 1), (2, 4), (3, 9), (4, 16), (5, 25)]
# ==========================================

getal_kwadraat_paar = []
for x in range (6):
    getal_kwadraat_paar.append((x,pow(x,2)))
print(getal_kwadraat_paar)

# getal_kwadraat_paar = []
# for x in range (6):
#     getal_kwadraat_paar.append((x,pow(x,2)))




# =========================================
# Opdracht 3:
# Maak een tuple genaamd tuple_count met de waarden 1, 2, 3, 4, 5
# Draai de volgorde van de getallen om. Zorg dat je een nieuwe tuple krijgt met de waarden 5, 4, 3, 2, 1
# Tip: Maak gebruik van de reversed() functie
#
# Verwachte uitkomst: (5, 4, 3, 2, 1)
# ==========================================

list2 = [1, 2, 3, 4, 5]
list2.sort(reverse=True)
print (list2)