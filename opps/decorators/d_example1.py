def decFun(f):
    def innerFun():
        print("welcome")
        f()
    return innerFun

@decFun
def fun():
    print("User")  

fun()      




# def decFun(f):
#     def innerFun():
#         print("Welcome")
#         f()
#     return innerFun

# def fun():
#     print("User")

# fun = decFun(fun)
# fun()
