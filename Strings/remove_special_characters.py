def removeSpecialChar(text):
    new  = ""
    for char in text:
        if char.isalnum():
            new += char
    return new
    
    
text = "vasu@$#@$64576"
print(removeSpecialChar(text))









# text = "vasu2@@31984"
# text2 = []

# for char in text:
#     if char.isalnum():
#         text2.append(char)
        
# # print(text2) 
# print("".join(text2))