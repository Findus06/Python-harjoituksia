import time


def OnkoJaollinen(n): # onko jaollinen jollain muulla kuin 1:llä tai itsellään
    for i in range(2, n): # tarkistaa kaikki kakkosesta n - 1:een
        if n % i == 0: # Jos on jaollinen
            return True
    return False

def GetPrime(n):
    Primes = [2]
    testiLuku = Primes[-1] + 1 # Primes listan viimainen
    
    #Selvitä onko seuraava luku jaollinen muulla kuin 1:llä tai itsellään.
    #Jos on jaollinen -> ei ole prime
    #Jos ei ole jaollinen millään -> Prime
    while len(Primes) < n:
        if(OnkoJaollinen(testiLuku) == False):
            Primes.append(testiLuku)
        testiLuku += 1
    return Primes[n - 1]

for i in range(5):
    start_time = (time.time()) # Aloita ajanotto
    print(GetPrime(10 ** (i + 1)))
    print("Aika:", time.time() - start_time) # Lopeta ajastin
