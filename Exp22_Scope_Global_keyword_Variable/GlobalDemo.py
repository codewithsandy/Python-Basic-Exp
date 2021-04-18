l = 10  # Global variable


def fun1(n):
    l = 5  # Local variable
    #l = l + 90    #We cant make operation on global variable
    print(l)
    print(n, "I have printed")


fun1("This is me")
print(l)
