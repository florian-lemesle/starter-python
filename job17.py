def myFun(*args: int):
    myList = [item for item in args]
    for x in myList:
        if x % 2 == 0:
            print(x)


myFun(7, 8, 6)
