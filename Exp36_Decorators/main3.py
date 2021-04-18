def dec1(def1):
    def exec():
        print("Executing now")
        def1()
        print("Executed")
    return exec

@dec1
def who_is_sandy():
    print("Sandy is good programmer")

#who_is_sandy = dec1(who_is_sandy)   #Decorative function is dec1 another term is @dec1
who_is_sandy()
