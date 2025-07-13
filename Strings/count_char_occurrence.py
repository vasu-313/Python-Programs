# Write a program to count how many times each character appears in a given string using a dictionary.

text = "vvaassu"

def charOccurrence(text):
    dici = {}

    for char in text:
        if char not in dici:
            dici[char] = 1
        else:
            dici[char] += 1
            
    result = ""        
    for key in dici:
        result += f"{key} = {dici[key]}\n"
    return result    
   
            
print(charOccurrence(text))   




# text = "vaaasu"

# dici = {}

# for i in text:
#     if i not in dici:
#         dici[i] = 1
#     else:
#         dici[i] += 1

# print(dici)

# for i in dici:
#     print(i, "=", dici[i])


