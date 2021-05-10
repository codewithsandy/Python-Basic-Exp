import time

initial = time.time()
#print(initial)
k = 0
while(k<10):
    print("This is sandy program")
    time.sleep(2)
    k+=1
print("while loop execution time: ", time.time() - initial, "Seconds")
