class Emp:
    leaves = 10
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
     #   return "Return Value"

"""Single Inheritance"""
class programmer(Emp):
    def __init__(self, new_args_name, new_args_salary, new_args_role, languages):
        self.name = new_args_name
        self.salary = new_args_salary
        self.role = new_args_role
        self.languages = languages
    def print2(self):
        return f"The Programmer name is {self.name}. \nSalary is {self.salary}. \nRole is {self.role} \nLanguages Known {self.languages}"

sandy = Emp("Sandesh", 50000, "Instructor")
avi = Emp("Avinash", 50001, "Student")

ruchita = programmer("Ruchita", 600, "Programmer", ["Python", "C Prog"])
rosy = programmer("Rosy", 200, "Programmer", ["Python", "Data Structure"])

print(rosy.print2())