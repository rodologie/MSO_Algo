import math
import random as rand
import csv

class Ville():
    
    def __init__(self, nom, x, y):
        # constructeur de la classe Ville
        self.nom = nom
        self.x = x
        self.y = y
        
    def distance_vers(self, autre_ville):
        distance = math.sqrt((self.x-autre_ville.x)**2+(self.y - autre_ville.y)**2)
        return distance
        
    
    def __str__():
        return self.nom

def generer_ville(nb_villes = 20):
    """ génère nb_villes aux coordonnées aléatoires, si nb_villes vide, 2à par défaut"""
    lst = []
    for val in range(nb_villes):
        ville = Ville(val,rand.randint(0,300),rand.randint(0,300))
        lst.append(ville)
    return lst
    
def lire_csv(file):
    lst = []

    with open('30.csv', 'r') as csvfile:
        spamreader = csv.reader(csvfile, delimiter=' ', quotechar='|')
        for row in spamreader:
            ville = Ville(row[0],row[1],row[2])
            lst.append(ville)
    return lst
            
