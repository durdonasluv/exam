text = input("Enter the text: ")
vowels = 'aeiouyAEIOUY'
puncts = "!@#$%^&*()_-=+[]{}|\\:;\"'<>,./?`~ "
vowel = 0
consonant = 0
for i in text:
    if i in vowels:
        vowel +=1
    elif i not in puncts and not i.isdigit():
        consonant += 1
print(f"vowels: {vowel}\n cons: {consonant}")