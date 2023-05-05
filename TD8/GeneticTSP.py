import os
import Population
import Trajet
import random

class PVC_Genetique:

    def __init__(self, lst_villes, taille_pop = 40, nb_generation = 100):
        self.lstvilles = lst_villes
        self.taille_pop = taille_pop
        self.nb_generation = nb_generation
        
    
    def croiser(parent1, parent2):
        e1 = Trajet()
        e2 = Trajet()
        done = []
        inter = random.randint(1,len(p1.lstvilles)):
            e1.ville = p1.lstvilles[:inter]
            e2.ville = p2.lstvilles[inter:]
            for i in range(len(e1)):
                if e1.lstvilles[i] in done:
                    for ville_rempl in e2:
                        if ville_rempl not in done:
                            e1.lstvilles[i] = ville_rempl
                            done.append(ville_rempl)
                            break
                else:
                    done.append(e1.lstvilles[i])
            e1.calc_dist()
            return e1
    
    def muter(self, trajet):
        i1 = random.randint(0,len(trajet.lstvilles))
        i2 = random.randint(0,len(trajet.lstvilles))
        trajet.lstvilles[i],trajet.lstvilles[i2] = trajet.lstvilles[i2],trajet.lstvilles[i1]
        trajet.calc_dist()
        return trajet
        
    
    def selectionner(self, population):
        moy = 0
        for path in population.trajet:
            moy += path.longueur
        moy = moy/len(population.trajet)
        for path in population.trajet:
            if path.longueur > moy:
            p.trajet.remove(path)
        return population
    
    def evoluer(self, population):
        nb_init = len(population.trajet)
        self.selectionner(population)
        while len(population.trajet) < nb_init:
            p1 = random.choice(population.trajet)
            p2 = random.choice(population.trajet)
            population.trajet.append(self.croiser(p1,p2))
    
    

    def clear_term(self):
        os.system('cls' if os.name=='nt' else 'clear')
    
def main():
    # A compléter
    return

if __name__ == "__main__":
    main()
