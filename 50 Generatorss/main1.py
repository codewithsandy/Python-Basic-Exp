def gen(n):
    for i in range(n):
        yield i

s = "Sandy"
for i in s:
    print(i, "\n")

# s = 5     #cant use iter function for integer

iterr = iter(s)
print(iterr.__next__())
print(iterr.__next__())
print(iterr.__next__())
print(iterr.__next__())
print(iterr.__next__())
