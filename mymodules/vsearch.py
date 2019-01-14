def search4vowels(word: str) -> set:
    """Wyświetla samogłoski znalezione w słowie podanym przez użytkownika"""
    vovels = set('aeiou')
    return vovels.intersection(set(word))


def search4letters(phrase: str, letters: str='aeiouy') -> set:
    """Zwraca zbiór liter podanych w zmiennej letters
    znalezionych w zmiennej pharse"""
    return set(letters).intersection(set(phrase))
