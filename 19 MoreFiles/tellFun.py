
"""   Use tell to display where pointer in file   """

f = open("sandy.txt")
print(f.tell())
print(f.readline())
print(f.tell())
print(f.readline())
print(f.tell())
f.close()