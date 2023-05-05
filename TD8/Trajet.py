import random
import Ville.py

class Trajet():

    def __init__(self, lst=[]):
        self.ville = random.sample(lst)
        self.longueur = calc_longueur()
        
    def calc_longueur(self, Ville1, Ville2):
        distance = 0
        for val in range(len(self.ville)):
            distance += Ville1.distance_vers(ville2)
        return distance
    
    def est_valide(self):
        for ville1 in self.ville:
            for ville2 in self.ville:
                if ville1 == ville2:
                    return False
        
        return True
    
    def __str__():
        return f"Trajet: {self.ville} \nDistance: {self.longueur}"
