def moveZeroesToEnd(arr):
    
    index = 0
    
    for i in range(len(arr)):
        if arr[i] != 0:
            arr[i], arr[index] = arr[index], arr[i]
            index += 1
    return arr
       
            
arr = [1,2,0,4,0,5,0,3]   
print(moveZeroesToEnd(arr))

# for num in arr:
#     print(num, end = " ")














# def move_zeroes(arr):
#     index = 0
#     for num in range(len(arr)):
#         if arr[num] != 0:
#             arr[index] = arr[num]
#             index += 1
            
    
#     for num in range(index, len(arr)):
#         arr[num] = 0
        
#     return arr    
        
# arr = [0,1,2,0,5,6,70,0,2]        
# print(move_zeroes(arr))   