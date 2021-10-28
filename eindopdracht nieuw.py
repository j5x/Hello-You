Q1 = True

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
    print("A: Je laat je familie achter en lijdt het leger af door weg te gaan met de auto")
    print("B: Je haalt je familie")
    print("")
    InputText = input().capitalize()
    if InputText == "A":
        Q5 = True
        Q3 = False
    if InputText == "B":
        Q7 = True
        Q3 = False
while Q5:
    print("Je bent het leger ontsnapt, en je gaat richting het vliegveld.")
    print("Als je eenmaal aankomt bij het vliegveld besluit je om naar Nederland te gaan.")
    print("Je hebt toestemming om naar Nederland te vluchten en je bent nu onderweg.")
    print("Type: A to continue")
    InputText = input().capitalize()
    if InputText == "A":
        Q5 = False
        Q13 = True
while Q7:
    print("Je rent naar binnen om je familie te halen.")
    print("Jullie rennen via de achter deur naar buiten en lopen om naar de auto.")
    print("In de auto krijgen jullie 2 opties.")
    print("A: ")