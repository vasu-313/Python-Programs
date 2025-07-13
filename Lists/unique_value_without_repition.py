numbers = [1,2,3,4,5,6,7,8,2,1,3,4,5,]

dici = {}

for num in numbers:
    if num not in dici:
        dici[num] = 1
    else:
        dici[num] += 1


for unique in dici:
    if dici[unique] == 1:
        print(unique)
        break
        