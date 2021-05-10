f1 = open("Sandy.txt")

try:
    f = open("my.txt")
except Exception as e:
    print(e)
finally:
    print("Run this anyway")
    f.close()
    f1.close()

print("Important Stuff")