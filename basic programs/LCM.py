a = 4 
b = 6

res = max(a,b)

while(res <= a*b):
    if(res % a == 0 and res % b == 0):
        break
    
    res += 1
    
print("LCM is", res)

import math

gcd = math.gcd(a,b)
lcm = (a*b) // gcd

print("GCD is", gcd)
print("LCM is", lcm)