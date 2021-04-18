""" Pickling a file Object"""
import pickle

stud = ["Sandy", "Avi", "Rosy", "Peter", "Rugita", "Josef"]
file = "Student_list.pkl"
fileobj = open(file, 'wb')
pickle.dump(stud, fileobj)
fileobj.close()