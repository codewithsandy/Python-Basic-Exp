s = set()

s.add(1)
s.add(1)
s.add(2)
s1 = s.union({1, 2, 3, 4})
print(s, s1)

s2 = s.intersection({1, 2, 3, 4})
print(s, s2)
