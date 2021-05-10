
"""   Use seek to display from pointer in file   """

f = open("sandy.txt")

print(f.readline())
f.seek(15)
print(f.readline())

f.close()