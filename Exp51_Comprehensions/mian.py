ls = []
for i in range(100):
    if i % 3 == 0:
        ls.append(i)

print(ls)

#Make list in one line

rs = [i for i in range(100)]
print(rs)


ms = [i for i in range(100) if i%3==0]
print(ms)