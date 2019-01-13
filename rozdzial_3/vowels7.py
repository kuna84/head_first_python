vovels = set('aeiou')
word = input("Podaj słowo, w którym należy wyszukać samogłoski: ")
found = vovels.intersection(set(word))
print(found)

for vovel in found:
    print(vovel)
