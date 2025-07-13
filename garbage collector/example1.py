import sys

x = 1000
print("Initial refcount:", sys.getrefcount(x))  # Expect 2 (x + temporary)

a = x
print("After a = x:", sys.getrefcount(x))       # Expect 3

b = x
print("After b = x:", sys.getrefcount(x))       # Expect 4

del a
print("After del a:", sys.getrefcount(x))       # Expect 3

del b
print("After del b:", sys.getrefcount(x))       # Expect 2
