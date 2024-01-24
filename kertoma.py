def kertoma(n):
    tulos = 1
    kierros = 1
    
    while kierros < n+1:
        tulos *= kierros
        kierros += 1   
        print(tulos) 
    return tulos


kertoma(6)