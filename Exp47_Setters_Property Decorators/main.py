class Employee:
    def __init__(self, fname, lname):
        self.fname = fname
        self.lname = lname
        self.email = f"{fname}.{lname}@sandy.com"

    def explain(self):
        return f"This employee is {self.fname} {self.lname}"
    def printmail(self):
        pass

obj1 = Employee("Peter", "Parkar")
obj2 = Employee("Sandy", "Pol")

print(obj1.explain())

print(obj1.email)
obj1.fname = "Spider"
print(obj1.email)

