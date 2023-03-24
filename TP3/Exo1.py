def croissant(n):
    if n>=1:
        croissant(n-1)
        print(n, end=' ')
    
def decroissant(max):
    if max >= 1:
        print(max, end=' ')
        decroissant(max-1)  

croissant(10)
print('\n')
decroissant(10)