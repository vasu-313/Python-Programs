# num = 5
# value = 1

# for i in range(1, num +1):
#     value *= i

# print(value)    

# def factorial(num):
#     value = 1
#     for i in range(1, num + 1):
#         value *= i
#     return value

# num = int(input("Enter a number: "))
# print(factorial(num))    


def factorial(num):
    if num < 0:
        return "Factorial not possible for negative numbers"

    if num == 0:
        return 1

    value = 1

    for i in range(1, num + 1):
        value = value * i

    return value


num = int(input("Enter a number: "))
print(factorial(num))
