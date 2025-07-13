
# num = int(input("Enter a number: "))

# f = True

# for i in range(2, num):
#     if num % i == 0:
#         f = False
# if f == True:
#     print(f"{num} is a prime number")
# else:
#     print(f"{num} is not a prime number")


import math

def is_prime(num):
    if num < 2:
        return False
        
    for i in range(2, int(math.sqrt(num))+1):
        if num % i == 0:
            return False
    return True
            
# print(is_prime(2))            
# print(is_prime(3))  
# print(is_prime(4))  
# print(is_prime(5))  


# prime numbers between range

low = int(input("Enter lower range: "))
high = int(input("Enter upper range: "))

prime_list = []

for j in range(low, high+1):
    if is_prime(j):
        # print(j)
        prime_list.append(j)
        

print(f"prime numbers between {low} and {high} are: {prime_list}")    