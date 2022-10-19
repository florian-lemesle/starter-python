def myFun(*args: int):
    myList = [item for item in args]
    myList.sort()
    print(myList)


myFun(4, 6, 5)
