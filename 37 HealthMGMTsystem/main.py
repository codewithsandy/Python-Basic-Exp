# Health Management System

# Health Management System
# 3 clients - Rose, Merry and Aileena

def getdate():
    import datetime
    return datetime.datetime.now()


# Total 6 files
# write a function that when executed takes as input client name
# One more function to retrieve exercise or food for any client


# bhai ye rha program
import datetime


def gettime():
    return datetime.datetime.now()


def take(k):
    if k == 1:
        c = int(input("enter 1 for excersise and 2 for food"))
        if (c == 1):
            value = input("type here\n")
            with open("Rose-ex.txt", "a") as op:
                op.write(str([str(gettime())]) + ": " + value + "\n")
            print("successfully written")
        elif (c == 2):
            value = input("type here\n")
            with open("Rose-food.txt", "a") as op:
                op.write(str([str(gettime())]) + ": " + value + "\n")
            print("successfully written")
    elif (k == 2):
        c = int(input("enter 1 for excersise and 2 for food"))
        if (c == 1):
            value = input("type here\n")
            with open("Merry-ex.txt", "a") as op:
                op.write(str([str(gettime())]) + ": " + value + "\n")
            print("successfully written")
        elif (c == 2):
            value = input("type here\n")
            with open("Merry-food.txt", "a") as op:
                op.write(str([str(gettime())]) + ": " + value + "\n")
            print("successfully written")
    elif (k == 3):
        c = int(input("enter 1 for excersise and 2 for food"))
        if (c == 1):
            value = input("type here\n")
            with open("Aileena-ex.txt", "a") as op:
                op.write(str([str(gettime())]) + ": " + value + "\n")
            print("successfully written")
        elif (c == 2):
            value = input("type here\n")
            with open("Aileena-food.txt", "a") as op:
                op.write(str([str(gettime())]) + ": " + value + "\n")
            print("successfully written")
    else:
        print("plz enter valid input (1(Rose),2(Merry),3(Aileena)")


def retrieve(k):
    if k == 1:
        c = int(input("enter 1 for excersise and 2 for food"))
        if (c == 1):
            with open("Rose-ex.txt") as op:
                for i in op:
                    print(i, end="")
        elif (c == 2):
            with open("Rose-food.txt") as op:
                for i in op:
                    print(i, end="")
    elif (k == 2):
        c = int(input("enter 1 for excersise and 2 for food"))
        if (c == 1):
            with open("Merry-ex.txt") as op:
                for i in op:
                    print(i, end="")
        elif (c == 2):
            with open("Merry-food.txt") as op:
                for i in op:
                    print(i, end="")
    elif (k == 3):
        c = int(input("enter 1 for excersise and 2 for food"))
        if (c == 1):
            with open("Aileena-ex.txt") as op:
                for i in op:
                    print(i, end="")
        elif (c == 2):
            with open("Aileena-food.txt") as op:
                for i in op:
                    print(i, end="")
    else:
        print("plz enter valid input (Rose,Merry,Aileena)")


print("health management system: ")
a = int(input("Press 1 for log the value and 2 for retrieve "))

if a == 1:
    b = int(input("Press 1 for Rose 2 for Merry 3 for Aileena "))
    take(b)
else:
    b = int(input("Press 1 for Rose 2 for Merry 3 for Aileena "))
    retrieve(b)

