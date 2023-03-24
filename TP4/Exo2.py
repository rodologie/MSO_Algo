# Le temps d'execution du tri fusion est de T(n) = 2*T(n/2) + O(n)
# Méthode d'itération: voir cours page 26
#
#
#
#
#
#
#
#


def Fusion(lst):
    if len(lst) == 1:
        return lst
    else:
        mid = len(lst)//2
        left = lst[:mid]
        right = lst[mid:]
        left = Fusion(left)
        right = Fusion(right)
        return Fusion(left,right)
    
    
def randomList(n):
    import random
    lst = []
    for i in range(n):
        lst.append(random.randint(0,100))
    return lst

lst = randomList(10)
print(Fusion(lst))