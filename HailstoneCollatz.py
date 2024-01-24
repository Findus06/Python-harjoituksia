aloitus = int(input("Anna aloitusluku: "))
def HailstoneNum(n):
    kierros = 0
    Lista = []
    while n != 1:
        if n % 2 == 1:
           n = 3 * n + 1

        elif n % 2 == 0:
          n =  n / 2
        kierros += 1
        print("Kierros: ",kierros, "Luku: ",n)
        Lista.append(n)
    print("Lista: ",Lista)
    return n
    
HailstoneNum(aloitus)