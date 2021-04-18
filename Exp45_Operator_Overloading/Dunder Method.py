class Employee:
    leaves = 5
    def __init__(self, name, salary, role):
        self.name = name
        self.salary = salary
        self.role = role

    def printdetails(self):
            return f"The name is {self.name}, Salary is {self.salary} Role is {self.role}"
    @classmethod
    def change_leaves(cls, newleaves):
            cls.leaves = newleaves

    #"""............Dunder Method..............."""
    def __add__(self, other):
            return self.salary + other.salary

    def __truediv__(self, other):
        return self.salary / other.salary

    def __repr__(self):
        return f"Employee ('{self.name}', {self.salary}, '{self.role}')"

    def __str__(self):
        return f"The name is {self.name}, Salary is {self.salary} Role is {self.role}"

emp1 = Employee("Sandy", 475, "Programmer")
emp2 = Employee("Peter", 5, "Spider Man")

print(emp1 + emp2)
print(emp1 / emp2)
print(emp1)