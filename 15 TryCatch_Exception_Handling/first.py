print("Enter Num 1 : ")
num1 = input()
print("Enter Num 2 : ")
num2 = input()
try:
    print("Sum = ", int(num1)+int(num2))
except Exception as e:
    print(e)


print("\tThis is important")