pharse = "Podaj jajko!"
plist = list(pharse)
print(pharse)
print(plist)
unwanted_letters = ['P', 'a', 'j']
    
for letter in unwanted_letters:    
    plist.remove(letter)
    plist.pop()

    
new_pharse = ''.join(plist)
print(plist)
print(new_pharse)
