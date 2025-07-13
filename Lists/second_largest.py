def second_largest(arr):
    n = len(arr)
    if n < 2:
        return -1
    
    first = second  = float('-inf')
    for num in arr:
        if num > first:
            second = first
            first = num
        elif num > second and num != first:
            second = num    
    
    if second == float('-inf'):  # No valid
        return -1 
    else:
        return second 
    
arr =  [12, 35, 1, 10, 34, 1] #  [10, 5, 10]  [10, 10, 10]
print(second_largest(arr))


# def second_largest(arr):
#     if len(arr) < 2:
#         return -1
        
#     largest = float('-inf')    
#     second_largest = float('-inf')   
    
#     for num in arr:
#         if num > largest:
#             second_largest = largest
#             largest = num
#         elif num < largest and num > second_largest:
#             second_largest = num
            
#     if second_largest == float('-inf'):
#         return -1 
#     else:
#         return second_largest, largest
        
# arr = [1,2,3,4,5,6,7]  
# sec_largest, largest = second_largest(arr)
# print(f"second_largest: {sec_largest}")
# print(f"largest: {largest}")


















# numbers = [6,2,3,4,7,5,1,8,8,-1,0,-2]

# first = float('-inf')
# second = float('-inf')

# for num in numbers:
#     if num > first:
#         second = first
#         first = num
#     elif num > second and num != first:
#         seocnd = num
# if second == float('-inf'):
#     print(-1)        
# else:
#     print(second)    

    