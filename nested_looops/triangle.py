   
def print1(n):
    for i in range(0,n):
        for j in range(0,n):
            print("*", end="")
        
        print()
                
def print2(n):
    for i in range(0,n):
        for j in range(0, i+1):
            print("*", end="")
        print()
        
def print3(n):
      for i in range(0,n):
        for j in range(0, i+1):
            print(j, end="")
        print()

def print4(n):
      for i in range(0,n):
        for j in range(0, i+1):
            print(i, end="")
        print()

def print5(n):
    for i in range(0,n+1):
        for j in range(n-i+1):
            print("*", end="")
        print()
        
def print6(n):
    for i in range(0,n+1):
        for j in range(1,n-i+1):
            print(j, end="")
        print()
        
def print7(n):
    for i in range(0,n):
        for j in range(0,n-i-1):
            print(" ", end="")
        for k in range(0, 2*i+1):
            print("*", end="")
        for l in range(0, n-i-1):
            print(" ", end="")
        print()

def print8(n):
    for i in range(0,n):
        for j in range(0,i):
            print(" ", end="")
        for k in range(0, 2*n-(2*i+1)):
            print("*", end="")
        for l in range(0, i):
            print(" ", end="")
        print()

def print9(n):
    for i in range(1,2*n):
        stars = i
        if i > n:
            stars = 2*n - i
        for j in range(1,stars+1):
            print("*", end="")
        print()

def print10(n):
    for i in range(0,n):
        
        if i % 2 == 0:
            start = 1
        else:
            start = 0
        for j in range(0,i+1):
            print(start, end=" ")
            start = 1 - start
        print()


def print11(n):
    space = 2 * (n-1)
    for i in range(1,n+1):
        
        for j in range(1,i+1):
            print(j, end="")
            
        for k in range(0,space):
            print(" ", end="")
            
            
        for l in range(i,0,-1):
            print(l, end="")
        
        print()  
        space -= 2  
        
        
        
        
def print20(n):
    space = 2*n - 2
    for i in range(1, 2*n):
        
        if i > 5: stars = 2*n-i
        else: stars = i
            
        for j in range(0, stars):
            print("*", end="")
                
        for k in range(0, space):
            print(" ", end="")
        
        for l in range(0,stars):
            print("*", end="")
        
        print()
        if i < 5 :  space -= 2 
        else:  space += 2

def print21(n):
    for i in range(0,n):
        for j in range(0,n):
            if i == 0 or j == 0 or i == n-1 or j == n-1:
                print("*", end="")
            else : 
                print(" ", end="")
            
        print()

def main():
    t = int(input("Enter a test case: "))
    
    for i in range(0,t):
       n =  int(input("Enter number: "))
       print21(n)


main()