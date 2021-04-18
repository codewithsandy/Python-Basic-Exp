def a_first(a):
    return a[1]

a = [[1, 4], [55, 9], [3, 8]]
#a.sort(key= a_first)
a.sort(key=lambda x:x[1])
print(a)