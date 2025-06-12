import os

def verifier_fichier():
    return os.path.exists("fichier.txt")
    #if os.path.exists("fichier.txt"):
    #    return True
    #return False

# Retourne "None"
def test():
    pass

def affiche(message="Message par defaut"):
    #global var => Precise qu'il faut mettre la variable "var" en global (=mauvaise pratique ; preferer le "return")
    print(message)
affiche()
affiche("Bonjour")

#print(globals() == locals())
#print(globals())
#print(locals())

# Passage par reference
def foo(param):
    #print(id(param))
    #param.append(1)
    test = param.copy()
    test.append(4)
    print(test)

var = [1, 2, 3]
print(id(var))
foo(param=var)
print(var)