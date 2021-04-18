"""
public - Anyone can use
Protected-  use _ for define    variable use only in Base and Derived Class
Private-    use __ for define
"""
class Emp:
    leaves = 10
    war = 4
    _protected_var = 9
    __private_var = 5
    def __init__(self, new_args_name, new_args_salary, new_args_role):          # Constructor function
        self.name = new_args_name
        self.salary = new_args_salary
        self.role = new_args_role

    def print_details(self):
        return f"\nName is {self.name}. \nSallary is {self.salary} \nRole is {self.role}"

    @classmethod
    def change_leaves(cls, new_leaves):
        cls.leaves = new_leaves
    @classmethod
    def from_dash(cls, string):
        params = string.split("-")
        return  cls(params[0], params[1], params[2])
    @staticmethod
    def print1(string):
        print("This is a good  " + string)

emp = Emp("Sandy", 500, "Programmer")

print(emp._protected_var)
#print(emp.__private_var)   #display erreor while using protected
#how to use private var
print(emp._Emp__private_var)    #name mambling
