nb1 = int(input("Rentrez un premier nombre: "))
nb2 = int(input("Rentrez un second nombre: "))

if nb1 == nb2:
    print("Valeurs égales")

else:
    if nb1 < nb2:
        for sequence in range(nb1-1, nb2):
            print(sequence)

    else:

        for sequence in range(nb1-1, nb2, -1):
            print(sequence)





