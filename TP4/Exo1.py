def tri(lst):
    for i in range(len(lst)):
        for j in range(i+1,len(lst)):
            if lst[i]>lst[j]:
                lst[i],lst[j] = lst[j], lst[i]
    return lst


def randomList(n):
    import random
    lst = []
    for i in range(n):
        lst.append(random.randint(0,100))
    return lst

lst = randomList(10)
print(lst)
print(tri(lst))
