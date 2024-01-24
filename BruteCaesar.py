import CaesarinSalaus as CS


def BruteCaesar(t, n):
    kierros = 1
    for i in range(n+1):
        t1 = CS.CaesarSalausPurkaja(i, t)
        kierros += 1
        print(t1, kierros)

# BruteCaesar("Arouu chnenw, måkoåblbg Cnebnl", 100) # hyvää joulua toivoo julius 81
# BruteCaesar("Zvyyävå deyrd dnnc xnufvyyr?", 100) # milloin tulet taas kahville? 100
BruteCaesar("Tlmxkbq tgw Huxebq tkx vtimnkxw", 300) # 
