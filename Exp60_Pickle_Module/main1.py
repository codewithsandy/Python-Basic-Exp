"""How to di-compile pickle file"""
import pickle
file = "Student_list.pkl"
fileobj = open(file,'rb')
stud = pickle.load(fileobj)
print(stud)
