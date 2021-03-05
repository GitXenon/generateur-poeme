import random

liste_nom = [
    {"nom": "rime", "genre": "m", "rime": "ime"},
    {"nom": "crime", "genre": "m", "rime": "ime"},
    {"nom": "prime", "genre": "f", "rime": "ime"},
    {"nom": "déprime", "genre": "f", "rime": "ime"},
    {"nom": "intérim", "genre": "m", "rime": "ime"},
    {"nom": "gym", "genre": "m", "rime": "ime"},
    {"nom": "lime", "genre": "f", "rime": "ime"},
    {"nom": "cybercrime", "genre": "m", "rime": "ime"},
    {"nom": "abime", "genre": "m", "rime": "ime"},
    {"nom": "enzyme", "genre": "f", "rime": "ime"},
    {"nom": "régime", "genre": "m", "rime": "ime"},
    {"nom": "estime", "genre": "f", "rime": "ime"},
    {"nom": "anonyme", "genre": "m", "rime": "ime"},
    {"nom": "victime", "genre": "f", "rime": "ime"},
    {"nom": "sublime", "genre": "m", "rime": "ime"},
    {"nom": "synonyme", "genre": "m", "rime": "ime"},
    {"nom": "acronyme", "genre": "f", "rime": "ime"},
    {"nom": "laid", "genre": "m", "rime": "ait"},
    {"nom": "plaie", "genre": "f", "rime": "ait"},
    {"nom": "volet", "genre": "m", "rime": "ait"},
    {"nom": "reflet", "genre": "m", "rime": "ait"},
    {"nom": "poulet", "genre": "m", "rime": "ait"},
    {"nom": "anglais", "genre": "m", "rime": "ait"},
    {"nom": "français", "genre": "m", "rime": "ait"},
    {"nom": "ballet", "genre": "m", "rime": "ait"},
    {"nom": "valet", "genre": "m", "rime": "ait"},
    {"nom": "gilet", "genre": "m", "rime": "ait"},
    {"nom": "galet", "genre": "m", "rime": "ait"},
    {"nom": "mollet", "genre": "m", "rime": "ait"},
    {"nom": "palais", "genre": "m", "rime": "ait"},
    {"nom": "couplet", "genre": "m", "rime": "ait"},
]

liste_verbe = [
    "apporte",
    "entre",
    "s'installe",
    "agace",
    "gratte",
    "vit",
    "grandit",
    "boit",
    "plante",
]
liste_determinant_feminin = ["une", "la", "ta"]
liste_determinant_masculin = ["un", "le", "ton"]
liste_adjectif_feminin = [
    "adroite",
    "difficile",
    "dure",
    "facile",
    "lisse",
    "maladroite",
    "pointue",
    "rugueuse",
    "tordue",
    "absente",
    "assise",
    "basse",
    "couchée",
    "haute",
    "présente",
    "blonde",
    "brune",
    "calme",
    "curieuse",
    "différente",
    "douce",
    "énervée",
    "gentille",
    "grande",
    "handicapée",
    "inséparable",
    "jalouse",
    "moyenne",
    "muette",
    "noire",
    "nouvelle",
    "petite",
    "polie",
    "propre",
    "rousse",
    "sage",
    "sale",
    "sérieuse",
    "sourde",
    "tranquille",
]
liste_adjectif_masculin = [
    "adroit",
    "difficile",
    "dur",
    "facile",
    "lisse",
    "maladroit",
    "pointu",
    "rugueux",
    "tordu",
    "absent",
    "assis",
    "bas",
    "couché",
    "haut",
    "présent",
    "blond",
    "brun",
    "calme",
    "curieux",
    "différent",
    "doux",
    "énervé",
    "gentil",
    "grand",
    "handicapé",
    "inséparable",
    "jaloux",
    "moyen",
    "muet",
    "noir",
    "nouveau",
    "petit",
    "poli",
    "propre",
    "roux",
    "sage",
    "sale",
    "sérieux",
    "sourd",
    "tranquille",
]


def rime_AABB():
    """Retourne un poème avec la structure de rime AABB

    Returns:
        structure_AABB: Un court poème formatté avec la structure de rime AABB.
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
    structure_AABB = "{}\n{}\n{}\n{}\n".format(
        groupe_nominal(premier_A),
        groupe_nominal(deuxieme_A),
        groupe_nominal(premier_B),
        groupe_nominal(deuxieme_B),
    )
    return structure_AABB


def groupe_nominal(dict_nom=random.choice(liste_nom)):
    """Création d'un groupe nominal à partir d'une liste de dictionnaires contenant des noms (noyaux).
    On détermine le déterminant par la suite et si on ajoute un complément.

    Args:
        dict_nom: Un dictionnaire contenant un nom. Par défaut on choisit un dictionnaire au hasard dans la liste.

    Returns:
        Un groupe nominal.
    """
    noyau = dict_nom["nom"]
    determinant = nom_vers_determinant(dict_nom)

    determinant = verifier_mot_debute_voyelle(noyau, determinant)

    if determinant[-1] == "'":
        # Dernier caractère est un apostrophe donc on doit coller déterminant avec noyau
        groupe_nominal = "{}{}".format(determinant, noyau)
    else:
        groupe_nominal = "{} {}".format(determinant, noyau)
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


def groupe_pronom():
    """Création d'un pronom

    Returns:
        Un pronom et son extension
    """
    pronom = random.choice(["je", "tu", "il", "elle", "nous", "vous", "ils", "elles"])
    groupe_pronom = "{}, {},".format(pronom, groupe_nominal())
    return groupe_pronom


def nom_vers_determinant(dict_nom):
    """Retourne un déterminant du même genre que le nom.

    Args:
        dict_nom: Un dictionnaire contenant un nom et son genre.

    Returns:
        Un déterminant du même genre que le nom passé en argument.
    """
    if dict_nom["genre"] == "f":
        determinant = random.choice(liste_determinant_feminin)
    else:
        determinant = random.choice(liste_determinant_masculin)
    return determinant


def verifier_mot_debute_voyelle(nom, determinant):
    """Retourne un déterminant selon si le mot passé en argument commence par une voyelle

    Returns:
        determinant
    """
    if nom[0] == ("a" or "e" or "i" or "o" or "u" or "h"):
        if determinant == "la" or determinant == "le":
            determinant = "l'"
        if determinant == "ta":
            determinant == "ton"
    return determinant


def nom_vers_adjectif(dict_nom):
    """Retourne un adjectif du même genre que le nom.

    Args:
        dict_nom: Un dictionnaire contenant un nom et son genre.

    Returns:
        Un adjectif du même genre que le nom passé en argument.
    """
    if dict_nom["genre"] == "f":
        adjectif = random.choice(liste_adjectif_feminin)
    else:
        adjectif = random.choice(liste_adjectif_masculin)
    return adjectif


if __name__ == "__main__":
    print(rime_AABB())
