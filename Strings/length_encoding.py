def length_encoding(text):
    count = 1
    string = []

    for i in range(1, len(text)):
        if text[i] == text[i-1]:
            count+=1
        else:
            string.append(text[i-1] +  str(count))
            count = 1


    string.append(text[-1] + str(count)) 

    return string 

text = "vvaassuu"
result = length_encoding(text)
print("".join(result))
