class Auto:
    def __init__(self):
        self.merkki = ""
        self.vari = ""
        self.paino = 0
        self.vuosimalli = 0
        self.kilometrit = 1
        self.hinta = 0
        
    def Laskuri(self):
        ikak = 1 + (1 / (2022 - self.vuosimalli)) * 10000 * 100
        kmk = 1 + (1 / self.kilometrit) * 10000 * 100
        (ikak + kmk) * 1000
        return(self.hinta)
    
    
    
Auto1 = Auto()

Autot = []
Auto1.merkki = "Toyota"
Auto1.vari = "Valkoinen"
Auto1.paino = 935
Auto1.vuosimalli = 1986
Auto1.kilometrit = 220000
print(Auto1.hinta)

Autot.append(Auto1)
