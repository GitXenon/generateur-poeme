import random
import secrets

from tinydb import TinyDB, Query

import wikitionnaire

db = TinyDB('db.json')

#TODO: Beau / bel. Devant un nom masculin commençant par une voyelle ou un h muet, on emploie la forme bel 

def initiation_rime():
    """Initie une liste de mots rimant pour être utilisée dans un poème.

    Returns:
        premier_A: dict contenant un nom qui rime avec deuxieme_A
        deuxieme_A: dict contenant un nom qui rime avec premier_A
        premier_B: dict contenant un nom qui rime avec deuxieme_B
        deuxieme_B: dict contenant un nom qui rime avec premier_B
    """
    liste_nom_rimant_A = []
    liste_nom_rimant_B = []
    premier_A = random.choice(liste_nom)
    premier_B = random.choice(liste_nom)

    while premier_A["rime"] == premier_B["rime"]:
        premier_B = random.choice(liste_nom)
    for i in range(len(liste_nom)):
        if liste_nom[i]["rime"] == premier_A["rime"]:
            liste_nom_rimant_A.append(liste_nom[i])
        if liste_nom[i]["rime"] == premier_B["rime"]:
            liste_nom_rimant_B.append(liste_nom[i])
    deuxieme_A = random.choice(liste_nom_rimant_A)
    deuxieme_B = random.choice(liste_nom_rimant_B)

    return premier_A, deuxieme_A, premier_B, deuxieme_B

def rime_AABB():
    """Retourne un poème avec la structure de rime AABB

    Returns:
        structure_AABB: Un court poème formatté avec la structure de rime AABB.
    """
    premier_A, deuxieme_A, premier_B, deuxieme_B = initiation_rime()
    structure_AABB = "{}\n{}\n{}\n{}\n".format(
        groupe_verbal_avec_preposition(premier_A),
        groupe_nominal_adjectif(deuxieme_A).capitalize(),
        groupe_verbal_avec_preposition(premier_B),
        groupe_nominal_adjectif(deuxieme_B).capitalize(),
    )
    return structure_AABB

def rime_ABAB():
    """Retourne un poème avec la structure de rime ABAB

    Returns:
        structure_ABAB: Un court poème formatté avec la structure de rime ABAB.
    """
    premier_A, deuxieme_A, premier_B, deuxieme_B = initiation_rime()
    structure_ABAB = "{}\n{}\n{}\n{}\n".format(
        groupe_verbal_avec_preposition(premier_A),
        groupe_nominal_adjectif(premier_B).capitalize(),
        groupe_verbal_avec_preposition(deuxieme_A),
        groupe_nominal_adjectif(deuxieme_B).capitalize(),
    )
    return structure_ABAB

def rime_ABBA():
    """Retourne un poème avec la structure de rime ABBA

    Returns:
        structure_AABB: Un court poème formatté avec la structure de rime AABB.
    """
    premier_A, deuxieme_A, premier_B, deuxieme_B = initiation_rime()
    structure_ABBA = "{}\n{}\n{}\n{}\n".format(
        groupe_verbal_avec_preposition(premier_A),
        groupe_nominal_adjectif(premier_B).capitalize(),
        groupe_verbal_avec_preposition(deuxieme_B),
        groupe_nominal_adjectif(deuxieme_A).capitalize(),
    )
    return structure_ABBA

