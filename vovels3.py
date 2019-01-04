vovels = ['a', 'e', 'i', 'o', 'u']
word = input("Podaj słowo, w którym należy wyszukać samogłoski: ")
found = []

for letter in word:
    if letter in vovels:
        if letter not in found:
            found.append(letter)
for vovel in found:
    print(vovel)
