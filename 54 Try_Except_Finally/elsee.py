""" if Except not execute then execute else statement otherwise not
    we can use one or more except statement for error handling
    FINALLY is always run it does not require to run previous statement
"""

f1 = open("Sandy.txt")

try:
    f = open("my2.txt")
# except Exception as e:
#     print(e)
except EOFError as e:
    print("Print Eof error")
except IOError as e:
    print("IO Error Occured........")
else:
    print("This will run only when except not running")
finally:
    print("Run this anyway")
    #f.close()
    f1.close()

print("Important Stuff")