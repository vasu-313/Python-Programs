words = "boy good a is anudeep"

words = words.split()

# words_reverse = words[::-1]
# print(words_reverse)

reverse_words = ""

for word in words:
    reverse_words = word + " " + reverse_words
print(reverse_words)   
 
