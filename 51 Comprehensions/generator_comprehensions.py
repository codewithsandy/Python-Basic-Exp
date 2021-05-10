
gen1 = (i for i in range(100) if i%5==0)
print(type(gen1))
print(gen1)
print(gen1.__next__())
print(gen1.__next__())
print(gen1.__next__())
print(gen1.__next__())
print(gen1.__next__())

print("\n\n")
for item in gen1:
    print(item)