class Emp:
    leaves = 10
    pass

john = Emp()
cena = Emp()

john.name = "John"
john.salary = 50000
john.role = "teacher"

cena.name = "John"
cena.salary = 100
cena.role = "Student"
print(john.salary)