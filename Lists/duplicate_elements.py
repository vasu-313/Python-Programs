numbers = [1,2,3,4,5,1,3,2,4,]

dici = {}

for num in numbers:
    if num not in dici:
        dici[num] = 1
    else:
        dici[num] += 1

for duplicates in dici:
    if dici[duplicates] >= 2:
        print(duplicates)            