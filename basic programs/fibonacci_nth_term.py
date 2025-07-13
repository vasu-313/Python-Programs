def fibonacci_nth_term(num):
    if num == 0:
        return 0
    elif num == 1:
        return 1
    else:
        first = 0
        second =1
        for i in range(2, num + 1):
            next_num = first + second
            first = second
            second = next_num
        return second

print(fibonacci_nth_term(5))    




# n = int(input())

# if n == 0:
#     print(1)
# elif n == 1:
#     print(1)
# else:
#     a = 0 
#     b = 1
#     for i in range(2, n+1):
#         c = a + b
#         a = b 
#         b = c
#     print(c)   