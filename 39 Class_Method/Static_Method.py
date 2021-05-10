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


sandy = Emp("Sandesh", 50000, "Instructor")
avi = Emp("Avinash", 50001, "Student")
ros = Emp.from_dash("Rose-80000-Teacher")

print(ros.salary)
print(Emp.print1("Rosy"))
