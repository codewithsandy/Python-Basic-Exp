"""Nested Function"""

"""Global keyword use to find value only in outside of local as well as GLOBAL only"""

x = 88


def rose():
    x = 20

    def merry():
        global x
        x = 33  # assign the value again

    print("Before calling Merry", x)
    merry()
    print("After calling Merry", x)  # print 20 because value of x in rose() is 20 and its not global variable


rose()
print(x)
"""print 33 because value of x is globally assigned in  merry() and its change the outside (of function)value of x"""