def groupe_nominal(dict_determinant, dict_nom):
    """Création d'un groupe nominal à partir d'une liste de dictionnaires contenant des noms (noyaux).
    On détermine le déterminant par la suite et si on ajoute un complément.

    Args:
        dict_determinant (dict): Un dictionnaire contenant tous les nombres et genre d'un déterminant.
        dict_nom (dict): Un dictionnaire contenant un nom et ses attributs.

    Returns:
        groupe_nominal (str): Un groupe nominal.
    """
    noyau = dict_nom['mot']
    genre_nombre = dict_nom['genre'] + dict_nom['nombre']
    dict_determinant = dict_determinant[genre_nombre]
    determinant = dict_determinant['mot']
    # Doit vérifier si déterminant est même genre que nom.
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
    noyau = dict_nom['mot']
    genre_nombre = dict_nom['genre'] + dict_nom['nombre']
    dict_determinant = dict_determinant[genre_nombre]
    dict_adjectif = dict_adjectif[genre_nombre]
    adjectif = dict_adjectif['mot']
    determinant = dict_determinant['mot']
    # Doit vérifier si déterminant est même genre que nom.
    determinant = verifier_mot_debute_voyelle(noyau, determinant)

    if determinant[-1] == "'":
        # Dernier caractère est un apostrophe donc on doit coller déterminant avec noyau
        groupe_nominal = "{}{} {}".format(determinant, noyau, adjectif)
    else:
        groupe_nominal = "{} {} {}".format(determinant, noyau, adjectif)
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

def nom_vers_determinant(dict_nom):
    """Retourne un déterminant du même genre que le nom.

    Args:
        dict_nom: Un dictionnaire contenant un nom et son genre.

    Returns:
        Un déterminant du même genre que le nom passé en argument.
    """
    dict_determinant = random.choice(liste_determinant)
    for k in dict_determinant:
        if k == dict_nom["genre"]:
            determinant = dict_determinant[k]
    return determinant

def verifier_mot_debute_voyelle(nom, determinant):
    """Retourne un déterminant selon si le mot passé en argument commence par une voyelle

    Returns:
        determinant (str): Un déterminant.
    """
    if nom[0] == ("a" or "e" or "i" or "o" or "u" or "h" or "é"):
        if determinant == "la" or determinant == "le":
            determinant = "l'"
        if determinant == "ta":
            determinant == "ton"
        if determinant == "ma":
            determinant = "mon"
    return determinant

def nom_vers_adjectif(dict_nom):
    """Retourne un adjectif du même genre que le nom.

    Args:
        dict_nom (dict): Un dictionnaire contenant un nom et son genre.

    Returns:
        adjectif (str): Un adjectif du même genre que le nom passé en argument.
    """
    dict_adjectif = random.choice(liste_adjectif)
    for k in dict_adjectif:
        if k == dict_nom["genre"]:
            adjectif = dict_adjectif[k]
    return adjectif

def nombre_syllables(mot):
    """Retourne le nombre de syllables dans un mot passé en argument.

    Args:
        mot (str): Un mot.
    
    Returns:
        num_syl (int): Le nombre de syllables dans le mot.
    """
    liste_voyelle = ['a', 'e', 'i', 'o', 'u', 'y', 'é']
    num_syl = 1

    for i in range(len(mot)):
        if mot[i] not in liste_voyelle:
            if i-1 >= 0:
                if mot[i-1] in liste_voyelle:
                    j = i+1
                    while(j < len(mot)):
                        if (mot[i+1] == 'r' and mot[i] != 'r') or (mot[i+1] == 'l' and mot[i] != 'l'):
                            break
                        if mot[j] in liste_voyelle:
                            num_syl = num_syl+ 1
                            break
                        else:
                            j=j+1
    return num_syl

if __name__ == "__main__":
    TableNom = db.table('nom')
    TableAdj = db.table('adjectif')
    TableDet = db.table('determinant')

    nom_int = secrets.randbelow(len(TableNom)-1)+1
    adj_int = secrets.randbelow(len(TableAdj)-1)+1
    det_int = secrets.randbelow(len(TableDet)-1)+1

    dict_nom = TableNom.all()[nom_int]
    dict_adj = TableAdj.all()[adj_int]
    dict_det = TableDet.all()[det_int]

    GNadj = groupe_nominal_adjectif(dict_det, dict_nom, dict_adj)
    print(GNadj)
    # print("Bienvenue au générateur de poème.\n-------------------\n\n")
    # print("Veuillez prendre une option parmis les suivantes:\n1.AABB\n2.ABBA\n3.ABAB\n")
    # choix = input()
    # if choix == "1":
    #     print(rime_AABB())
    # if choix == "2":
    #     print(rime_ABBA())
    # if choix == "3":
    #     print(rime_ABAB())