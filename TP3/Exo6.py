#La complexité d'un algorithme de recherche séquentielle est de O(n). Dans le meilleur des cas, elle est de n+1.
#Dans le pire des cas, elle est de 2n+1.
#Elle est en moyenne de (3n+1)/2.


# La complexité d'un algorithme de recherche dichotomique est de O(log(n)).
# Dans le meilleur des cas, elle est de log(n)+1.
# Dans le pire des cas, elle est de 2log(n)+1.
# Elle est en moyenne de (3log(n)+1)/2.


def dicho(list,lst,k):
    if lst[len(lst)//2] > k:
        if k<lst[0]:
            print("impossible")
            return -1
        else:
            dicho(list,lst[:len(lst)//2],k)
    elif lst[len(lst)//2] < k:
        if k>lst[-1]:
            print("impossible")
        else:
            dicho(list, lst[len(lst)//2:],k)
    elif lst[len(lst)//2] == k:
        print(list.index(k))


lst = [2,4,5,7,8,9,10,11,12,13,14,15,16,17,18,19,20]
dicho(lst,lst,7)