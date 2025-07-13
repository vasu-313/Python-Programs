# name = "vasu"
# reverse = name[::-1]
# print(reverse)

 
# name = "vasu"
# reverse_string = "".join(reversed(name))
# print(reverse_string)    


# name = "vasu"
# reverse_string = ""

# i = len(name) - 1  # Start from last index
 
# while i >= 0:
#     reverse_string += name[i]
#     i -= 1
# print(reverse_string)    


text = "usav"
reverse = ""

for char in text:
    reverse = char + reverse
   
print(reverse)    