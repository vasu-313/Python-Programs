def linear_search(l,target):
    for i in range(0, len(l)):
        if l[i] == target:
            return i
    return -1
    
l = [1,2,3,3,4,5]
target = 3  

result = linear_search(l, target)

if result != -1:
    print(result)
else:
    print("not found")