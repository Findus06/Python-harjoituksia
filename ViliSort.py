import SortingBase as SB
import random


def viliSort(L):
    #VL = L
    for i in range(len(L)):
        for j in range(0, len(L) - i - 1):
            if L[j] > L[j + 1]:
                L[j], L[j + 1] = L[j + 1], L[j]
    print(L)
    
def bubbleSort(L):
    #VL = L
    for i in range(len(L)):
        for j in range(0, len(L) - i - 1):
            if L[j] > L[j + 1]:
                L[j], L[j + 1] = L[j + 1], L[j]
    print(L)
   
def tarkistaLista(L):
    lippu = 0
    i = 1
    while i < len(L):
        if(L[i] < L[i - 1]):
            lippu = 1
        i += 1
    if (not lippu):
        return False
    else:
        return True
            

def bogoSort(L):
    numero = 0
    while tarkistaLista(L) != False:
        
        for i in range(len(L)):
            RandomIndex = random.randint(0,len(L) - 1)
            L[i], L[RandomIndex] = L[RandomIndex], L[i]
            numero += 1
            print("Lista: ", L, "Kierros: ", numero)
        
  
    
    
def insertionSort(L):
    n = len(L)  # annetaan n:lle sama arvo kuin listan pituus
      
    if n <= 1: # Jos listan pituus on pienempi tai yhtäsuuri kuin 1 niin silloin ei funktiota suoriteta
        return  
 
    for i in range(1, n):  # Luodaan for looppi jossa range on 1 - n:ään
        K = L[i]  # K:lle annetaan arvo joka on sama kuin L i indexi
        j = i-1 # J:lle annetaan arvo joka on sama kuin i index - 1 jotta saadaan edellinen indexin arvo
        while j >= 0 and K < L[j]: # luodaan while looppi jossa katsotaan että onko j isompi kuin tai yhtäsuuri kuin 0 ja 
                                   # katsotaan onko K pienempi kuin Listan j index
            L[j+1] = L[j]  # j:n arvo muuttuu samaksi kuin listan j+1 arvo eli seuraava arvo
            j -= 1 # j:stä otetaan 1 pois jotta saadaan edellinen seuraavassa loopissa
        L[j+1] = K # Listan j+1 arvo vaihdetaan K:n arvoon
    print(L)  # Printataan lista

def quickSort(L):
    PK = [] # Pienempi kuin
    YK = [] # Yhtäsuuri kuin
    SK = [] # Suurempi kuin
    
    for i in range(len(L)):
        PK


    
   



bogoSort([0,3,1,2,4,6,5,7,8,9])
