import random
import secrets
import re
import logging

from tinydb import TinyDB, Query

# TODO: Beau / bel. Devant un nom masculin commençant par une voyelle ou un h muet, on emploie la forme bel


def groupe_nominal(dict_determinant, dict_nom):
    """Création d'un groupe nominal à partir d'une liste de dictionnaires contenant des noms (noyaux).
    On détermine le déterminant par la suite et si on ajoute un complément.

    Args:
        dict_determinant (dict): Un dictionnaire contenant tous les nombres et genre d'un déterminant.
        dict_nom (dict): Un dictionnaire contenant un nom et ses attributs.

    Returns:
        groupe_nominal (str): Un groupe nominal.
    """
    noyau = dict_nom["mot"]
    genre_nombre = dict_nom["genre"] + dict_nom["nombre"]

    dict_determinant = dict_determinant[genre_nombre]
    determinant = dict_determinant["mot"]
    determinant = verifier_mot_debute_voyelle(noyau, determinant)

    if determinant[-1] == "'":
        # Dernier caractère est un apostrophe donc on doit coller déterminant avec noyau
        groupe_nominal = "{}{}".format(determinant, noyau)
    else:
        groupe_nominal = "{} {}".format(determinant, noyau)
    return groupe_nominal


def groupe_nominal_adjectif(dict_determinant, dict_nom, dict_adjectif):
    """Création d'un groupe nominal avec expansion à partir d'une liste de dictionnaires contenant des noms (noyaux).
    On détermine le déterminant par la suite et si on ajoute un complément.

    Args:
        dict_determinant (dict): Un dictionnaire contenant tous les nombres et genre d'un déterminant.
        dict_nom (dict): Un dictionnaire contenant un nom et ses attributs.

    Returns:
        groupe_nominal (str): Un groupe nominal.
    """
    noyau = dict_nom["mot"]
    genre_nombre = dict_nom["genre"] + dict_nom["nombre"]

    dict_determinant = dict_determinant[genre_nombre]
    determinant = dict_determinant["mot"]

    dict_adjectif = dict_adjectif[genre_nombre]
    adjectif = dict_adjectif["mot"]

    determinant = verifier_mot_debute_voyelle(adjectif, determinant)
    if determinant[-1] == "'":
        # Dernier caractère est un apostrophe donc on doit coller déterminant avec noyau
        groupe_nominal = "{}{} {}".format(determinant, adjectif, noyau)
    else:
        groupe_nominal = "{} {} {}".format(determinant, adjectif, noyau)
    return groupe_nominal


def groupe_verbal():
    """Création d'un groupe verbal

    Returns:
        un groupe verbal
    """
    noyau = random.choice(liste_verbe)
    pronom = random.choice(["je", "tu", "il", "elle", "nous", "vous", "ils", "elles"])

    groupe_verbal = "{} {} {}".format(pronom, groupe_pronom(), noyau)
    return groupe_verbal


def groupe_verbal_avec_preposition(Gn=None):
    """Création d'un groupe verbal avec expansion prepositionnel

    Returns:
        un groupe verbal + Gprep
    """
    noyau = random.choice(liste_verbe)
    Gprep = groupe_prepositionnel()
    if Gn is None:
        Gn = groupe_nominal()
    else:
        Gn = groupe_nominal(Gn)
    groupe_verbal = "{} {} {}".format(Gprep, noyau, Gn)
    groupe_verbal = groupe_verbal.capitalize()
    return groupe_verbal


def groupe_pronom():
    """Création d'un pronom

    Returns:
        Un pronom et son extension
    """
    pronom = random.choice(["je", "tu", "il", "elle", "nous", "vous", "ils", "elles"])
    groupe_pronom = "{}, {},".format(pronom, groupe_nominal())
    return groupe_pronom


def groupe_prepositionnel():
    """Création d'un groupe prepositionnel

    Returns:
        Un groupe prépositionnel avec son expansion groupe du nom.
    """
    preposition = random.choice(liste_preposition)
    gn = groupe_nominal()
    groupe_prepositionnel = "{} {}".format(preposition, gn)
    return groupe_prepositionnel


