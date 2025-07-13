# name = input("Enter: ")
# original_name = name

# reverse_string = name[::-1]

# if reverse_string == original_name:
#     print(f"{name} is palindrome")
# else:
#     print(f"{name} is not palindrome")


text = "madam"

reverse = ""

for char in text:
    reverse = char + reverse


if text == reverse:
    print(f"{text} is palindrome")
else:
    print("not palindrome")    