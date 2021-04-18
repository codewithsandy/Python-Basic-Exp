"""
==      value equality          two obj have the same value
is      reference equality      two references refer to the same value
"""
a = [7, 5, 2]
b = a
print(a)
print(a == b)
print(b is a)
c = a[:]
print(c is b)
