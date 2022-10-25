import os

doyoulive = 1


def start():
    os.system('cls')
    print("Je leeft in een land waar oorlog is. Je hebt 2 keuzes:")
    keuze1()


def keuze1():
    print(" ")
    print(" a. Je blijft in het land wonen, en gaat verder met je leven.")
    print(" b. Je vlucht uit je land op zoek naar een beter leven.")
    print(" ")

    antwoord_een = input("ik kies keuze ")

    if antwoord_een == "a":
        gevolg_a()
    elif antwoord_een == "b":
        gevolg_b   
     
def gevolg_a():
    print(" ")
    print(" ")
    print(" ")
    print("Je hebt ervoor gekozen om in je land te blijven wonen, desondanks de oorlog die er gaande is.")
    print(" ")
    print("Tijdens een van de gevechten dichtbij jou woonplaats zijn er bommen neergekomen, waaronder eentje in jou straat")
    print("je hebt het helaas niet overleefd.")

def gevolg_b():
    print(" ")
    print(" ")
    print(" ")
    print("Je hebt ervoor gekozen om te vluchten uit je land, En je hebt een voertuig nodig om weg te komen.")
    
def keuze2():
    print(" Welk vervoersmiddel kies jij?")
    print("a. Vrachtwagen")
    print("b. Vliegtuig")
    print("c. Boot")

    antwoord2 = input("Ik kies voertuig ")

    if antwoord2 == "a":
        gevolg2_a()
    elif antwoord2 == "b":
        gevolg2_b()
    elif antwoord2 == "c":
        gevolg2_b()
    elif antwoord2 == "d":
        secret_lvl()

def gevolg2_a():
    print("Je spreekt met een mensensmokkelaar af om je naar Nederland te brengen, daar betaal je een bedrag voor.")

def gevolg2_b():
    print("Je hebt met een piloot afgesproken om te vertrekken vanaf een grasveldje.")
def gevolg2_c():
    print("Je regelt een boot die rond middernacht vertrekt.")
def secret_lvl():
    print("Je hebt een secret route gevonden...")





start()