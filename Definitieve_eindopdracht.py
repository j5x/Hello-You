# reminder alle oneven S getallen (S1 tm S21)zijn geconnect en alle even (S1 tm S20) zijn geconnect
S1 = False
S2 = False
S3 = False
S4 = False
S5 = False
S6 = False
S7 = False
S8 = False
S9 = False
S10 = False
S11 = False
S12 = False
S13 = False
S14 = False
S15 = False
S16 = False
S17 = False
S18 = False
S19 = False
S20 = False
S21 = False
S1 = True
while S1:
    print("Jij bent Ahmad Sawari, een vluchteling uit Syrië, jij moet de goede keuzes zien te maken om te overleven.(Let op, GEBRUIK HOOFDLETTERS)")
    print("")
    print("Je bent in je huis met je familie, lekker TV aan het kijken en ineens hoor je een luide knal.")
    print("Wat ga je doen?")
    print("")
    print("A: Je gaat naar buiten kijken wat er aan de hand is")
    print("B: je blijft binnen veilig bij je familie.")
    InputText = input()
    InputText.capitalize()
    
    if InputText == "A":
        print("")
        print("Je ziet het Syrische leger met tanks en explosieve wapens, je rent naar binnen om tegen je familie te zeggen dat ze in de bombshelter moeten gaan zitten.")
        print("")
        S1 = False
        S2 = True
    elif InputText == "B":
        print("Het Syrische leger komt bij je huis naar binnen en schiet jou en je familie dood.")
        print("")
        print("Wil je herstarten? Y/N")
        InputText = input().capitalize()
        if InputText == "Y":
            S1 = True
        elif InputText == "N":
            exit()

while S2:
   
    print("Je bent net optijd in de bombshelter, jullie wachten een paar uur tot dat het geluid stopt,")
    print("Jij en je familie zijn veilig voor nu, jullie gaan naar buiten om te kijken wat er nog over is. Bijna alles is weggevaagd.")
    print("Jullie gaan een hoek om en zien een man met een auto ernaast.")
    print("Wat gaan je doen?")
    print("")
    print("A: Terug naar huis en een plan van aanpak bedenken.")
    print("B: Naar de man toe lopen en vragen wat er is gebeurd.")
    print("")
    InputText = input().capitalize()
    if InputText == "A":
        print("Jullie gaan terug naar huis en bedenken wat jullie nu verder gaan doen.")
        print("Na een uur overleggen zijn jullie tot het besluit gekomen om te vluchten uit het land.")
        print("En daarna pakken jullie de auto en gaan meteen weg")
        print("")
        S2 = False
        S3 = True
    elif InputText == "B":
        print("Jullie lopen naar de man toe en vragen aan hem wat er allemaal is gebeurd.")
        print("De man legt in kort uit wat er allemaal is gebeurd.")
        print("Na de man zijn verhaal zegt hij dat hij onderweg was naar het vliegveld om te vluchten, hij vraagt of jullie mee willen.")
        print("Jullie zeggen ja en gaan meteen vertrekken naar het vliegveld")
        print("")
        S2 = False
        S4 = True

while S3:
    print("")
    print("Terwijl jullie onderweg zijn houdt de douane jullie tegen en arresteert jou en laat je familie buiten wachten terwijl ze jou ondervragen.")
    print("")
    print("De douane agent heeft een vragen voor je:")
    print("")
    print("[D] Oke, hierkomt vraag 1, waarom ben jij aan het vluchten?")
    print("A: Het is hier gevaarlijk wij kunnen hier niet blijven.")
    print("B: Ik en mijn familie willen op vakantie gaan naar het buitenland")
    InputText = input().capitalize()
    if InputText == "A":
        print("[D] DIT IS LAND VERRAAD! JULLIE GAAN DE GEVANGENIS IN!")
        print("Jullie zitten in de gevangenis en wachten de doodstraf af.")
        print("")
        print("Wil je herstarten? Y/N")
        InputText = input().capitalize()
        if InputText == "Y":
            S3 = True
        elif InputText == "N":
            exit()
    if InputText == "B":
        print("[D] Oke, aangezien jij geen tiener meer bent, moet je het leger in, maar als je mij een flinke som betaald dan zie ik het door de vingers, ")
        print("[D] Als jij mij 1 miljoen SYP(Syrian Pound)(800$) betaald dan laat ik je gaan.")
        print("A: Je geeft hem het geld en jullie gaan door met jullie reis")
        print("B: Je geeft hem niks.")
        if InputText == "A":
            print("")
            S3 = False
        if InputText == "B":
            print("[D] Dus je wilt niet betalen, Oke het leger in dan maar.")
            print("Je gaat het leger in voor een lange periode en je wordt dood geschoten in oorlog.")
            print("Wil je herstarten? Y/N")
            if InputText == "Y":
                    S3 = True
            elif InputText == "N":
                    exit()