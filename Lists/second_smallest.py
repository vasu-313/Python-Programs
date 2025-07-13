def second_smallest(arr):
    if len(arr) < 2:
        return -1
    
    smallest = float('inf')
    second_smallest = float('inf')

    for num in arr:
        if num < smallest:
            second_smallest = smallest
            smallest = num
        elif num > smallest and num < second_smallest:
            second_smallest = num
         
    if second_smallest == float('inf'):
        return -1
    else:
        return second_smallest, smallest

arr = [1,2,3,4,5,6,7]  
sec_smallest, smallest = second_smallest(arr)
print(f"second_smallest: {sec_smallest}")
print(f"smallest: {smallest}")

    