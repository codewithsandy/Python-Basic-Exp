
def printsan(string):
    return f"This Is Not Possible {string}"

def add(n1, n2):
    return n1 + n2 +5


"""main1 file import in main2 but execution start from MAIN FUNCTION also this methos use to print the file name"""
print("One More Issue is ", __name__)

"""Void main function"""
if __name__ == '__main__':
    print(printsan("Sandy"))
    o = add(5, 5)
    print(o)