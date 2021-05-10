class Dad:
    basketball = 1

class Son(Dad):
    dance = 2
    basketball = 2
    def isdance(self):
        return f"Yes i dance {self.dance} no. of times"

class Grand_son(Son):
    dance = 5
    def isdance(self):
        return f"I dance awesomely {self.dance} no. of times"

instance1 = Dad()
instance1 = Son()
instance1 = Grand_son()
print(instance1.isdance())

print("Basketball plays ", instance1.basketball, "Time")
# First check variable itself and does not found then it will check  one by one upper level (Bottom to Top)