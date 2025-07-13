def selection_sort(nums):
    
    for i in range(0, len(nums)):
        min_index = i
        for j in range(i+1, len(nums)):
            if nums[j] < nums[min_index]:
                min_index = j
        temp = nums[i]
        nums[i] = nums[min_index]
        nums[min_index] = temp
    return nums    
      
        
    
nums = [5,6,7,2,4,9] 
print(selection_sort(nums))



# num = [5,6,7,2,4,9]

# for i in range(0, len(num)):
#     min_index = i
#     for j in range(i+1, len(num)):
#         if num[j] < num[min_index]:
#             min_index = j
#     temp = num[i]
#     num[i] = num[min_index]
#     num[min_index] = temp
# print(num)