def linear_search(nums, target):

    for i in range(0, len(nums)):
        if nums[i] == target:
            return i
        elif nums[i] > target:
            return i

    return len(nums)    

nums = [1,3,5,6]
target = 2  # 5 , # 2 , #7   

print(linear_search(nums, target))


        