def verifier_mot_debute_voyelle(nom, determinant):
    """Retourne un déterminant selon si le mot passé en argument commence par une voyelle

    Returns:
        determinant (str): Un déterminant.
    """
    if nom[0] == ("a" or "e" or "i" or "o" or "u" or "h" or "é"):
        if determinant == ("la" or "La" or "Le" or "le"):
            determinant = "l'"
        if determinant == "ta":
            determinant == "ton"
        if determinant == "ma":
            determinant = "mon"
    return determinant


def nombre_syllables(mot):
    """Retourne le nombre de syllables dans un mot passé en argument.

    Args:
        mot (str): Un mot.

    Returns:
        num_syl (int): Le nombre de syllables dans le mot.
    """
    liste_voyelle = ["a", "e", "i", "o", "u", "y", "é"]
    num_syl = 1

    for i in range(len(mot)):
        if mot[i] not in liste_voyelle:
            if i - 1 >= 0:
                if mot[i - 1] in liste_voyelle:
                    j = i + 1
                    while j < len(mot):
                        if (mot[i + 1] == "r" and mot[i] != "r") or (
                            mot[i + 1] == "l" and mot[i] != "l"
                        ):
                            break
                        if mot[j] in liste_voyelle:
                            num_syl = num_syl + 1
                            break
                        else:
                            j = j + 1
    return num_syl


def trouver_rime(dict_nom, table_nom):
    """Avec la phonétique API, retourne une liste de dict qui rime avec le mot passé en argument.

    Args:
        dict_nom (dict): Un dictionnaire contenant un nom.
        table_nom (table): la base de donnée avec tous les noms.

    Returns:
        liste_rimant (list): Une liste de mot qui rime avec le mot.
    """
    regex = "([\u0254\u0303|\u0069|\u0065|\u025b|\u025b\u0303|\u0153\u0303|\u0153|\u0259|\u00f8|\u0079|\u0075|\u006f|\u0254|\u0254\u0303|\u0251\u0303|\u0251|\u0061][\u006e|\u0272|\u014b|\u0261|\u006b|\u006d|\u0062|\u0070|\u0076|\u0066|\u0064|\u0074|\u0292|\u0283|\u007a|\u0073|\u0281|\u006c|\u006a]*)\\\\$"
    m = re.search(regex, dict_nom["API"])
    try:
        newRegex = m[0]
    except TypeError:
        logging.info("Aucun rime trouvé avec ce mot.")
        return table_nom
    res = "".join(
        r"\u{:04X}".format(ord(chr)) for chr in newRegex
    )  # On convertit le rime en unicode
    liste_rimant = table_nom.search(Query().API.search(res))
    return liste_rimant


if __name__ == "__main__":
    db = TinyDB("db.json")

    TableNom = db.table("nom")
    TableAdj = db.table("adjectif")
    TableDet = db.table("determinant")

    nom_int = secrets.randbelow(len(TableNom))
    adj_int = secrets.randbelow(len(TableAdj))
    det_int = secrets.randbelow(len(TableDet))

    dict_nom = TableNom.all()[nom_int]
    dict_adj = TableAdj.all()[adj_int]
    dict_det = TableDet.all()[det_int]

    ListeNom = trouver_rime(dict_nom, TableNom)

    nom_int2 = secrets.randbelow(len(ListeNom))
    adj_int2 = secrets.randbelow(len(TableAdj))
    det_int2 = secrets.randbelow(len(TableDet))

    dict_nom2 = ListeNom[nom_int2]
    dict_adj2 = TableAdj.all()[adj_int2]
    dict_det2 = TableDet.all()[det_int2]

    GNadj = groupe_nominal_adjectif(dict_det, dict_nom, dict_adj)
    GNadj2 = groupe_nominal_adjectif(dict_det2, dict_nom2, dict_adj2)
    print(GNadj.capitalize())
    print(GNadj2.capitalize())
    # print("Bienvenue au générateur de poème.\n-------------------\n\n")
    # print("Veuillez prendre une option parmis les suivantes:\n1.AABB\n2.ABBA\n3.ABAB\n")
    # choix = input()
    # if choix == "1":
    #     print(rime_AABB())
    # if choix == "2":
    #     print(rime_ABBA())
    # if choix == "3":
    #     print(rime_ABAB())
