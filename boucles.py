import time

## Boucle FOR

liste = [1, 2, 3, 4, 5]
for element in liste:
    print(element)

i = 8
for i in [0, 1, 4, 7, 8]:
    print(i)

for i in range(10):
    print("Bonjour")

## Boucle WHILE (tant que "vrai")

i = 0
while i < 10:
    print("Bonjour")
    i += 1

#continuer = "o"
#while continuer == "o":
#    print("On continue...")
#    continuer = input("Voulez-vous continuer ? o/n")

#while True:
#    print("Sauvegarde en cours...")
#    time.sleep(600)

# Avec "continue" on passe directement a la prochaine iteration
# Avec "break" on sort de la boucle
liste = ["1", "4", "25", "Paul", "3", "Pierre"]
for element in liste:
    if element.isdigit():
        #continue
        break
    print(element)

# Comprehensions de listes
liste = [-5, -4, -3, -2, -1, 0, 1, 2, 3, 4, 5]
nombres_positifs = [i for i in liste if i > 0]
print(nombres_positifs)
nombres_positifs = [i * 2 for i in liste if i > 0]
print(nombres_positifs)