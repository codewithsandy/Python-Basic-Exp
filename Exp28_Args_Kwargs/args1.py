def funargs(*args):
    for item in args:
        print(item)

list = ["Sandy", "Shiv", "Louis"]
funargs(*list)

def funargs1(normal, *args1):
    print(normal)
    for item in args1:
        print(item)

list1 = ["Sandy", "Shiv", "Louis"]

normal = "I am a normal argument "
funargs(normal, *list1)