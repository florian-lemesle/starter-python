nb = int(input("Entrez un nombre entier: "))
file = open("data.txt", "r")
data = file.read()
words = data.split()
counter = 0

for word in words:
    if len(word) == nb:
        counter += 1

print(counter)

