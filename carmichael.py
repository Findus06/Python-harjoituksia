import CoPrimo as cp
import kongruenssi as kong

def carmichael(n):
    a = cp.coPrimo(n)
    m = 1
    
    while True:
        Tarkistin = True
        for i in range(len(a)):
            if kong.Kongruenssi(a[i]**m, 1, n) == False:
                m += 1
                Tarkistin = False
                break
        
        if Tarkistin == True:
            return m
        
print(carmichael(100))
print(carmichael(56))
print(carmichael(255))
        