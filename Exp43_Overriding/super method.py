class A:
    classvar1 = "I am in class A"   #class var
    def __init__(self):                                 #Constructor of class A
        self.var1 = "I am Inside class A constructor"
        self.classvar1 = "Instance var in class A"
        self.special = "Special"

class B(A):
    classvar1 = "I am in class B"   #classvar1 overriding

    def __init__(self):                                 #Constructor of class B
                                     # call before define instance var
        self.var1 = "I am Inside class B constructor"
        #self.classvar1 = "Instance var in class B"          #Instance var overriding
        super().__init__()
        print(super().classvar1)


a = A()
b = B()

print("\n", b.special, "\n",b.var1, "\n",b.classvar1)
