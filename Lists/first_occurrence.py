# def firstOcc(l, x):
    
#     for i in range(len(l)):
#         if l[i] == x:
#             return i
#     return -1    


# l = [1, 10, 10, 10, 20, 20, 40]
# x = 20

# print(firstOcc(l, x))

def firstOcc(l, x):
    low = 0
    high = len(l) - 1

    while low <= high:
        mid = (low + high) // 2

        if l[mid] < x:
            low = mid + 1
        elif l[mid] > x:
            high = mid - 1

        else:
            if mid == 0 or l[mid - 1] != l[mid]:
                return mid
            else:
                high = mid - 1   

    return -1 

l = [5, 10, 10, 20, 20]
x = 10

print(firstOcc(l, x))



