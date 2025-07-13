nums = [1,2,3,4,5,6,-1,-2,-3,-4]

pos_count = 0
sum = 0

for num in nums:
    if num > 0:
        pos_count += 1
        sum += num
        
average = sum / pos_count        
        
print(pos_count )    
print(sum)
print("average:",average)
