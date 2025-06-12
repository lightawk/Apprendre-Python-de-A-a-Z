class Voiture:
    # Attribut de classe
    voitures_crees = 0
    # Constructeur ("self" fait referene a l'instance)
    def __init__(self, marque):
        Voiture.voitures_crees += 1
        self.marque = marque
    # Methode "afficher_marque"
    def afficher_marque(self, vitesse):
        print(f"La marque de la voiture est {self.marque}, sa vitesse est de {vitesse}")

voiture_01 = Voiture("Renault")
voiture_02 = Voiture("Volkswagen")
#voiture_01.afficher_marque()
Voiture.afficher_marque(voiture_01, 50)

#print(voiture_01.marque)
#print(voiture_02.marque)
#print(Voiture.voitures_crees)