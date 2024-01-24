def GetBool():
    global MyMoves, OpponentMoves
    
    # Tarkista, onko tarpeeksi tietoa päätöksen tekemiseen
    if len(OpponentMoves) < 2:
        return True
    
    # Analysoi tietoja ja tee päätös
    viimeisimmat_siirrot = OpponentMoves[-2:]
    if viimeisimmat_siirrot == [True, True]:
        return False
    elif viimeisimmat_siirrot == [True, False]:
        return True
    elif viimeisimmat_siirrot == [False, True]:
        return True
    elif viimeisimmat_siirrot == [False, False]:
        return False
    
    # Jos vastustaja valitsee vain yhden vaihtoehdon, valitse vastakkainen
    if OpponentMoves[-1] == OpponentMoves[-2]:
        return not OpponentMoves[-1]
    
    # Jos tietoja ei ole tarpeeksi, arvaa
    true_laskuri = OpponentMoves[-10:].count(True)
    false_laskuri = OpponentMoves[-10:].count(False)
    
    # Tee älykkäämpi päätös
    if true_laskuri > false_laskuri:
        return False
    elif true_laskuri < false_laskuri:
        return True
    else:
        return not OpponentMoves[-1]
