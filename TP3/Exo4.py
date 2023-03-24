
def maxliste(lst):
    # cas de base
    if len(lst) == 1:
        return lst[0]
    
    # cas récursif
    else:
        # diviser la liste en deux sous-listes
        milieu = len(lst) // 2
        gauche = lst[:milieu]
        droite = lst[milieu:]
        
        # appel récursif pour trouver le max de chaque sous-liste
        max_gauche = maxliste(gauche)
        max_droite = maxliste(droite)
        
        # trouver le max global entre les max des deux sous-listes
        if max_gauche > max_droite:
            return max_gauche
        else:
            return max_droite



print(maxliste([1,2,3,4,5,6,7,42,9,10,11,12,13,14,15,16,17,18,19,20]))