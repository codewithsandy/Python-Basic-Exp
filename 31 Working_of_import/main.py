import sklearn1 as sk

print(sk.__version__)

import sys

print(sys.path)

from sklearn1.ensemble import RandomForestClassifier

print(RandomForestClassifier)

"""Import file from same directory  and use their functions"""
import file2
print(file2.a)
file2.printfun("Good Programmer ")
