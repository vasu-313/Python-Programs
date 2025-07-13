text = "vasu is a very bad boy"
# print(text.title()) 

words = text.split()

for word in words:
    new_text = word[0].upper() + word[1:]
    print(new_text, end=" ")

   