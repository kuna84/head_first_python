def search4vovels():
    """Wyświetla samogłoski znalezione w słowie podanym przez użytkownika"""
    vovels = set('aeiou')
    word = input('Podaj słowo, w którym należy wyszukać samogłoski: ')
    found = vovels.intersection(set(word))
    for vowel in found:
        print(vowel)
 
