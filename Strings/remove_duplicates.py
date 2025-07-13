# Write a program to extract all unique characters from a string using a set and print them.


def removeDuplicates(text):
    new_set = set()
    ordered = []
    
    for char in text:
        if char not in new_set:
            new_set.add(char)
            ordered.append(char)
        
    return ordered

text = "vvaassu"
result = removeDuplicates(text)    
print("".join(result))








# text = "vvvvvvvvvaasuuuuuuuuuu"

# null_set = set()
# ordered = []

# for char in text:
#     if char not in null_set:
#         null_set.add(char)
#         ordered.append(char)



# print(null_set)        
# print(ordered)        
# print("".join(ordered))        