import random

#Lotto peli
#1-41 lukuja
VoittoRivi = []
Arvaukset = []
#Luuppaa 7 kertaa
#ei  saa olla samoja lukuja
#tarkistaa ja vaihtaa samat luvut


#Pelaajan inputti
while len(Arvaukset) < 7:
    luku = int(input("Anna Lukuja: "))
    
    if luku > 41 or luku < 1:
        print("Luku ei ole alueen sisällä")
        continue
    
    if luku not in Arvaukset:
        Arvaukset.append(luku)
    else:
        print("Olet jo kirjoittanut tämän")
        
while len(VoittoRivi) < 7:
    num = random.randint(1,42)
    if num not in VoittoRivi:
        VoittoRivi.append(num)
    if luku not in VoittoRivi:
        VoittoRivi.append(luku)
