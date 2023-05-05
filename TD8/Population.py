import Ville.py
import Trajet.py

class Population():
    
    def __init__(self):
        self.trajets=[]
        
    def initialiser(self, taille, liste_villes) 
        for i in range(taille):
            self.trajets.append(Trajet(liste_villes))
    
    def ajouter(trajet):
        self.trajets.append(trajet)
    
    def meilleur():
        best = self.trajets[0]
        for trajet in self.trajets:
            if trajet.longueur < best.longueur:
                best = trajet
        return best
    
    def __str__():
        return self.trajets
