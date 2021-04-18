def square(a):
    return a*a

def cube(a):
    return a*a*a

func = [square, cube]
#num = [5, 3, 4, 8, 9, 2]

for i in range(5):
    val = list(map(lambda x:x(i), func))        #Its Perform x=2 : x(i)  2(i)   i is the value of for loop
    print(val)