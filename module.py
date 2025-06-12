import random, os
# Importer la @fn pprint du module pprint
from pprint import pprint

# Generer un nombre entier aleatoire
r = random.randint(0, 2)
print(r)
# Generer un nombre decimal aleatoire
r = random.uniform(0, 1)
print(r)
# Generer un nombre entier aleatoire avec un "pas"
r = random.randrange(0, 101, 10)
print(r)

# Creer une arborescence
chemin = "/Users/Alex/Desktop/Data/Python"
dossier = os.path.join(chemin, "dossier", "test")
#print(dossier)

## Creer un dossier ##

#os.mkdir()
# Creer un dossier a l'interieur d'un dossier qui n'existe pas
if not os.path.exists(dossier):
    os.makedirs(dossier)
else:
    print("Le dossier existe deja !")

# Idem avec passage d'argument
#os.makedirs(dossier, exist_ok=True)

## Supprimer un dossier ##

if os.path.exists(dossier):
    os.removedirs(dossier)

# Liste des fonctions du module "random" ; voir les fonctions sans "underscores"
pprint(dir(random))
#help(random.randint)