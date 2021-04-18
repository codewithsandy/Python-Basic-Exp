#a = input("What is your name: ")
# b = input("How much do you earn:  ")
# if int(b==0):
#     raise ZeroDivisionError("B is zero")
#
# if a.isnumeric():
#     raise Exception("Numbers not allowed")
#
# print(f"Hello {a}")

c = input("Enter your name")
try:
    print(a)

except Exception as e:
    if c=="sandy":
        raise ValueError("Sandy is blocked, He is not allowed")
    print("exception handled")