from random import randint

nombre_a_trouver = randint(0, 100)
essais_restants = 5

print("**** Le jeu du nombre mystere ****")

# Boucle principale
while essais_restants > 0:
    print(f"Il te reste {essais_restants} essai{'s' if essais_restants > 1 else ''}")

    # Saisie de l'utilisateur
    choix_utilisateur = input("Devine le nombre :")
    if not choix_utilisateur.isdigit():
        print("Veuillez entrer un nombre valide.")
        continue

    choix_utilisateur = int(choix_utilisateur)

    if nombre_a_trouver > choix_utilisateur: # Plus grand
        print(f"Le nombre mystere est plus grand que {choix_utilisateur}")
    elif nombre_a_trouver < choix_utilisateur: # Plus petit
        print(f"Le nombre mystere est plus petit que {choix_utilisateur}")
    else: # Egal (succes)
        break

    essais_restants -= 1

# Gagne ou perdu
if essais_restants == 0:
    print(f"Dommage ! Le nombre mystere etait {nombre_a_trouver}")
else:
    print(f"Bravo ! Le nombre mystere etait bien {nombre_a_trouver} !")
    print(f"Tu as trouve le nombre en {6 - essais_restants} essai")

print("Fin du jeu.")