""".................................IMPORTANT..................................................
        Instance OverRiding
Instance variable - print(b.classvar1) first check the Instance var in class B if not found then
check Instance var in class A BUT NOT print Because its overrides in class B Then it will print class variable
    How to Use Overrided Variable of Class A
use super().__init__() in class B
............................................................................................."""
class A:
    classvar1 = "I am in class A"   #class var
    def __init__(self):                                 #Constructor of class A
        self.var1 = "I am Inside class A constructor"
        self.classvar1 = "Instance var in class A"
        self.special = "Special"

class B(A):
    classvar1 = "I am in class B"   #classvar1 overriding

    def __init__(self):                                 #Constructor of class B
        super().__init__()                              # call before define instance var
        self.var1 = "I am Inside class B constructor"
        #self.classvar1 = "Instance var in class B"          #Instance var overriding

    # a is a instance variable of class A
a = A()
b = B()
print(b.classvar1)
print(b.special) #Print overrided instance var from class A

print("\n", b.special, "\n",b.var1, "\n",b.classvar1)
