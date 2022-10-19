with open("output.txt", "w") as f:
    f.write(input("Entrez un texte: "))

with open("output.txt", 'r') as f:
    print(f.read())