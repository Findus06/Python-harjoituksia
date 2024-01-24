def Binaarihaku(n,l):
    if len(l) == 1:
        return l[0]
    # Puolet = len / 2
    puolet = int(len(l) / 2)
    alkuPuoli = l[:puolet]
    loppuPuoli = l[puolet:]
    
    if n <= alkuPuoli[-1]:
        return Binaarihaku(n, alkuPuoli)
    if n >= loppuPuoli[0]:
        return Binaarihaku(n, loppuPuoli)
    
print(Binaarihaku(8,[0,1,2,3,4,5,6,7,8,9]))