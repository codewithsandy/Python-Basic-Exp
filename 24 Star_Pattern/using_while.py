a = int(input("How many Row you want to print: "))
b = bool(int(input("Type 1 Or 0 ")))

def star(a, b):
    if b == True:
        c = 1
        while c <= a:
            print(c * "*")
            c = c + 1
    else:
        while a > 0:
            print(a * "*")
            a = a - 1

star(a,b)
