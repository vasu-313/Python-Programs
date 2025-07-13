fd = open(r'C:\Users\vasul\OneDrive\Desktop\data.txt', 'r')
data = fd.read()
print(data)
fd.close()