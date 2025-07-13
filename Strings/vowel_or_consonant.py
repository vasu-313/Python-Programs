char = "!"

char = char.lower()

vowels = "aeiou"

if not char.isalpha():
    print("this is not a alphabet")
elif char in vowels:
    print(f"{char} is a vowel")  
else:
    print(f"{char} is a consonant")     
