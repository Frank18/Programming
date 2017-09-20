name = input("Enter your name: ")
age = int(input("Geef je leeftijd: "))
paspoort = input("Ben je in bezit van een paspoort: ")
if age > 18 and paspoort == "Ja":
    print("Gefeliciteerd " + name + " je mag stemmen!")
else:
    print("Helaas " + name + " je mag niet stemmen...")