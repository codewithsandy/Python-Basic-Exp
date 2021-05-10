
f = open("sandy.txt", "r")
content = f.read()
print(content)
f.close()

f = open("sandy.txt", "r")
content = f.read(3)
print(content)
f.close()

print("\n\t")

f = open("sandy.txt", "r")
content = f.read(5656565)
print("1", content)
content = f.read(5656565)
print("2", content)
f.close()

"""
Print Line By Line
content means characterwise
f means linewise in file
"""

f = open("sandy.txt", "rt")
for line in f:
    print("\t", line, end="")
f.close()


f = open("sandy.txt", "r")
print(f.readline())
print(f.readline())
print(content)
f.close()


f = open("sandy.txt", "r")
print(f.readlines())
print(content)
f.close()