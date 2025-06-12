print("Hello World !")

#### VARIABLES ####

# Variable
mon_nombre = 10
# Adresse mémoire de la variable
print(id(mon_nombre))

## 1.Affectations ##

a, b = 5, 8
print(a, b)
# Inverser l'affectation
a, b = b, a
print(a, b)
# Affectation multiple
a = b = c = 5

# => "None", "True", "False" est un Singleton (=meme adresse memoire)
# => Plage entre -5 et 256 ; chaines < 20 caracteres => idem

## 2.Types ##

a = 10
# Pour s'assurer du veritable type de la variable (@fn "type")
print(type(a))
# Convertir un nombre entier en chaine de caracteres
str(30)
# Convertir une chaine de caracteres en nombre entier
int("10")

# Saisie utilisateur
#nombre = input("Entrez un nombre : ")
#print(nombre)

# Methodes sur les chaines de caracteres
print("Bonjour".upper())
print("Bonjour".lower())
print("bonjour tout le monde".capitalize())
print("bonjour tout le monde".title())
print("bonjour".replace("jour", "soir"))
print("   bonjour   ".strip()) # Enleve les caracteres a partir du debut / fin de chaine (espaces par defaut)
print("   bonjour   ".strip(" ujor")) # Enleve les caracteres specifies dans le pattern ; s'arrete au premier caractere qui n'est pas dans le pattern
print("   bonjour   ".rstrip(" ujor")) # Idem en partant de la droite
print("   bonjour   ".lstrip(" ujor")) # Idem en partant de la gauche
print(".".join("1, 2, 3, 4, 5".split(", "))) # Transformer une chaine en liste avec "split" et inversement avec "join"

# Ajouter des 0 avec "zfill"
print("9".zfill(4))
for i in range(100):
    print(str(i).zfill(4))

# Verifier si une chaine est..
print("bonjour".islower())
print("50".isdigit())
# Compter le nombre d'occurences de..
print("Bonjour le jour".count(" jour"))
# Retourne l'index de l'occurence dans la chaine
print("Bonjour le jour".find("jour"))
print("Bonjour le jour".index("jour"))
# Idem en partant de la droite (fin)
print("Bonjour le jour".rfind("jour"))
# Se termine par..
print("image.png".endswith(".png"))
# Commence par..
print("image.png".startswith("image"))

# f-string (version > 3.6)
prenom = "Paul"
print(f"Bonjour { prenom } !")
# format
age = 37
phrase = "Je m'appelle {name} et j'ai {age} ans.".format(name=prenom, age=age)
print(phrase)