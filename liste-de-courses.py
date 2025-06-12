import sys

LISTE = []

# Multiligne avec """
MENU = """Choississez parmi les 5 options suivantes :
1: Ajouter un element a la liste
2: Retirer un element a la liste
3: Afficher la liste
4: Vider la liste
5: Quitter
Votre choix : """

MENU_CHOICES = ["1", "2", "3", "4", "5"]

while True:
    user_choice = ""
    while user_choice not in MENU_CHOICES:
        user_choice = input(MENU)
        if user_choice not in MENU_CHOICES:
            print("Veuillez choisir une option valide...")

    if user_choice == "1": # Ajouter un element
        item = input("Entrer le nom d'un element a ajouter a la liste de courses : ")
        LISTE.append(item)
        print(f"L'element {item} a bien ete ajoute a la liste.")
    elif user_choice == "2": # Retirer un element
        item = input("Entrer le nom d'un element a retirer de la liste de courses : ")
        if item in LISTE:
            LISTE.remove(item)
            print(f"L'element {item} a bien ete retire de la liste.")
        else:
            print(f"L'element {item} n'est pas dans la liste.")
    elif user_choice == "3": # Afficher un element
        if LISTE:
            print("Voici le contenu de votre liste :")
            # Le chifffre indique a quel indice on commence..
            for i, item in enumerate(LISTE, 1): 
                print(f"{i}. {item}")
        else:
            print("Votre liste ne contient aucun element.")
    elif user_choice == "4": # Vider la liste
        LISTE.clear()
        print("La liste a ete videe de son contenu.")
    elif user_choice == "5": # Quitter
        print("A bientot !")
        sys.exit()
        
    print("-" * 50)