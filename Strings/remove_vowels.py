def removeVowels(text):
    vowels = "aeiou"
    result = ""
    for char in text:
        if char.isalpha() and char not in vowels:
                result += char
    return result  

text = "vasu@$#@$64576"
print(removeVowels(text))    





# text = "VaSu"

# vowels = "aeiouAEIOU"
# new = []

# for char in text:
#     if char not in vowels:
#         new.append(char)
# print("".join(new))        