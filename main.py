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
    {"nom": "amour", "genre": "f", "rime": "our"},
    {"nom": "moere", "genre": "f", "rime": "our"},
    {"nom": "tourd", "genre": "m", "rime": "our"},
    {"nom": "bourre", "genre": "m", "rime": "our"},
    {"nom": "rebours", "genre": "m", "rime": "our"},
    {"nom": "atour", "genre": "m", "rime": "our"},
    {"nom": "séjour", "genre": "m", "rime": "our"},
    {"nom": "discours", "genre": "m", "rime": "our"},
    {"nom": "parcours", "genre": "m", "rime": "our"},
    {"nom": "retour", "genre": "m", "rime": "our"},
    {"nom": "jour", "genre": "m", "rime": "our"},
    {"nom": "cour", "genre": "f", "rime": "our"},
    {"nom": "four", "genre": "m", "rime": "our"},
    {"nom": "sourd", "genre": "m", "rime": "our"},
    {"nom": "secours", "genre": "m", "rime": "our"},
    {"nom": "concours", "genre": "m", "rime": "our"},
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

liste_determinant = [
    {"m":"un", "f":"une"},
    {"m":"le", "f":"la"},
    {"m":"ton", "f":"ta"},
    {"m":"mon", "f":"ma"},
]

liste_adjectif = [
    {"m":"oblitérateur", "f":"oblitératrice"},
    {"m":"vérificatif", "f":"vérificative"},
    {"m":"congratulatoire", "f":"congratulatoire"},
    {"m":"énumérateur", "f":"énumératrice"},
    {"m":"apollinarien", "f":"apollinarienne"},
    {"m":"sardanapalesque", "f":"sardanapalesque"},
    {"m":"transfigurateur", "f":"transfiguratrice"},
    {"m":"émerillonné", "f":"émerillonnée"},
    {"m":"vivificateur", "f":"vivificatrice"},
    {"m":"résurrectionnel", "f":"résurrectionnelle"},
    {"m":"vociférateur", "f":"vocifératrice"},
    {"m":"caméléonesque", "f":"caméléonesque"},
    {"m":"phraséologique", "f":"phraséologique"},
    {"m":"localisateur", "f":"localisatrice"},
    {"m":"glorificateurs", "f":"glorificatrice"},
    {"m":"épigrammatique", "f":"épigrammatique"},
    {"m":"tintinnabulant", "f":"tintinnabulante"},
    {"m":"irréalisé", "f":"irréalisée"},
    {"m":"inassouvissable", "f":"inassouvissable"},
    {"m":"valétudinaire", "f":"valétudinaire"},
    {"m":"méphistophélique", "f":"méphistophélique"},
    {"m":"prévaricateur", "f":"prévaricatrice"},

]

liste_preposition = [
    "à",
    "durant",
    "pendant",
    "après",
    "en",
    "pour",
    "avant",
    "entre",
    "près",
    "avec",
    "excepté",
    "sans",
    "chez",
    "hormis",
    "sauf",
    "concernant",
    "hors",
    "selon",
    "contre",
    "jusque",
    "sous",
    "dans",
    "malgré",
    "suivant",
    "de",
    "moyennant",
    "sur",
    "depuis",
    "outre",
    "vers",
    "derrière",
    "par",
    "voici",
    "dès",
    "parmi",
    "voilà​",
    "devant",
    "vu",
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
        groupe_verbal_avec_preposition(premier_A),
        groupe_nominal_adjectif(deuxieme_A).capitalize(),
        groupe_verbal_avec_preposition(premier_B),
        groupe_nominal_adjectif(deuxieme_B).capitalize(),
    )
    return structure_AABB


def groupe_nominal(dict_nom=None):
    """Création d'un groupe nominal à partir d'une liste de dictionnaires contenant des noms (noyaux).
    On détermine le déterminant par la suite et si on ajoute un complément.

    Args:
        dict_nom: Un dictionnaire contenant un nom. Par défaut on choisit un dictionnaire au hasard dans la liste.

    Returns:
        Un groupe nominal.
    """
    if dict_nom is None:
        random.seed(random.randrange(99999999))
        dict_nom = random.choice(liste_nom)
    noyau = dict_nom["nom"]
    determinant = nom_vers_determinant(dict_nom)
    determinant = verifier_mot_debute_voyelle(noyau, determinant)

    if determinant[-1] == "'":
        # Dernier caractère est un apostrophe donc on doit coller déterminant avec noyau
        groupe_nominal = "{}{}".format(determinant, noyau)
    else:
        groupe_nominal = "{} {}".format(determinant, noyau)
    return groupe_nominal

def groupe_nominal_adjectif(dict_nom=None):
    """Création d'un groupe nominal à partir d'une liste de dictionnaires contenant des noms (noyaux).
    On détermine le déterminant par la suite et si on ajoute un complément.

    Args:
        dict_nom: Un dictionnaire contenant un nom. Par défaut on choisit un dictionnaire au hasard dans la liste.

    Returns:
        Un groupe nominal.
    """
    if dict_nom is None:
        random.seed(random.randrange(99999999))
        dict_nom = random.choice(liste_nom)
    noyau = dict_nom["nom"]
    determinant = nom_vers_determinant(dict_nom)
    expansion = nom_vers_adjectif(dict_nom)
    determinant = verifier_mot_debute_voyelle(expansion, determinant)

    if determinant[-1] == "'":
        # Dernier caractère est un apostrophe donc on doit coller déterminant avec noyau
        groupe_nominal_adjectif = "{}{} {}".format(determinant, expansion, noyau)
    else:
        groupe_nominal_adjectif = "{} {} {}".format(determinant, expansion, noyau)
    return groupe_nominal_adjectif

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
        determinant
    """
    if nom[0] == ("a" or "e" or "i" or "o" or "u" or "h"):
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
        dict_nom: Un dictionnaire contenant un nom et son genre.

    Returns:
        Un adjectif du même genre que le nom passé en argument.
    """
    dict_adjectif = random.choice(liste_adjectif)
    for k in dict_adjectif:
        if k == dict_nom["genre"]:
            adjectif = dict_adjectif[k]
    return adjectif


if __name__ == "__main__":
    print(rime_AABB())
