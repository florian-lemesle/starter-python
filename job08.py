lrg = int(input("Entrez la largeur: "))
htr = int(input("Entrez la hauteur: "))


for x in range(1, htr+1):
    if x == 1 or x == htr:
        for y in range(1, lrg+3):
            if y == 1:
                print("|", end='')
            elif y == lrg+2:
                print("|")
            else:
                print("-", end='')

    else:
        for y in range(1, lrg+3):
            if y == 1:
                print("|", end='')
            elif y == lrg+2:
                print("|")
            else:
                print(" ", end='')
