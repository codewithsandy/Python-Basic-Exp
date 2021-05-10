class Emp:
    leaves = 10

    def print_details(self):
        return f"\nName is {self.name}. \nSallary is {self.salary} \nRole is {self.role}"

""" self is a convention for handle argument....Obj2 in function......print_details()"""

Obj1 = Emp()
Obj2 = Emp()

Obj1.name = "Andersen"
Obj1.salary = 50000
Obj1.role = "teacher"

Obj2.name = "Stephan"
Obj2.salary = 100
Obj2.role = "Student"

print(Obj2.print_details())         # calling function and pass Obj2 argument
