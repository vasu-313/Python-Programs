# approach for average 1

# nums = [1,2,3,4,5,6]
# sum = 0


# for num in nums:
#     sum = sum + num
    
# average = sum / len(nums)
# print("Average:",average)  




# list1 = [1,2,3,4,5,6,7,8,9]

# if len(list1) % 2 == 1:
#     median_index = len(list1) // 2
#     median = list1[median_index]
# else:
#     mid1 = len(list1) // 2
#     mid2 = mid1 - 1
#     median = (list1[mid1] + list1[mid2] ) / 2
    
# print("median:",median)    

def median(arr):
    arr.sort()
    n = len(arr)
    
    if n % 2 == 1:
        median = n // 2
        return arr[median] 
        
    elif n % 2 == 0:
        mid1 = (n // 2) - 1
        mid2 = n // 2 
        median = (arr[mid1] + arr[mid2]) / 2
        return median
       
arr = [1,2,3,4,5,6,7,8,9,10,11,12,13,14]        
print(median(arr))     











# approach for average 2

# def avg(arr):
    
#     elements = len(arr)
#     sum_of_elements = 0
    
#     for num in arr:
#         sum_of_elements += num
     
#     result = sum_of_elements // elements 
#     return result

# arr = [1,2,3,4,5]    
# print(avg(arr))  



# approach for average 3

# def avg(arr):
#     if not arr:
#         return 0
#     return sum(arr) / len(arr)    
    
# arr = [1,2,3,4,5]
# print(avg(arr))


            
   


