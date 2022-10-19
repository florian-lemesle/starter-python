def mySort(*args: list):
    myList = [item for item in args]
    new_list = []

    while myList:
        minimum = myList[0]
        for x in myList:
            if x < minimum:
                minimum = x
        new_list.append(minimum)
        myList.remove(minimum)

    return new_list


result = mySort(4, 6, 5)


def myDisplay(*args: list):
    myList = [item for item in args]
    print(myList)


myDisplay(5, 6)

#j'ai loupé une journée entière pour des raisons personels, sur les 3 journées qu'on avait pour les jobs, je n'ai donc pas pu faire les job 22 et pour aller plus loin.
