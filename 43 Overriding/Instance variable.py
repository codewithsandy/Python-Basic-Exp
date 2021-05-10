""".................................IMPORTANT..................................................
        OverRiding
Instance variable - print(b.classvar1) first check the Instance var in class B if not found then
check  Instance var in class A if not found it will print class variable
............................................................................................."""

class A:
    classvar1 = "I am in class A"   #class var
    def __init__(self):
        self.var1 = "I am Inside class A constructor"
        self.classvar1 = "Instance var in class A"      #instance class var

class B(A):
    classvar1 = "I am in class B"

# a is a instance variable of class A
a = A()
b = B()
print(b.classvar1)