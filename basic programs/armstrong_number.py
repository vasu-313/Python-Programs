import math
def armstrong(num):
    result = 0
    original_num = num
    
    digit_count = len(str(num))
    
    while num != 0:
        digit = num % 10
        result += math.pow(digit, digit_count)
        num = num // 10
    
    if original_num == result:
        return True
    else:
        return False

# num = int(input("Enter a number: ")) 

# if armstrong(num):
#     print(f"{num} is armstrong number")
# else:
#     print(f"{num} is not armstrong number")


def armstrong_In_Range(start, end):
    armstrong_numbers = []
    for num in range(start, end + 1):
        if armstrong(num):
            # print(num)
            armstrong_numbers.append(num)
    return armstrong_numbers

start = int(input("Enter start of range: "))
end = int(input("Enter end of range: "))

print(armstrong_In_Range(start, end))          
    