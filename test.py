# age = 63
# if age > 62:
#     print("You can get Social Security Benefits")

# report = "large bonuses"
# if "large bonuses" in report:
#     print("Vacation time!")

# hits = 12
# shield = 0
# if hits > 10 and shield == 0:
#     print("You're dead")

# name = input("Enter your name: ")
# age = int(input("Enter your age: "))
# if age < 18:
#     print(name + ", you can't vote.")
# else:
#     print(name + ", you can vote.")

# name = input("Enter a word: ")
# print("The word spelled out: ")
# for char in name:
#     print(char)

# for i in range(11):
#     print(i, end=" ")
# print()
# for i in range(1, 10):
#     print(i, end=" ")
# print()
# for i in range(0, 9, 2):
#     print(i, end=" ")
# print()
# for i in range(1, 10, 2):
#     print(i, end=" ")
# print()
# for i in range(20, 61, 10):
#     print(i, end=" ")

score = int(input("Geef je score: "))
if score > 15:
    print("Gefeliciteerd!")
print("Met een score van",score,"ben je geslaagd!")

name = input("Enter your name: ")
age = int(input("Geef je leeftijd: "))
paspoort = input("Ben je in bezit van een paspoort: ")
if age > 18 and paspoort == "Ja":
    print("Gefeliciteerd " + name + " je mag stemmen!")
else:
    print("Helaas " + name + " je mag niet stemmen...")

# 2.1
letters = ('A', 'C', 'B', 'B', 'C', 'A', 'C', 'C', 'B')
print(sorted(letters))
print(sorted(str(letters.count('A'))), (sorted(str(letters.count('B')))), (sorted(str(letters.count('C')))))

# 2.2
cijferICOR = 8
cijferPROG = 7
cijferCSN = 6
gemiddelde = cijferICOR + cijferPROG + cijferCSN
beloning = gemiddelde // 3
print('Gefeliciteerd uw cijfers met een gemiddelde van',gemiddelde // 3,'leveren uw',beloning * 30,'euro op!')

# sarah = 14
# mark = 10
# fatima = 5
# test = sarah + mark + fatima
# sum(test)

# 2.3
# Gelukt

# 2.4
uren = input('Vul hier je aantal gewerkte uren in: ')
uurloon = input('Vul hier in wat je per uur verdient: ')
salaris = uren * uurloon
print(uren + ' uur werken levert ' + salaris + ' euro op!')

# def hello(name):
#     print('welcome '+ name +' to the world of phyton')
# hello(input('Vul hier uw naam in: '))

# def rng(lijstje):
#     diff = max(lijstje) - min(lijstje)
#     print(diff)
# rng(eval(input('Geef hier je getallen in: ')))

# lijst = [1, 2, 3]
# def swapFS(lijst):
#     if len(lijst) > 1:
#         lijst[0], lijst[1] = lijst[1], lijst[0]
# print(lijst)
# swapFS(lijst)
# print(lijst)

# s = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h']
# s[:4]
# s[3:6]
# s[3]
# s[5:7]
# s[3:]
# s[5:]

# events.count('9/14')
# events.find('9/14')
# events.find('9/15')
# events[13:40]
# list = events[13:40].strip().split('\n')


for i in range(1, 5):
    print(i, i**2, 2**i)






