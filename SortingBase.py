import random as ran


def LuoLista(n):
    L = []
    for i in range(n):
        L.append(i + 1)
    return L

def SekoitaLista(L):
    for i in range(len(L)):
        RandomIndex = ran.randint(0,len(L) - 1)
        L[i], L[RandomIndex] = L[RandomIndex], L[i]
    return L




