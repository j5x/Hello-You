Q1 = True
Q5 = False
Q7 = False
Q9 = False
Q11 = False
Q13 = False
Q15 = False
Q17 = False
Q19 = False
while Q1:
    print("Jij bent Ahmad Sawari, je woont in Syrie(Let op gebruik HOOFDLETTERS!)")
    print("Je zit lekker TV te kijken met je familie en ineens hoor je een luide knal.")
    print("Wat ga je doen?")
    print("A: Je gaat met je familie via de achter deur naar buiten")
    print("B: Je gaat naar buiten om te kijken. ")
    print("")
    InputText = input().capitalize()
    if InputText == "A":
        Q1 = False
        Q2 = True
    if InputText == "B":
        Q1 = False
        Q3 = True

while Q3:
    print("Als je buiten bent zie je het Syrische Leger.")
    print("")
    print("Wat ga je doen?")
    print("A: Je laat je familie achter en lijdt het leger af door weg te gaan met de auto.")
    print("B: Je haalt je familie en gaat samen weg.")
    print("")
    InputText = input().capitalize()
    if InputText == "A":
        Q3 = False
        Q5 = True
    if InputText == "B":
        Q7 = True
        Q3 = False

while Q5:
    print("Je bent het leger ontsnapt, en je gaat richting het vliegveld.")
    print("Als je eenmaal aankomt bij het vliegveld besluit je om naar Nederland te gaan.")
    print("Je hebt toestemming om naar Nederland te vluchten en je bent nu onderweg naar het vliegveld.")
    print("Type: A to continue...")
    InputText = input().capitalize()
    if InputText == "A":
        Q5 = False
        Q13 = True

while Q7:
    print("Je rent naar binnen om je familie te halen.")
    print("Jullie rennen via de achter deur naar buiten en lopen om naar de auto.")
    print("In de auto krijgen jullie 2 opties.")
    print("A: Jullie gaan naar het vliegveld.")
    print("B: Jullie gaan naar de grens.")
    print("")
    InputText = input().capitalize()
    if InputText == "A":
        Q7 = False
        Q9 = True
    if InputText == "B":
        Q7 = False
        Q11 = True

while Q9:
    print("Jullie komen aan bij de bij het vliegveld.")
    print("Je gaat naar de balie toe en vraagt of jullie naar Nederland mogen vluchten.")
    print("Jullie hebben toestemming gekregen van Nederland om daar heen te vluchten")
    print("Jullie wachten op het vliegtuig.")
    print("Type: A to continue...")
    InputText = input().capitalize()
    if InputText == "A":
        Q9 = False
        Q15 = True

while Q11:
    print("Jullie komen bij de grens aan")
    print("Jullie worden gestopt door de duane")
    print("De duane ondervraagt jou.")
    print("Na een uur van ondervraging worden jullie naar de gevangenis gebracht.")
    print("Type: A to continue...")
    InputText = input().capitalize()
    if InputText == "A":
        Q11 = False
        Q17 = True

while Q13:
    print("")
    print("Op het vliegveld kom je je familie tegen.")
    print("Ze zijn met iemand mee gelift om bij het vliegveld te komen.")
    print("Jullie krijgen toestemming om naar Nederland te vliegen")
    print("Jullie hebben 2 keuzes")
    print("A: Jullie pakken het 1e vliegtuig.")
    print("B: Jullie pakken het 2e vliegtuig.")
    InputText = input().capitalize()
    if InputText == "A":
        Q13 = False
        Q15 = True
        print("Type: A to continue...")
    InputText = input().capitalize()
    if InputText == "B":
        Q13= False
        Q12 = True
while Q15:
    print("Het vliegtuig is er en jullie gaan aanboord. ")
    print("Eenmaal aanboord zoeken jullie een goede plek uit.")
    print("")
    print("*5 uur later*")
    print("")
    print("Type: A to continue...")
    InputText = input().capitalize()
    if InputText == "A":
        Q15 = False
        Q19 = True

while Q17:
    print("Je krijgt levenslang vanwege land verraad.")
    print("Je familie probeert nog te onstnappen")
    print("Je familie wordt gepakt.")
    print("Type: A to continue")
    InputText = input().capitalize()
    if InputText == "A":
        Q17 = False
        Q21 = True

while Q19:
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
    scriptinput = input()
    if scriptinput == "y" or scriptinput == "Y":
        Q1 = True
        print("[o]*Het script word gerestart*")
        print("")
    elif scriptinput == "n" or scriptinput == "N": 
        print("[o]Thanks for running")
        exit()
    

while Q21:
    print("Je familie is gepakt en jullie worden allemaal gestraft.")
    print("De overheid heeft besloten jullie te excuteren.")
    print("GAME OVER")
    print("Wil je herstarten? Y/N")
    scriptinput = input().capitalize()
    scriptinput = input()
    if scriptinput == "y" or scriptinput == "Y":
        Q1 = True
        print("[o]*Het script word gerestart*")
        print("")
    elif scriptinput == "n" or scriptinput == "N": 
        print("[o]Thanks for running")
        exit()