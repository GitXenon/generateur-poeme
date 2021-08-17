import os, random

def ouvrir_lexique():
    # TODO : changer nom variable temp
    lexique = open("Lexique383.tsv", encoding="UTF-8")
    lexique_text = lexique.read()
    temp = lexique_text.splitlines()
    index = 0
    while index < len(temp):
        temp[index] = temp[index].split("\t")
        index += 1
    return temp

def Retourner_Liste_Mot(cat_gram, genre, nombre):
    """Retourne une liste avec la catégorie grammaticale donnée
    """
    liste_cgram = []
    lexique = ouvrir_lexique()
    for x in lexique:
        if cat_gram in x[3]:
            if x[4] == genre or x[4] == "":
                if x[5] == nombre or x[5] == "":
                    liste_cgram.append(x)
    return liste_cgram

def Retourner_Verbe(conjugaison):
    liste_verbe = []
    lexique = ouvrir_lexique()
    for x in lexique:
        if "VER" in x[3]:
            if conjugaison in x[10]:
                liste_verbe.append(x)
    verbe = random.choice(liste_verbe)
    return verbe[0]

def Retourner_Mot(liste_cgram):
    random.seed()
    return random.choice(liste_cgram)[0]

def genere_grammaire():
    """On réitère jusqu'à temps que tous les groupes de mot soit transformé en categorie lexical
        S: une phrase
        GN: un groupe du nom
        GV: un groupe verbal
        GPR: un groupe pronominal
        _dt: déterminant
        _pn: pronom TODO
        _nn: nom
        _vb: verbe
        _pr: pronom


    Returns:
        symbole_non_terminal (str): Une chaîne de catégories lexical
    """
    symbole_non_terminal = "S"

    while not symbole_non_terminal.islower():
        remplacement_S = ["GN", "GV"]
        remplacement_GN = ["_pn", "_dt_nn", "GNGN", "GNGPR"]
        remplacement_GV = ["GN_vb", "_pn_vb", "_dt_nn_vb", "GVGN", "GV_pn", "GVGPR", "GPRGV"]
        remplacement_GPR = ["_prGN", "_pr_pn"]
        while "S" in symbole_non_terminal:
            symbole_non_terminal = symbole_non_terminal.replace(
                "S", random.choice(remplacement_S), 1
            )
        while "GN" in symbole_non_terminal:
            symbole_non_terminal = symbole_non_terminal.replace(
                "GN", random.choice(remplacement_GN), 1
            )
        while "GV" in symbole_non_terminal:
            symbole_non_terminal = symbole_non_terminal.replace(
                "GV", random.choice(remplacement_GV), 1
            )
        while "GPR" in symbole_non_terminal:
            symbole_non_terminal = symbole_non_terminal.replace(
                "GPR", random.choice(remplacement_GPR), 1
            )

    return symbole_non_terminal

def chaine_lexical_vers_mots(chaine_lexical):
    """Remplace les symboles des catégories en un symbole terminal (un mot).
    
    Args:
        chaine_lexical (str): une chaîne de catégorie lexical
    Returns:
        phrase (str): une série de mots
    """
    # On choisit un genre et un nombre au hasard
    liste_genre = ["m", "f"]
    liste_nombre = ["s", "p"]
    random.seed()
    genre = random.choice(liste_genre)
    random.seed()
    nombre = random.choice(liste_nombre)
    print(genre, nombre)

    liste_determinant = Retourner_Liste_Mot("ART", genre, nombre)
    liste_nom = Retourner_Liste_Mot("NOM", genre, nombre)
    liste_adjectif = Retourner_Liste_Mot("ADJ", genre, nombre)
    liste_verbe = Retourner_Liste_Mot("VER", genre, nombre)
    liste_pronom = Retourner_Liste_Mot("PRO", genre, nombre)

    while "_dt" in chaine_lexical:
        random.seed()
        chaine_lexical = chaine_lexical.replace("_dt", Retourner_Mot(liste_determinant) + " ", 1)
    while "_pn" in chaine_lexical:
        random.seed()
        chaine_lexical = chaine_lexical.replace(
            "_pn", Retourner_Mot(liste_determinant) + " ", 1
        )
    while "_nn" in chaine_lexical:
        random.seed()
        chaine_lexical = chaine_lexical.replace("_nn", Retourner_Mot(liste_nom) + " ", 1)
    while "_vb" in chaine_lexical:
        random.seed()
        chaine_lexical = chaine_lexical.replace("_vb", Retourner_Mot(liste_verbe) + " ", 1)
    while "_pr" in chaine_lexical:
        random.seed()
        chaine_lexical = chaine_lexical.replace("_pr", Retourner_Mot(liste_pronom) + " ", 1)
    while "_adj" in chaine_lexical:
        random.seed()
        chaine_lexical = chaine_lexical.replace("_adj", Retourner_Mot(liste_adjectif) + " ", 1)

    phrase = chaine_lexical
    return phrase


