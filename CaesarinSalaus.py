aakkoset = ['a','b','c','d','e','f','g','h','i','j','k','l','m','n','o','p','q','r','s','t','u','w','v','x','y','z','å','ä','ö']

def CaesarSalaus(n,s):
    L = []
    for i in range(len(s)): # Käydään läpi kaikki merkit
        if s[i] == ' ': # Ohita välilyönti
            L.append(' ')
        else:
            if s[i] in aakkoset:
                if s[i].isupper(): # Tarkista, onko kirjain iso
                    L.append(aakkoset[(aakkoset.index(s[i].lower()) + n) % len(aakkoset)].upper()) # Lisätään iso kirjain takaisin isona
                else:
                    L.append(aakkoset[(aakkoset.index(s[i]) + n) % len(aakkoset)]) # Lisätään listaan kirjain, joka on n askeleen päässä aakkoset-listan kirjaimesta
            else:
                L.append(s[i]) # Lisätään erikoismerkki sellaisenaan
    return "".join(L) # Palautetaan lista merkkijonona

def CaesarSalausPurkaja(n,s):
    s = s.lower() # Muutetaan kaikki pieniksi kirjaimiksi
    L = [] # Lista, johon tulee salauksen purkamisen jälkeen kirjaimet
    for i in range(len(s)): # Käydään läpi kaikki merkit
        if s[i] == ' ': # Ohita välilyönti
            L.append(' ')
        else:
            if s[i] in aakkoset:
                if s[i].isupper(): # Tarkista, onko kirjain iso
                    L.append(aakkoset[(aakkoset.index(s[i].lower()) - n) % len(aakkoset)].upper()) # Lisätään iso kirjain takaisin isona
                else:
                    L.append(aakkoset[(aakkoset.index(s[i]) - n) % len(aakkoset)]) # Lisätään listaan kirjain, joka on n askeleen päässä aakkoset-listan kirjaimesta
            else:
                L.append(s[i]) # Lisätään erikoismerkki sellaisenaan
    return "".join(L) # Palautetaan lista merkkijonona

if __name__ == "__main__":
    print(CaesarSalausPurkaja(5,"Tunxpjqnof")) # Opiskelija
    print(CaesarSalausPurkaja(-3,"qbhbb åfkå")) # tekee aina
    print(CaesarSalausPurkaja(-4,"durxx puypx")) # hywää työtä
    print(CaesarSalausPurkaja(8,"pqx pqx pözii!")) # hip hip huraa!
