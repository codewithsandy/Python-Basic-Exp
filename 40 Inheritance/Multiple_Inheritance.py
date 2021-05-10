class Emp:
    leaves = 10
    war = 4
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

class player:
    no_of_games = 4
    war = 5
    def __init__(self, name, game):
        self.name = name
        self.game = game
    def print_details(self):
        return f"\nName is {self.name}. \nGame is {self.game}"

"""Multiple Inheritance"""
class CoolProgrammer(Emp, player):
    languages = "C++"
    war = 6
    def print_lang(self):
        print(self.languages)

sandy = Emp("Sandesh", 50000, "Instructor")
avi = Emp("Avinash", 50001, "Student")

ruchita = player("Ruchita", ["Cricket"])
rosy = CoolProgrammer("Rosy", 6565, "Cool_Programmer")
rosy.print_lang()
print(rosy.war)     #Print War priority wise
print(rosy. __dict__)

