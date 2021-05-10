""" Constructor - The process of passing argument from line no. 15 To Line no. 2 """

class Emp:
    leaves = 10
    def __init__(self, new_args_name, new_args_salary, new_args_role):          # Constructor function
        self.name = new_args_name
        self.salary = new_args_salary
        self.role = new_args_role
    def print_details(self):
        return f"\nName is {self.name}. \nSallary is {self.salary} \nRole is {self.role}"

"""
__init__ function handles the class argument
Obj1 pass argument to Emp class it will automatically pass argument to __init__  function
"""
Obj1 = Emp("Sandesh", 50000, "Instructor")

print(Obj1.salary)