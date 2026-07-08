n = int(input())
candidate = n + 1

while True:
    for i in range(2, candidate):
        if candidate % i == 0:
            break

    else:
        print(candidate)
        break

    candidate += 1
    
        