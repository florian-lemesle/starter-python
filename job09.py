h = int(input("Entrez la hauteur: "))
espace1 = (h - 1)
espace2 = 0

while 0 <= espace1:

    for x in range(0, espace1):
        if x != espace1:
            print(" ", end='')
    print("/", end='')

    for x in range(0, espace2):
        if espace1 == 0:
            print("_", end='')
        else:
            print(" ", end='')
    print("\\")

    espace1 = (espace1 - 1)
    espace2 = (espace2 + 2)
