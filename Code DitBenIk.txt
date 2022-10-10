from datetime import datetime

print("Hello you! Wie ben jij?")
print(" ")
naam = input("ik ben ")
print(" ")
print(f"Hallo {naam}!")
print(f"In welk jaar ben jij geboren?")
print(" ")
jaar=input("In het jaar ")
print(" ")
calc = datetime.now().year - int(jaar)
jaartijd = datetime.now().year 
print(f"het is {jaartijd} dus jij bent {calc} jaar oud.( het is alleen per jaar, niet met maanden en dagen :)" )
print(" ")

print("Ik ben een nieuwkomer op het Mediacollege Amsterdam. Om mij beter te leren kennen stel ik een aantal vragen over mij.")
print(" ")
print("Beantwoord deze vraag met: A, B of C.")
print(" ")
print(" ")
print("Vraag 1")
print(" ")
print("Hoe oud ben ik?")
print("A. 15")
print("B. 16")
print("C. 17")
antwoord = input(": ")
if antwoord == "A":
    print("Fout, Probeer opnieuw!")
if antwoord == "B":
    print("Goed, Lekker bezig!")
if antwoord == "C":
    print("Fout, Probeer opnieuw!")
print(" ")

print("Vraag 2")
print(" ")
print("Waar woon ik??")
print("A. Amsterdam")
print("B. Haarlem")
print("C. Hoofddorp")
antwoord = input(": ")
if antwoord == "A":
    print("Fout, Probeer opnieuw!")
if antwoord == "B":
    print("Fout, Probeer opnieuw!")
if antwoord == "C":
    print("Goed, Lekker bezig!")
print(" ")

print("Vraag 3")
print(" ")
print("Wat is mijn favo game?")
print("A. Apex")
print("B. Minecraft")
print("C. Valorant")
antwoord = input(": ")
if antwoord == "A":
    print("Goed, Lekker bezig!")
if antwoord == "B":
    print("Goed, Lekker bezig!")
if antwoord == "C":
    print("Goed, Lekker bezig!")
print(" ")

    
