import re, os, random


def retourner_mot(categorie):
    """Retourne un mot du lexique selon une catégorie donnée

    Args:
        categorie (str): La catégorie désirée du mot

    Returns:
        resultat_mot (str): une string contenant un mot
    """
    if categorie == "nom":
        regex = r"^([a-z]+\b\s*)+ (NN)$"
    if categorie == "det":
        regex = r"^([a-z]+\b\s*)+ (DT|IN)$"
    if categorie == "adj":
        regex = r"^([a-z]+\b\s*)+ (JJ)$"
    if categorie == "pron":
        regex = r"^([a-z]+\b\s*)+ (PRP)$"
    if categorie == "adv":
        regex = r"^([a-z]+\b\s*)+ (RB)$"
    if categorie == "vb":
        regex = r"^([a-z]+\b\s*)+ (VB)$"
    if categorie == "pr":
        regex = r"^([a-z]+\b\s*)+ (IN)$"

    lexicon = open("fr-lexicon.txt", encoding="UTF-8")
    lexicon_text = lexicon.read()

    list_mots = re.findall(regex, lexicon_text, re.MULTILINE)
    try:
        tuple_resultat_mot = random.choice(list_mots)
    except IndexError:
        print(list_mots, categorie)
        quit()

    return tuple_resultat_mot[0]


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
    while "_dt" in chaine_lexical:
        chaine_lexical = chaine_lexical.replace("_dt", retourner_mot("det") + " ", 1)
    while "_pn" in chaine_lexical:
        chaine_lexical = chaine_lexical.replace(
            "_pn", retourner_mot("pron") + " ", 1
        )
    while "_nn" in chaine_lexical:
        chaine_lexical = chaine_lexical.replace("_nn", retourner_mot("nom") + " ", 1)
    while "_vb" in chaine_lexical:
        chaine_lexical = chaine_lexical.replace("_vb", retourner_mot("vb") + " ", 1)
    while "_pr" in chaine_lexical:
        chaine_lexical = chaine_lexical.replace("_pr", retourner_mot("pr") + " ", 1)
    while "_adj" in chaine_lexical:
        chaine_lexical = chaine_lexical.replace("_adj", retourner_mot("adj") + " ", 1)

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
    print("1. Générer un poème randomisé\n2. Générer un poème à partir d'une structure déjà établis\n0. Quitter\n")
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
        else:
            print("Ceci n'est pas une option!")

