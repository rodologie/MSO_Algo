# tour de Hanoi

def hanoi(n, depart, arrivee, intermediaire):
    if n == 1:
        print("Déplacer un disque du pilier", depart, "vers le pilier", arrivee)
    else:
        hanoi(n-1, depart, intermediaire, arrivee)
        print("Déplacer un disque du pilier", depart, "vers le pilier", arrivee)
        hanoi(n-1, intermediaire, arrivee, depart)

    
