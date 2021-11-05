import os
play = True

Q = 1

while play:
    while Q == 1:
        print("Jij bent Ahmad Sawari, je woont in Syrie(Let op gebruik HOOFDLETTERS!)")
        print("Je zit lekker TV te kijken met je familie en ineens hoor je een luide knal.")
        print("Wat ga je doen?")
        print("A: Je gaat met je familie via de achter deur naar buiten")
        print("B: Je gaat naar buiten om te kijken. ")
        print("")
        InputText = input().capitalize()
        if InputText == "A":
            Q = 2
            os.system('cls')
        elif InputText == "B":
            Q = 3
            os.system('cls')

    while Q == 3:
        print("Als je buiten bent zie je het Syrische Leger.")
        print("")
        print("Wat ga je doen?")
        print("A: Je laat je familie achter en lijdt het leger af door weg te gaan met de auto.")
        print("B: Je haalt je familie en gaat samen weg.")
        print("")
        InputText = input().capitalize()
        if InputText == "A":
            Q = 5
            os.system('cls')
        if InputText == "B":
            Q = 7
            os.system('cls')

    while Q == 5:
        print("Je bent het leger ontsnapt, en je gaat richting het vliegveld.")
        print("Als je eenmaal aankomt bij het vliegveld besluit je om naar Nederland te gaan.")
        print("Je hebt toestemming om naar Nederland te vluchten en je bent nu onderweg naar het vliegveld.")
        print("Type: A to continue...")
        InputText = input().capitalize()
        if InputText == "A":
            Q = 13
            os.system('cls')

    while Q == 7:
        print("Je rent naar binnen om je familie te halen.")
        print("Jullie rennen via de achter deur naar buiten en lopen om naar de auto.")
        print("In de auto krijgen jullie 2 opties.")
        print("A: Jullie gaan naar het vliegveld.")
        print("B: Jullie gaan naar de grens.")
        print("")
        InputText = input().capitalize()
        if InputText == "A":
            Q = 7
            os.system('cls')
        if InputText == "B":
            Q = 11
            os.system('cls')

    while Q == 9:
        print("Jullie komen aan bij de bij het vliegveld.")
        print("Je gaat naar de balie toe en vraagt of jullie naar Nederland mogen vluchten.")
        print("Jullie hebben toestemming gekregen van Nederland om daar heen te vluchten")
        print("Jullie wachten op het vliegtuig.")
        print("Type: A to continue...")
        InputText = input().capitalize()
        if InputText == "A":
            Q = 15
            os.system('cls')

    while Q == 11:
        print("Jullie komen bij de grens aan")
        print("Jullie worden gestopt door de duane")
        print("De duane ondervraagt jou.")
        print("Na een uur van ondervraging worden jullie naar de gevangenis gebracht.")
        print("Type: A to continue...")
        InputText = input().capitalize()
        if InputText == "A":
            Q = 17
            os.system('cls')

    while Q == 13:
        print("")
        print("Op het vliegveld kom je je familie tegen.")
        print("Ze zijn met iemand mee gelift om bij het vliegveld te komen.")
        print("Jullie krijgen toestemming om naar Nederland te vliegen")
        print("Jullie hebben 2 keuzes")
        print("A: Jullie pakken het 1e vliegtuig.")
        print("B: Jullie pakken het 2e vliegtuig.")
        InputText = input().capitalize()
        if InputText == "A":
            Q = 15
            os.system('cls')
            print("Type: A to continue...")
        InputText = input().capitalize()
        if InputText == "B":
            Q = 12
            os.system('cls')
    while Q== 15:
        print("Het vliegtuig is er en jullie gaan aanboord. ")
        print("Eenmaal aanboord zoeken jullie een goede plek uit.")
        print("")
        print("*5 uur later*")
        print("")
        print("Type: A to continue...")
        InputText = input().capitalize()
        if InputText == "A":
            Q = 19

    while Q == 17:
        print("Je krijgt levenslang vanwege land verraad.")
        print("Je familie probeert nog te onstnappen")
        print("Je familie wordt gepakt.")
        print("Type: A to continue")
        InputText = input().capitalize()
        if InputText == "A":
            Q = 21
            os.system('cls')

    while Q == 19:
        print("")
        print("Hij heeft een bomgordel om zich heen")
        print("Iedereen aan boord probeerd hem over te halen om het niet te doen.")
        print("Hij luisterd niet en laat zijn vest exploderen.")
        print("Iedereen aanboord is dood")
        print("")
        print("GAME OVER")
        print("Wil jij dit script herstarten? Y/N")
        print("")
        scriptinput = input().capitalize()
        if scriptinput == "y" or scriptinput == "Y":
            Q = 1
            print("[o]*Het script word gerestart*")
            print("")
            os.system('cls')
        elif scriptinput == "n" or scriptinput == "N": 
            print("[o]Thanks for running")
            os.system('cls')
            exit()
        
    while Q == 21:
        print("Je familie is gepakt en jullie worden allemaal gestraft.")
        print("De overheid heeft besloten jullie te excuteren.")
        print("GAME OVER")
        print("Wil je herstarten? Y/N")
        scriptinput = input().capitalize()
        if scriptinput == "y" or scriptinput == "Y":
            Q = 1
            print("[o]*Het script word gerestart*")
            print("")
            os.system('cls')
        if scriptinput == "n" or scriptinput == "N": 
            print("[o]Thanks for running")
            os.system('cls')
            exit()

    while Q == 2:
        print("Jullie horen allemaal schoten.")
        print("Het is het Syrische leger.")
        print("Jullie gaan naar de auto.")
        print("Waar gaan jullie heen?")
        print("A: de haven")
        print("B: het vliegveld")
        InputText = input().capitalize()
        if InputText == "A":
            Q = 4
            os.system('cls')
        if InputText == "B":
            Q = 6
            os.system('cls')
    while Q == 4:
        print("Jullie komen aan bij de haven.")
        print("Jullie komen een oude vriend tegen.")
        print("Jullie praten even met hem en vertellen hem wat er is gebeurd.")
        print("Hij vindt het erg wat er is gebeurd.")
        print("Hij bied aan om jullie me te laten gaan als hij vracht weg brengt.")
        print("Waar gaan jullie eraf? zegt hij.")
        print("Waar ga je heen?")
        print("A: Griekeland")
        print("B: Nederland")
        InputText = input().capitalize()
        if InputText == "A":
            Q = 8
            os.system('cls')
        if InputText == "B":
            Q = 10
            os.system('cls')

    while Q == 6:
        print("Jullie komen aan op het vliegveld")
        print("Jullie gaan naar de balie en alleen jij krijgt toestemming van Nederland om er heen te vluchten.")
        print("Je gaat in discussie met de man achter de balie.")
        print("Na een half uur discussie voeren is het geregeld dat je familie mee kan.")
        print("Type: A to continue... ")
        InputText = input().capitalize()
        if InputText == "A":
            Q = 12
            os.system('cls')

    while Q == 8:
        print("Jullie zijn onderweg naar Griekeland.")
        print("Onderweg vraagt hij of je zeker weten naar Griekeland wilt.")
        print("Hij zegt dat Nederland een.")
        print("Je gaat met je familie bespreken of Nederland een goede keuze is.")
        print("Je familie laat jou kiezen.")
        print("Wat kies je?")
        print("A: Griekeland")
        print("B: Nederland")
        InputText = input().capitalize()
        if InputText == "A":
            Q = 14
            os.system('cls')
        if InputText == "B": 
            Q = 16
            os.system('cls')

    while Q == 10:
        print("")
        print("Nederland dus? oke daar zijn we over 2 weken.")
        print("Je geniet van de rust op het schip en de tijd vliegt bij.")
        print("Type: A to continue...")
        InputText = input().capitalize()
        if InputText == "A":
            Q = 16
            os.system('cls')
    
    while Q == 12:
        print("jullie hebben de eerste vlucht gemist")
        print("In Syrie gaan niet veel vluchten, elke 2 weken gaat er een nieuwe vlucht.")
        print("Dus jullie wachten")
        print("")
        print("*2 weken later*")
        print("")
        print("Jullie vlucht is er en na 5 uur zijn jullie geland in Nederland")
        print("Type: A to continue...")
        InputText = input().capitalize()
        if InputText == "A":
            Q = 20
            os.system('cls')
    while Q == 14:
        print("Na anderhalve week kom je aan in Griekeland.")
        print("De Griekse Duane checked de boot en vind jou en je familie.")
        print("Je probeert hun over te halen om te geloven dat jullie bemanning van het schip zijn") 
        print("Type: A to continue...")
        InputText = input().capitalize()
        if InputText == "A":
            Q == 18
            os.system('cls')

    while Q == 16:
        print("Halverwege de reis op schip is ")
        print("Komt er een marine schip langs.")
        print("Jullie verstoppen je, ze checken het schip en vinden niks.")
        print("Dat was heel lucky.")
        print("Jullie komen aan in Nederland.")
        print("Type: A to continue...")
        InputText = input().capitalize()
        os.system('cls')
        if InputText == "A":
            Q = 20
    
    while Q == 18:
        print("De mannen van de Duane nemen jou mee naar degevangenis.")
        print("De rechter die besluit jou en je vrouw 30 jaar in de cel te geven")
        print("Jouw dochter en zoon die worden bij een pleeggezin geplaats.")
        print("GAME OVER")
        print("Wil jij dit script herstarten? Y/N")
        print("")
        scriptinput = input().capitalize()
        if scriptinput == "y" or scriptinput == "Y":
            Q = 1
            print("[o]*Het script word gerestart*")
            print("")
            os.system('cls')
        elif scriptinput == "n" or scriptinput == "N": 
            print("[o]Thanks for running")
            os.system('cls')
            exit()
    while Q == 20:
        print("Jullie regelen een verblijfsvergunning bij de overheid.")
        print("")
        print("*5 jaar later* ")
        print("")
        print("Je had een eigen bedrijf opgericht en is nu wereldwijd bekent.")
        print("Je woont in Amsterdam en hebt een luxe huis.")
        print("Je bent succesvol geworden. ")
        print("Game end.")
        print("")
        print("Wil jij dit script herstarten? Y/N")
        print("")
        scriptinput = input().capitalize()
        if scriptinput == "y" or scriptinput == "Y":
            Q = 1
            print("[o]*Het script word gerestart*")
            print("")
            os.system('cls')
        elif scriptinput == "n" or scriptinput == "N": 
            print("[o]Thanks for running")
            os.system('cls')
            exit()