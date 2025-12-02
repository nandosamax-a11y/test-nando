# ==========================================
# Voorbeeld Opdracht
# Gegeven zijn de variabelen a = 3 en b = 10. Evalueer met een if statement of a groter is dan b. Als dat zo is, print dan a. Als dat niet zo is, print dan b.
# # ==========================================
#
# a = 3
# b = 10
#
# if a > b:
#     print(a)
# else:
#     print(b)
from http.cookiejar import join_header_words

# ==========================================
# Opgave 1:
# Gegeven is een int input getal_1 en getal_2 en drie print methodes.
# Schrijf een if statement dat controleert of getal1 een veelvoud is van getal2, andersom of dat beide getallen geen veelvoud zijn van de ander.
# Zet de juiste print methode op de goede plek in je if statement.
# Voorbeeld goede output: 10 is een veelvoud van 5
# ==========================================


# getal_1 = int(input("voer een getal in: "))
# getal_2 = int(input("voer een getal in: "))
# getal3 = 1
# som = int(getal_1 // getal_2)
# som2 =int(getal_2 // getal_1)
# if som > getal3: print(f'{getal_1} is een veelvoud van {getal_2}')
# elif som2 > getal3: print(f'{getal_2} is een veelvoud van {getal_1}')
# else:print("er is geen veelvoud")



# ==========================================
# Opgave 2:
# De basisprijs van een bioscoopkaartje is 12 euro.

# - Kinderen tot 5 jaar zijn gratis
# - kinderen van 5 tot 12 jaar betalen de halve prijs.
# - Personen tussen 13 en 54 jaar moeten de volle prijs betalen
# - vanaf 55 jaar is de toegang weer gratis.

# Maak een programma dat de te betalen prijs afdrukt nadat je de leeftijd hebt ingevoerd als input.
# Voorbeeld output: Voor de leeftijd 10 jaar is de prijs: 6.0
# ==========================================

# leeftijd = int(input("voer je leeftijd in: "))
# prijs = 12
# halveprijs = prijs / 2
# if leeftijd < 5:print('gratis')
# elif leeftijd < 13 and leeftijd > 4: print(halveprijs)
# elif leeftijd > 55:print('gratis')
# else:print(prijs)




# ==========================================
# Opgave 3:
# Schrijf een programma dat 3 gehele getallen (integers) sorteert. De willekeurige inputs worden opgeslagen in de variabelen num1, num2 en num3 (maak deze variabelen met inputs zelf aan). Schrijf een if statement die het laagste getal in num1 stopt, het middelste getal in num2 en het hoogste getal in num3.

# Print de variabelen in de volgorde num1, num2, num3.
# Voorbeeld input: 3 1 2
# Voorbeeld output: 1 2 3
# ==========================================

# Lees een regel met inputs en splits deze op spaties
# invoer1 = int(input("Voer meerdere getallen in, gescheiden door spaties: "))
# invoet2 = int(input("Voer meerdere getallen in, gescheiden door spaties: "))
# invoet3 = int(input("Voer meerdere getallen in, gescheiden door spaties: "))
# invoer5 = int(input("Voer meerdere getallen in, gescheiden door spaties: "))
# invoer4 = int(input("Voer meerdere getallen in, gescheiden door spaties: "))
#
# getallen = sorted(f'{invoer1}{invoet2}{invoet3}{invoer4}{invoer5}')
# print(getallen)





# ==========================================
# Opgave 4:
# Gegeven is de variabele 'totaal' met een waarde van 0.
# Schrijf een programma dat herhaaldelijk een getal als input vraagt.
# Elk getal dat je invoert moet moet worden opgeteld bij het totaal.
# Als je 0 invoert moet het programma stoppen en met een print statement het totaal en het gemiddelde van de getallen afdrukken
# (dus totaal / aantal inputs). Als er geen getallen zijn ingevoerd moet de volgende string worden geprint: "er zijn geen getallen ingevoerd".
#
# Voorbeeld input: 2, 4, 6, 0
# Voorbeeld output: totaal: 12, gemiddelde: 4.0
# ==========================================

totaal = 0
aantal = 0
getal = int(input("getal"))


while getal > 0 :
    totaal += getal
    aantal += 1
    gemiddeld = totaal / aantal
    getal = int(input("getal"))
    print(totaal)
    print(gemiddeld)



# ==========================================
# Opgave 5:
# Schrijf een input die een integer verwacht en stop deze in de variabele “factor”.
# Schrijf daarna een programma dat de tafel van “factor” afdrukt, Print de tafel van 'factor' van 1 tot en met 10.

# Voorbeeld input: 5
# Voorbeeld output:
#   1 x 5 = 5
#   2 x 5 = 10
#   3 x 5 = 15    # enz. tot en met 10
# ==========================================