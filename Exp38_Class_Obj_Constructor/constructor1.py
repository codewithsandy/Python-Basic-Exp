class Emp:
    leaves = 10
    pass


john = Emp()
cena = Emp()
MrBean = Emp()

"""Instance name for joh like name salary role"""
john.name = "John"
john.salary = 50000
john.role = "teacher"

cena.name = "John"
cena.salary = 100
cena.role = "Student"
print(john.salary)

print(Emp.leaves)
john.leaves = 15        #do not assign values aginst the class it doesent take
print("\t", Emp.leaves)

print(Emp.__dict__)

