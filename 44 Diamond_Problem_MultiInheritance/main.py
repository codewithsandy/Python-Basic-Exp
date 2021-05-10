class A():
    def method1(self):
        print("This is a Method of Class A")

class B(A):
    def method1(self):
        print("This is a Method of Class B")
class C(A):
    def method1(self):
        print("This is a Method of Class C")
class D(B, C):
    def method1(self):
        print("This is a Method of Class D")

a = A()
b = B()
c = C()
d = D()

d.method1()
