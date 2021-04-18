class Employee:
    def __init__(self, fname, lname):
        self.fname = fname
        self.lname = lname
        # self.email = f"{fname}.{lname}@sandy.com"

    def explain(self):
        return f"This employee is {self.fname} {self.lname}"
    @property
    def email(self):
        if self.fname == None or self.lname == None:
            return "Emain is not set"
        return f"{self.fname}.{self.lname}.@parker.com"
    @email.setter
    def email(self, string):
        print("Setting Now")
        names = string.split("@")[0]
        self.fname = names.split(".")[0]
        self.lname = names.split(".")[1]
    @email.deleter
    def email(self):
        self.fname = None
        self.lname = None


obj1 = Employee("Peter", "Parkar")

print(obj1.email)

obj1.fname = "Spider"
print(obj1.email)   #email() mathod take as a property line 9 using @property decorator

obj1.email = "This.man@peter.com"     #display error we cant set use setter

print(obj1.fname)
print(obj1.lname)
print(obj1.email)

del obj1.email

print(obj1.email)