a = 12
b = 18

small = min(a, b)

for i in range(1, small+1):
    if (a % i == 0 and b % i == 0):
        gcd = i
        
print("GCD", gcd)

import math

gcd1 = math.gcd(a,b)

print(gcd1)