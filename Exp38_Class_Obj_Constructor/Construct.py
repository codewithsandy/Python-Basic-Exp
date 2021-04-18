class Emp:
    leaves = 10
    pass

MrBean = Emp()


MrBean.name = "MrBean"
MrBean.salary = 9999
MrBean.role = "Student"
print(Emp.leaves)
print(MrBean.__dict__)
MrBean.leaves = 20         #it creates leaves variable under MrBean
print(MrBean.__dict__)
print(Emp.__dict__)         # instance value of object changes does not affected by class values