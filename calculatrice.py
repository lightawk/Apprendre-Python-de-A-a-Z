#a = input("Entrez un premier nombre : ")
#b = input("Entrez un deuxieme nombre : ")
#print(f"Le resultat de l'addition de {a} avec {b} est égal a { int(a) + int(b) }")

a = b = ""
# Tant que "a" et "b" ne contiennent pas des nombres on continue..
while not (a.isdigit() and b.isdigit()):
    a = input("Entrez un premier nombre : ")
    b = input("Entrez un deuxième nombre : ")
    if not (a.isdigit() and b.isdigit()):
        print("Veuillez entrer deux nombres valides.")

print(f"Le resultat de l'addition de {a} avec {b} est egal a {int(a) + int(b)}")