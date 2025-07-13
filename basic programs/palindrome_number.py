# num = 121
# reverse = 0 
# original_num = num 

# while num > 0:
#     digit = num % 10
#     reverse = reverse * 10 + digit
#     num = num // 10 


# if reverse == original_num:
#     print("The number is a Palindrome")

# else:
#     print("The number is not a palindrome")    


def is_palindrome(num):
    reverse = 0
    original_num = num

    while num > 0:
        digit = num % 10
        reverse = reverse * 10 + digit
        num = num // 10
    # return reverse == original_num    
    if reverse == original_num:
        return "The number is palindrome"
    else:
        return "The number is not palindrome"    
    
print(is_palindrome(121))    
print(is_palindrome(12345))    