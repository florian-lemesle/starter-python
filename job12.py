file = open("data.txt", "r")
data = file.read()
words = data.split()

print('Le nombre de mots dans le fichier est de', len(words))
