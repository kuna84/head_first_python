import pprint

people = {}

people['Ford'] = {"Nazwisko": "Ford Perfect",
                  "Płeć": "mężczyzna",
                  "Zawód": "Badacz",
                  "Planeta": "Betelgeza 7"}

people['Artur'] = {"Nazwisko": "Artur Dent",
                  "Płeć": "mężczyzna",
                  "Zawód": "pan kanapka",
                  "Planeta": "Ziemia"}

people['Tricia'] = {"Nazwisko": "Tricia McMillan",
                  "Płeć": "kobieta",
                  "Zawód": "matematyczka",
                  "Planeta": "Ziemia"}

people['robot'] = {"Nazwisko": "Marvin",
                  "Płeć": "n/a",
                  "Zawód": "paranoid android",
                  "Planeta": "n/a"}

print(people)
pprint.pprint(people)
pprint.pprint(people['Artur'])
print(people['Artur'])
