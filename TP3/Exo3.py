import time

def fibonacci1(n, f0=1, f1=1):
    if n>0:
        print(f0, end=' ')
        fibonacci1(n-1, f1, f0+f1)
        
def fibonacci2(n):
    if n<= 1:
        return 1
    else:
        return fibonacci2(n-1) + fibonacci2(n-2)

#time1 = time.time()
fibonacci1(40)
#time2 = time.time()
#print('\n')
#print('T1: ',time2-time1)

# time3 = time.time()
# print(fibonacci2(40))
# time4 = time.time()
# print('\n')
# print('T2: ', time4-time3)