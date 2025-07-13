num = 2024

if (num % 4 == 0 and num % 100 != 0 ) or ( num % 400 == 0 ):
    print(f"{num} is a leap year")
else:
    print(f"{num} is a not leap year")    