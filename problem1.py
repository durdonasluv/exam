def count_vowels_and_consonants(text: str):
    count_vowels = 0
    count_cons = 0
    vowels = 'aeiou'
    for i in text:
        if i.lower() in vowels:
            count_vowels += 1
        elif i.isalpha():
            count_cons += 1
    return {
        "vowels": count_vowels,
        "consonants": count_cons
    }
    
    
text = input("Enter the text: ")
print(count_vowels_and_consonants(text))