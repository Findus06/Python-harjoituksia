def tarkista_mana(manapooli, kortin_mana):
    manapooli_sanakirja = muunna_mana_sanakirjaksi(manapooli)
    kortin_mana_sanakirja = muunna_mana_sanakirjaksi(kortin_mana)

    for valu, maara in kortin_mana_sanakirja.items():
        if valu not in manapooli_sanakirja or manapooli_sanakirja[valu] < maara:
            if "neutraali" not in manapooli_sanakirja or manapooli_sanakirja["neutraali"] < (maara - manapooli_sanakirja.get(valu, 0)):
                return False
            else:
                manapooli_sanakirja["neutraali"] -= (maara - manapooli_sanakirja.get(valu, 0))
                manapooli_sanakirja[valu] = max(0, manapooli_sanakirja[valu] - maara)

    return True

def muunna_mana_sanakirjaksi(mana):
    sanakirja = {"neutraali": 0}

    while mana:
        if mana[0].isdigit():
            maara = ""
            while mana and mana[0].isdigit():
                maara += mana[0]
                mana = mana[1:]
            maara = int(maara)
        else:
            maara = 1

        if not mana:
            break

        if mana[0] == "r":
            valu = "punainen"
        elif mana[0] == "g":
            valu = "vihreä"
        elif mana[0] == "u":
            valu = "sininen"
        elif mana[0] == "b":
            valu = "musta"
        elif mana[0] == "w":
            valu = "valkoinen"
        else:
            valu = "neutraali"

        mana = mana[1:]

        if valu in sanakirja:
            sanakirja[valu] += maara
        else:
            sanakirja[valu] = maara

    return sanakirja



manapooli_str = input("Syötä manapoolin valu- ja määrätiedot välilyönnillä erotettuna (esim. 2 r r): ")
kortin_mana_str = input("Syötä kortin manan valu- ja määrätiedot välilyönnillä erotettuna (esim. 2 r r): ")

if tarkista_mana(manapooli_str, kortin_mana_str):
    print("Sinulla on tarpeeksi manaa!")
else:
    print("Sinulla ei ole tarpeeksi manaa!")