if __name__ == "__main__":
    os.chdir("./poeme_generator")
    print("""---------------------------------------                                   
 ___ ___ ___ ___ ___ ___ ___ _____ ___ 
| . | -_|   | . | . | . | -_|     | -_|
|_  |___|_|_|___|  _|___|___|_|_|_|___|
|___|           |_|                    
---------------------------------------""")
    print("Faites un choix parmis les options suivantes:")
    print("1. Générer un poème randomisé\n2. Générer un poème à partir d'une structure déjà établis\n3. Fill-in the blank\n0. Quitter\n")
    while True:
        choix_utilisateur = input()
        if choix_utilisateur == "0":
            quit()
        if choix_utilisateur == "1":
            poeme = ""
            for i in range(4):
                random.seed()
                symbole = genere_grammaire()
                poeme_temp = chaine_lexical_vers_mots(symbole)
                poeme_temp += "\n"
                poeme += poeme_temp
            print(poeme)
        elif choix_utilisateur == "2":
            random.seed()
            liste_structure_poeme = ["_dt_nn", "_dt_nn_adj"]
            chaine_lex = random.choice(liste_structure_poeme)
            poeme = ""
            for i in range(4):
                poeme_temp = chaine_lexical_vers_mots(chaine_lex)
                poeme_temp.capitalize()
                poeme_temp += "\n"
                poeme += poeme_temp
            print(poeme.capitalize())
        elif choix_utilisateur == "3":
            print("Je vais essayer de décrire,\nCe cadeau ", end="")
            liste_adjectif_masculin_singulier = Retourner_Liste_Mot("ADJ", "m", "s")
            liste_adjectif_feminin_singulier = Retourner_Liste_Mot("ADJ", "f", "s")
            print(Retourner_Mot(liste_adjectif_masculin_singulier), end="")
            liste_nom_masculin_singulier = Retourner_Liste_Mot("NOM", "m", "s")
            liste_nom_feminin_singulier = Retourner_Liste_Mot("NOM", "f", "s")
            liste_nom_feminin_pluriel = Retourner_Liste_Mot("NOM", "f", "p")
            print(", ce " + Retourner_Mot(liste_nom_masculin_singulier) + ".")
            print("💛")
            print("C'est une " + Retourner_Mot(liste_nom_feminin_singulier) + ", un "+ Retourner_Mot(liste_nom_masculin_singulier) + " " +Retourner_Mot(liste_adjectif_masculin_singulier))
            print(Retourner_Verbe("inf") + " et " + Retourner_Verbe("inf") + " tour à tour.\n💛")
            print("Se " + Retourner_Verbe("inf") + " et "+ Retourner_Verbe("inf") +" et " + Retourner_Verbe("inf"))
            print("Et avoir de la "+Retourner_Mot(liste_nom_feminin_singulier)+". c'est " + Retourner_Verbe("inf")+".\n💛")
            print("C'est un ensemble de "+ Retourner_Mot(liste_nom_masculin_singulier)+" et de " + Retourner_Mot(liste_nom_masculin_singulier))
            print("C'est le battement du "+Retourner_Mot(liste_nom_masculin_singulier)+" dans la "+Retourner_Mot(liste_nom_feminin_singulier)+".\n💛")
            print("Un "+Retourner_Mot(liste_adjectif_masculin_singulier)+ " " + Retourner_Mot(liste_nom_masculin_singulier)+", et des " + Retourner_Mot(liste_nom_feminin_pluriel))
            print("Un "+Retourner_Mot(liste_nom_masculin_singulier)+", et une "+Retourner_Mot(liste_adjectif_feminin_singulier) +" "+ Retourner_Mot(liste_nom_feminin_singulier)+".")
        else:
            print("Ceci n'est pas une option!")

