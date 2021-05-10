Num_List = ["60", "25", "11", "1997"]

Num_List = list(map(int, Num_List))
# Under Map function first passed argument that can convert the string to like int (as per need)


Num_List[2] = Num_List[2] + 1
print(Num_List[2])

def sq(a):
    return a*a

num = [5, 3, 4, 8, 9, 2]
square = list(map(sq, num))
print(square)