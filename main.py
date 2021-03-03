import random

liste_nom = [
    {"nom": "armoire", "genre": "f"},
    {"nom": "clé", "genre": "f"},
    {"nom": "porte", "genre": "f"},
    {"nom": "sonette", "genre": "f"},
    {"nom": "lavabo", "genre": "m"},
    {"nom": "allumette", "genre": "f"},
    {"nom": "anniversaire", "genre": "m"},
    {"nom": "appétit", "genre": "m"},
    {"nom": "beurre", "genre": "m"},
    {"nom": "coquille", "genre": "f"},
    {"nom": "crêpe", "genre": "f"},
    {"nom": "marionnette", "genre": "f"},
    {"nom": "marteau", "genre": "m"},
    {"nom": "métal", "genre": "m"},
    {"nom": "mètre", "genre": "m"},
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


def nouvelle_phrase():
    """Retourne une phrase selon une structure.

    Args:
        nombre_nom: Le nombre de nom

    Returns:
        Une phrase.
    """
    dict_nom = random.choice(liste_nom)  # Retourne un nom au hasard dans la liste
    nom = dict_nom["nom"]  # prend l'attribut nom du dict
    det = nom_vers_determinant(dict_nom)  # retourne un dét du même genre
    verbe = groupe_verbal()
    phrase = "{} {} {}".format(det, nom, verbe)
    return phrase


def groupe_nominal():
    """Création d'un groupe nominal à partir d'une liste de dictionnaires contenant des noms (noyaux). On détermine le déterminant par la suite et si on ajoute un complément.

    Returns:
        Un groupe nominal.
    """
    dict_nom = random.choice(liste_nom)
    noyau = dict_nom["nom"]
    determinant = nom_vers_determinant(dict_nom)
    expansion = nom_vers_adjectif(dict_nom)
    if len(expansion) > 5:
        # Si adjectif long on le met après le noyau
        groupe_nominal = "{} {} {}".format(determinant, noyau, expansion)
    else:
        # Si adjectif court on le met avant le noyau
        groupe_nominal = "{} {} {}".format(determinant, expansion, noyau)

    return groupe_nominal

def groupe_verbal():
    """Création d'un groupe verbal

    Returns:
        un groupe verbal
    """
    # # complement_direct = [
    #     "",
    #     groupe_nominal(),
    #     pronom(),
    #     groupe_verbal_infinitif(),
    #     subordonnee_completive(),
    # ]  # complément direct ou non
    # complement_indirect = []
    # avec_attribut = []
    # avec_modificateur = []

    noyau = random.choice(liste_verbe)
    pronom = random.choice(["je", "tu", "il", "elle", "nous", "vous", "ils", "elles"])

    groupe_verbal = "{} {} {}".format(pronom, noyau, groupe_nominal())
    return groupe_verbal


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
    print(groupe_verbal())
    # print(nouvelle_phrase() + ",\n" + nouvelle_phrase() + ",\n" + nouvelle_phrase()+ ",\n" + nouvelle_phrase())
