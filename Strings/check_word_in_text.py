text = "anudeep is good boy"
words = text.split()
sub = "vasu"
found = False

for word in words:
    if word == sub:
        print("yes")
        found = True
        break

if not found :
    print("No")