import random
import os
def clear():
    print('\033c', end='')
def rollDice():
    return random.randint(0,1)
doyoulive = rollDice()
def toekomst():
    print("Je bent in nederland aangekomen en krijgt een baantje bij een bedrjf. Nu werk je nog zwart want je hebt nog geen geldig Nederlands paspoort")
def keuze_boot():
    print("Je hebt een boot geregeld, de kapitein wilt vertrekken rond middernacht.")
    print("\nTijdens je reis over het water naar Nederland kom je de kustwacht tegen en je wordt tegengehouden om je te identificeren. Dit kan je natuurlijk niet.")
    print("Wat doe je?")
    print("\n1. Je blijft op de boot,")
    print("2. Je vlucht in een rubberen bootje,")
    antwoord_boot = input("Ik kies optie: ")
    if antwoord_boot == "1":
        print("Je wordt gevonden en wordt terug meegenomen naar je eigen land.")
    elif antwoord_boot == "2":
        print("Je bent gevlucht met je rubber bootje, Je bent al een paar dagen aan het rond dobberen in het bootje.")
        rollDice()
        if doyoulive > 0:
            print("Het is je gelukt om in Nederland aan te komen met het bootje")
        elif doyoulive == 0:
            print("er was een grote storm, en je hebt het niet overleeft.")
def keuze_vliegtuig():
    print("Je hebt een vliegtuig geregeld die weggaat vanaf een grasveldje.")
    print("mensen zien het vliegtuig en merken dat je weg gaat vluchten.")
    print("Je hebt plek voor 1 persoon meer in het vliegtuig, neem je iemand mee?")
    print("\n1. Ja, ik neem iemand mee,")
    print("2. Nee, ik laat iedereen achter,")
    antwoord_plek = input("\nIk kies optie: ")
    if antwoord_plek == "1":
        print("Je neemt iemand mee, die kies je door te loten.")
        print("Je kan in de pasagiersruimte blijven zitten of je kan je verstoppen in het ruim voor als je land, wat doe je?")
        print("\n1. Je blijf in de pasagiersruimte,")
        print("2. Je verstopt je in het ruim, ")
        antwoord_verstoppen = input("Ik kies optie: ")
        if antwoord_verstoppen == "1":
            print("je hebt ervoor gekozen om je niet te verstoppen en om in het ruim te blijven zitten. Bij het landen hebben ze je vliegtuig gechecked en vonden ze jullie in de pasagiersruimte, Daarom vroegen ze om een paspoort, maar die heb je niet. Ze sturen je terug naar je eigen land.")
        elif antwoord_verstoppen == "2":
            print("Je hebt ervoor gekozen om je in het ruim te verstoppen, en je bent aan het landen. Als je geland bent vergeten ze het ruim te checken en komen jullie veilig in nederland aan.")
            toekomst()
    elif antwoord_plek == "2":
        print("Je neemt niemand mee, en mensen vinden dit niet leuk. ze gaan voor het vliegtuig protesteren zodat je niet weg kan komen. ")
def keuze_vrachtwagen():
    print("Je hebt een vrachtwagen geregeld met een mensensmokkelaar genaamd: Han Solo, om je naar een ander land te krijgen.")
    print("Je komt langs een tolgebouw op de grens. Als je ontdekt word word je weer terug gebracht naar je eigen land. Wat ga je doen?")
    print("\n1. Je blijft zitten in de vrachtwagen,")
    print("2. je gaat uit de vrachtwagen,")
    antwoord_vrachtwagen = input("\nIk kies voor optie: ")
    if antwoord_vrachtwagen == "1":
        print("\nJe hebt ervoor gekozen om in de vrachtwagen te blijven zitten, op de hoop niet gechecked te worden.")
        print("Je komt aan bij de poort waarna ze een inspectie willen doen, ze checken de vrachtwagen en komen jullie tegen.")
        print("Ze brengen je terug naar je eigen land.")
    elif antwoord_vrachtwagen == "2":
        print("\nJe stopt voor het tolgebouw en probeert langs het gebouw te glippen.")
        print("De grenswachters merken dit en rennen achter je aan,")
        print("\n1. je geeft je over aan de grenswachters,")
        print("2. je ziet een bos waar je heen kan rennen.")
        antwoord_grenswachter = input("\nIk kies optie: ")
        if antwoord_grenswachter == "1":
            print("Je hebt je overgegeven, en de grenswachters sturen je terug naar je eigen land.")
        elif antwoord_grenswachter =="2":
            print("Je rent het bos in, waar je de grenswachters kwijt bent geraakt. Later vind je de vrachtwagen weer en reis je mee verder naar Nederland.")
            toekomst()
def voertuig():
    print("Je hebt ervoor gekozen om te vluchten uit je land. Je hebt een voertuig nodig om te vluchten. Welk voertuig kies je?")
    print("\n1. Vrachtwagen,")
    print("2. Vliegtuig,")
    print("3. Boot,")
    antwoord2 = input("ik ga met voertuig nummer: ")
    if antwoord2 == "1":
        print("\n\n")
        keuze_vrachtwagen()
    elif antwoord2 == "2":
        print("\n\n")
        keuze_vliegtuig()
    elif antwoord2 == "3":
        print("\n\n")
        keuze_boot()
def start():
    clear()
    print("Je leeft in een land, waar oorlog is. Je hebt 2 keuzes:")
    print(" ")
    print(" 1. Je blijft in het land wonen, en gaat verder met je leven.")
    print(" 2. Je vlucht uit je land op zoek naar een beter leven.")
    print(" ")
    antwoord1 = input("ik kies ")
    if antwoord1 == "1":
        print("\nJe hebt ervoor gekozen om in je eigen land te blijven. Dit was niet zo'n goede keuze want de oorlog is dichterbij jou huis gekomen, waardoor je het helaas niet hebt overleeft.")
        print(" ")
    elif antwoord1 == "2":
        print("\n\n")
        voertuig()
start()