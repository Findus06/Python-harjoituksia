def Kongruenssi(a,r,b): # a = luku yksi, r = luku kaksi, b = jakojäännös
    return a % b == r % b

# printti ei toteudu
if __name__ == "__main__":
    print(Kongruenssi(5,2,3)) # True
    print(Kongruenssi(5,2,4)) # False
    