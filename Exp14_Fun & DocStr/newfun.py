# a = 5
# b = 10


def myfun(a, b):
    """This is function which will calculate average of two number
            Function Doesent work for 3 Number"""                           # This is Doc String // firt line after fun creation
    average = (a + b) / 2
    print(average)
    return average


v = myfun(5, 10)

print("\t", v)

print(myfun.__doc__)
