def is_prime(x):
    if x < 2:
        return False
    for i in range(2, x):
        if x % i == 0:
            return False
    return True
            
def printPrimeFactorization(n):
    pfact = []
    for i in range(2, n+1):
        if is_prime(i):
            while n % i == 0:
                pfact.append(i)
                n = n // i
    return pfact 
    
n = 100
result = printPrimeFactorization(n)
print(" ".join(map(str, result)))