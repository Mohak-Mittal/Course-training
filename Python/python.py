a =(input("Enter a name: "))
vowels = 0
consonants = 0
for i in a:
    if i in "aeiouAEIOU":
        vowels += 1
    else:
        consonants += 1
print ("Number of vowels:", vowels)
print ("Number of consonants:", consonants)