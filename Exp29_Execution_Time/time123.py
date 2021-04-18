import time

initial = time.time()
#print(initial)
k = 0
while(k<10):
    print("This is sandy program")
    k+=1
print("while loop execution time: ", time.time() - initial, "Seconds")

initial2 = time.time()
for i in range(1000000):
    print("T")
print("for loop execution time: ", time.time() - initial2, "Seconds")

localtime = time.asctime(time.localtime(time.time()))
print(localtime)