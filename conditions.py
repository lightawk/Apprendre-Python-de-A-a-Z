utilisateur = "root"
mot_de_passe = ""

if utilisateur == "root" and mot_de_passe == "":
    print("Acces autorise !")
else:
    print("Acces non autorise !")

if not utilisateur == "root":
    print("Acces non autorise !")

#if..:
#elif..:
#else..:

# Differents types d'erreurs => SyntaxError: invalid syntax (regarder avant l'accent) / RuntimeError / NameError / TypeError