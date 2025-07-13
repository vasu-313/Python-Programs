# nums = [1,3,5,7,4]
# print(f"Before sorting: {nums}")

# for i in range(len(nums)-1, 0, -1):
#     for j in range(i):
#         if nums[j] > nums[j+1]:
#             temp = nums[j]
#             nums[j] = nums[j+1]
#             nums[j+1] = temp
        
        
# print(f"after sorting: {nums}")
 

#  Descending Order

nums = [1,3,5,6,8]

for i in range(len(nums)-1,0,-1):
    for j in range(i):
        if nums[j] < nums[j+1]:
            temp = nums[j]
            nums[j] = nums[j+1]
            nums[j+1] = temp 
            
print(nums)