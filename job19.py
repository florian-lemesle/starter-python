def myFun(*args: int):
    myList = [item for item in args]
    new_list = []

    while myList:
        minimum = myList[0]
        for x in myList:
            if x < minimum:
                minimum = x
        new_list.append(minimum)
        myList.remove(minimum)

    print(new_list)

myFun(4, 6, 5)

