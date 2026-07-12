def sq(n):
    for i in range(0,n):
        for j in range(0,n):
            print("*", end="")
        
        print()
        
        
t = 5
for i in range(1,t):
    i+=2
    sq(i)        
    print()