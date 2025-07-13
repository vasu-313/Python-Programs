def count_digits(num):
    count = 0

    while num != 0:
        num //= 10
        count += 1
    return count
print(count_digits(1234567))    
print(count_digits(-1234567))    





# def count_digits(n):
#     return len(str(abs(n)))

# print(count_digits(123456))
# print(count_digits(-123))
# print(count_digits(0))