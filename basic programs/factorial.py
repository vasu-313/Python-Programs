# num = 5
# value = 1

# for i in range(1, num +1):
#     value *= i

# print(value)    

def factorial(num):
    value = 1
    for i in range(1, num + 1):
        value *= i
    return value

num = int(input("Enter a number: "))
print(factorial(num))    