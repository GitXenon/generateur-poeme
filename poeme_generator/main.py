import re, os, random


def retourner_mot(categorie):
    """Retourne un mot du lexique selon une catégorie donnée

    Args:
        categorie (str): La catégorie désirée du mot

    Returns:
        resultat_mot (str): une string contenant un mot
    """
    if categorie == "nom":
        regex = r"^([a-z]+\b\s*)+ NN$"
    if categorie == "det":
        regex = r"^([a-z]+\b\s*)+ DT$"
    if categorie == "adj":
        regex = r"^([a-z]+\b\s*)+ JJ$"
    if categorie == "pron":
        regex = r"^([a-z]+\b\s*)+ PRP$"
    if categorie == "adv":
        regex = r"^([a-z]+\b\s*)+ RB$"
    if categorie == "vb":
        regex = r"^([a-z]+\b\s*)+ VB$"
    if categorie == "pr":
        regex = r"^([a-z]+\b\s*)+ IN$"

    lexicon = open("fr-lexicon.txt", encoding="UTF-8")
    lexicon_text = lexicon.read()

    list_mots = re.findall(regex, lexicon_text, re.MULTILINE)
    try:
        resultat_mot = random.choice(list_mots)
    except IndexError:
        print(list_mots, categorie)
        quit()

    return resultat_mot


def genere_grammaire():
    """On réitère jusqu'à temps que tous les groupes de mot soit transformé en categorie lexical

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

def categorie_lexical_vers_mots(chaine_lexical):
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

    phrase = chaine_lexical
    return phrase


if __name__ == "__main__":
    os.chdir("./poeme_generator")
    random.seed()

    chaine_terminaux = genere_grammaire()
    phrase = categorie_lexical_vers_mots(chaine_terminaux)

    print(phrase)
    print(categorie_lexical_vers_mots(genere_grammaire()))
    print(categorie_lexical_vers_mots(genere_grammaire()))
    print(categorie_lexical_vers_mots(genere_grammaire()))
    # resultat_det = retourner_mot("det")
    # resultat_nom = retourner_mot("nom")
    # resultat_adj = retourner_mot("adj")

    # resultat_det = pluralize(resultat_det, custom=plural_determinant)
    # resultat_nom = pluralize(resultat_nom)
    # resultat_adj = pluralize(resultat_adj)

    # print("{} {} {}".format(resultat_det, resultat_nom, resultat_adj))
