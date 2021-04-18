"""
Iterable    -   __iter__()  or  __getitem__()
Iterator    -   __next__()
Iteration   -
"""

def gen(n):
    for i in range(n):
        yield i

#g = gen(89765456432165464988789465456421321564578979874654654613216547897894654)       # dont print number upto n number print location
# print(g)

g = gen(4)
print(g.__next__())
print(g.__next__())
print(g.__next__())
print(g.__next__())
