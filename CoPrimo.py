import tekijat as SYT

def coPrimo(n): # n = 8
    L = []
    for i in range(1,n):
        if SYT.SYT([i,n]) == 1:
            L.append(i)
    return L

if __name__ == "__main__":
    print(coPrimo(8)) # [1, 3, 5, 7]
