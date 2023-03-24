def syracuse(n, lst=[[]]):
    lst[0].append(n)
    if n == 1:
        lst.append(lst[0].index(1)+1)
        lst.append(max(lst[0]))
    else:
        if n%2 == 0:
            syracuse(n//2)
        else:
            syracuse(3*n+1)
    return lst
            

print(syracuse(13))

