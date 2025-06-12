# Une liste est un objet "mutable" i.e on peut la modifier
liste_1 = [1, 2, 3, 4, 5]
liste_2 = [250, "Python", True]

## Methodes de listes

liste_1.append(5)
print(liste_1)
liste_1.extend([10, 25, 15])
print(liste_1)
liste_1.remove(5)
print(liste_1)

# Slices
liste_3 = [
    "utilisateur_01",
    "utilisateur_02",
    "utilisateur_03",
    "utilisateur_04",
    "utilisateur_05"
]
print(liste_3[1:2])
print(liste_3[::2]) # Par pas de 2

## Méthodes de d'index / de tri

employes = ["Carlos", "Max", "Martine", "Patrick", "Alex", "Max"]
resultat = employes.index("Max")
#resultat = employes.count("Max")
#employes.sort() # Ne renvoie rien
employes = sorted(employes)
employes.reverse()
print(employes)

## Enlever des elements

element = employes.pop(-1)
print(element)
print(employes)
employes.clear()
print(employes)

## Joindre des elements

employes = ["Carlos", "Max", "Martine", "Patrick", "Alex", "Max"]
#resultat = "_".join(employes)
resultat = "\n".join(employes)
print(resultat)

## Separer une chaine de caracteres en differents elements

courses = "Riz, Pommes, Lait, Salade, Saumon, Beurre"
courses = courses.split(", ")
print(courses)

# Listes imbriquées
liste_4 = ["Python", ["Java", "C++", ["C"]], ["Ruby"]]
print(liste_4[1][-1][0])
print(liste_4[1][0:2])

# Longueur de chaine / liste
print(len("Python"))
print(len([1, 2, 3]))

# Agregats
print(round(2.2))
print(min([1, 2, 3]))
print(max([1, 2, 3]))
print(sum([10, 10, 10]))
print(list(range(2, 5)))