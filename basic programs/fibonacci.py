# n = int(input("Enter the number of terms: "))

# if n == 0:
#     print(1)
# elif n == 1:
#     print(1, 1)
# else:
#     print(1, 1, end = " ")
#     a = 1
#     b = 1
#     for i in range(2, n + 1):
#         c = a + b
#         print(c, end = " ")
#         a = b
#         b = c


def generate_fibonacci_list(n):
    if n == 0:
        return [1]
    elif n == 1:
        return [1, 1]
    else:
        sequence = [1, 1]
        a, b = 1, 1
        for _ in range(2, n + 1):
            c = a + b
            sequence.append(c)
            a, b = b, c
        return sequence

# Example usage
n = int(input("Enter the number of terms: "))
fib_sequence = generate_fibonacci_list(n)
print(*fib_sequence)




# def fibonacci(num):

#     first = 0
#     second = 1
#     sequence = [first, second]

#     for i in range(3,num+1):
#         next_num = first + second
#         sequence.append(next_num)
#         first = second
#         second = next_num
    
#     return sequence

    
# num = int(input("Enter the number of terms: "))
# print(fibonacci(num))    
    
