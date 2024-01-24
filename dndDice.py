import random as ran

def Noppa(m,s):
    m2 = int(m)
    s2 = int(s)
    for i in range(m2):
        tulos = ran.randint(1,s2)
        print(tulos)
        


Noppa(input("Syötä noppien määrä: "),input("Syötä sivujen määrä: "))