def find_minimum(a, b):
   
    result = []
    
    result.append(a+b)
    
    result.append(a-b)
    
    result.append(a*b)
    try:
        result.append(a/b)
    except ZeroDivisionError:
        pass
    
    return min(result)

print(find_minimum(10,0))