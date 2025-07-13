def reverse(list1):
    left = 0
    right = len(list1) - 1

    while left < right:
        list1[left], list1[right] = list1[right], list1[left]

        left += 1
        right -= 1

    return list1
list1 = [1,2,3,4,5,6,7,8,9]
result = reverse(list1)
print(result)    