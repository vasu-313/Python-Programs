text = "anudeepdharmavarapu vasulakkoju is a hero"

longest_string = ""

words = text.split()

for word in words:
    if len(word) > len(longest_string):
        longest_string = word

print(longest_string)