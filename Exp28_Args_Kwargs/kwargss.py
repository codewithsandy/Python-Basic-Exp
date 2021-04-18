def funargs1(normal, *args, **kwargs):
    print(normal)
    for item in args:
        print(item)
    print("\nNow I would Like to introduce some of our heroes")
    for key, value in kwargs.items():
        print(f"{key} is a {value}")


list1 = ["Sandy", "Shiv", "Louis", "Vector", "Peter", "John"]
normal = "I am a normal argument "
kw = {"aris": "classco", "Martin": "President", "Kelvin": "Chairman"}   # add item function will be add again again 

funargs1(normal, *list1, **kw)
