def searcher():
    import time
    # Some 4 sec time consuming task
    book = "This a very long Book includes 10k pages"
    time.sleep(4)

    while True:
        text = (yield)
        if text in book:
            print("Your text is in the book")
        else:
            print("Your text is not in the book")


""" First search.send() take time for execution it will make coroutine
then next search.send() does not take time for execution
"""

search = searcher()
print("Search Started")
next(search)
search.send("pages")
input("Press any key")
search.send("10k")
input("Press any key")
search.send("hello i am sandy")

search.close()  #Close coroutine

input("Press any key")
search.send("very")
