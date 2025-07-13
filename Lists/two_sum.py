def two_sum(nums, target):
    left = 0
    right = len(nums) -1

    while left < right:
        sum = nums[left] + nums[right]

        if sum == target:
            return [left, right]
        elif sum < target:
            left += 1
        else:
            right -= 1
    return -1

nums = [1,2,3,4,5,6]
target = 9
result = two_sum(nums, target)

if result != -1:
    print(result)
else:
    print("Target is not found")    