"""
Classes - Template
Object - Instance of Class
DRY - Do Not Repeat Yourself
"""


class student:
    pass            # pass means nothing else


""" sandy and sara is the object of student class """

sandy = student()               # sandy object derived to student class
instance2 = student()
print(sandy, instance2)              # both object are different and stored on different location

sandy.name = "Sandesh"          # .name is the instance
sandy.std = 12
sandy.section = 1
print(sandy.name)

instance2.name = "Issueeee"            # No any compaltion for assign all the instace for all object
instance2.subjects = ["Python", "Machine Learning", "Artificial Intelligence"]
print("\n1.Instance name is: ", instance2.name, "\n2.Subjects Name Are: ", instance2.subjects)