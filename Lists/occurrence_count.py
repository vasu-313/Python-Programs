numbers = [1,2,3,4,5,6,1,2,3]

dici = {}

for num in numbers:
    if num not in dici:
        dici[num] = 1
    else:
        dici[num] += 1

print(dici)

for num in dici:
    if dici[num] == 1:
        print(num)
        break

