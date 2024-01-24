def Tekijät(n):
    T = []
    for i in range(1,n+1):
        if n % i == 0: # Jos jakaantuu tasan, niin jakojäännös on 0
            T.append(i)
            
    return T

def Tekijät2(n):
    T = [1]
    for i in range(2,n):
        if n % i == 0: # Jos jakaantuu tasan, niin jakojäännös on 0
            T.append(i)
    T.append(n)       
    return T
    
            
    
# print(Tekijät(16)) # [1, 2, 4, 8, 16]
# print(Tekijät2(16)) # [1, 2, 4, 8, 16]
# 1 * 16, 2 * 8, 4 * 4, 8 * 2, 16 * 1
# Tekijät ovat luonnolliset luvut, joilla saadaan kerrottuna alkuperäinen luku.


def SYT(L):
    L.sort()
    nollat = L.count(0)
    for i in range(nollat):
        L.remove(0)

    if  len(L) == 1:
        return L[0]
    if len(L) == 0:
        return L[0]
    T0 = Tekijät(L[0])
    T1 = Tekijät(L[1])
    
    i0 = len(T0)-1 
    i1 = len(T1)-1
    suurin = -1
    while True:
        if T0[i0] == T1[i1]:
            suurin = T0[i0]
            break
        if T0[i0] > T1[i1]:
            i0 -= 1
        else:
            i1 -= 1
 
    return SYT(L[2:] + [suurin])

#print(SYT([84,64,54])) # 2 
#print(SYT([24,16,64,128])) # 8
#print(SYT([15, 10, 5, 3, 2, 1, 0])) # 1       

        
        