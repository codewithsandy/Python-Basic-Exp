from functools import reduce

list1 = [1, 2, 3, 4, 5]
num = 0
for i in list1:
    num = num + i
print(num)

print("\n")

"""Map Reduce Function"""
num1 = reduce(lambda x,y:x+y, list1)
print(num1)