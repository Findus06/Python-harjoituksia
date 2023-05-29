def tarkista_mana(manapooli, kortin_mana):
    manapooli_sanakirja = muunna_mana_sanakirjaksi(manapooli)
    kortin_mana_sanakirja = muunna_mana_sanakirjaksi(kortin_mana)

    for valu, maara in kortin_mana_sanakirja.items():
        if valu not in manapooli_sanakirja or manapooli_sanakirja[valu] < maara:
            return False

    return True

def muunna_mana_sanakirjaksi(mana):
    sanakirja = {}

    osat = mana.split()
    for i in range(0, len(osat), 2):
        valu = muunna_valu_suomenkieliseksi(osat[i])
        maara = int(osat[i+1])
        sanakirja[valu] = maara

    return sanakirja

def muunna_valu_suomenkieliseksi(valu):
    if valu == "r":
        return "punainen"
    elif valu == "g":
        return "vihreä"
    elif valu == "u":
        return "sininen"
    elif valu == "b":
        return "musta"
    elif valu == "w":
        return "valkoinen"
    else:
        return "neutraali"

manapooli_str = input("Syötä manapoolin valu- ja määrätiedot välilyönnillä erotettuna (esim. neutraali 3 punainen 2): ")
kortin_mana_str = input("Syötä kortin manan valu- ja määrätiedot välilyönnillä erotettuna (esim. neutraali 2 punainen 2): ")

if tarkista_mana(manapooli_str, kortin_mana_str):
    print("Sinulla on tarpeeksi manaa!")
else:
    print("Sinulla ei ole tarpeeksi manaa!")