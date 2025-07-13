# Write a program that takes a string as input and finds the first character that appears only once using a dictionary.


def nonRepeatingChar(text):
    dici = {}

    for char in text:
        if char not in dici:
            dici[char] = 1
        else:
            dici[char] += 1
            
    for key in dici:
        if dici[key] == 1:
            return key
            
    return '$'  # if no unique character is found      

text = "vvaassuu"
    
print(nonRepeatingChar(text))  