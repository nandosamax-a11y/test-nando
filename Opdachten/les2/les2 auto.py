print("Welkom!\n je gaat op reis! \nKies je richting: links, rechts of rechtdoor.")
rechts_teller = 0
links_teller = 0
rechtdoor_teller = 0

while True:
    keuze = input("Welke richting kies je? ")

    if keuze not in ["links", "rechts", "rechtdoor"]:
        print("Ongeldige keuze. Kies: links, rechts of rechtdoor.")

    if keuze == "rechts":
        rechts_teller += 1
        if rechts_teller == 4:
            print("Je bent terug op het begin!")
            break
        if rechts_teller == 3 and rechtdoor_teller == 1:
            print("je bent verdwaalt!!!")
            break
        if links_teller == 2 and rechtdoor_teller == 1 and rechts_teller == 1:
            print(" je wint !!Je bent aangekomen in Spanje!!! \n geniet van je vakantie!!!!!")
            break
        if links_teller == 2 and rechtdoor_teller >= 2:
            print("je hebt een ongeluk gehad.. \n je bent de sloot in gereden")
            break
        else:
            print("Je ging rechts. ")

    if keuze == "links":
        links_teller += 1
        if links_teller == 4:
            print("Je bent terug op het begin!")
            break
        if links_teller == 2 and rechtdoor_teller == 1 and rechts_teller == 1:
            print(" je wint !!Je bent aangekomen in Spanje!!! \n geniet van je vakantie!!!!!")
            break
        if links_teller == 2 and rechtdoor_teller >= 2:
            print("je hebt een ongeluk gehad.. \n je bent de sloot in gereden")
            break
        else:
            print("Je ging links. ")

    if keuze == "rechtdoor":
        rechtdoor_teller += 1
        if rechtdoor_teller == 4:
            print("je komt aan in Duitsland..... \n probeer het nog een keer en meen eens een afslag")
            break
        if rechts_teller == 3 and rechtdoor_teller == 1:
            print("je bent verdwaalt!!!")
            break
        if links_teller == 2 and rechtdoor_teller == 1 and rechts_teller == 1:
            print(" je wint !!Je bent aangekomen in Spanje!!! \n geniet van je vakantie!!!!!")
            break
        else:
            print("je ging rechtdoor")
# test