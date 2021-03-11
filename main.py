import random

liste_nom = [
    {"nom": "rime", "genre": "m", "rime": "im"},
    {"nom": "crime", "genre": "m", "rime": "im"},
    {"nom": "prime", "genre": "f", "rime": "im"},
    {"nom": "déprime", "genre": "f", "rime": "im"},
    {"nom": "intérim", "genre": "m", "rime": "im"},
    {"nom": "gym", "genre": "m", "rime": "im"},
    {"nom": "lime", "genre": "f", "rime": "im"},
    {"nom": "cybercrime", "genre": "m", "rime": "im"},
    {"nom": "abime", "genre": "m", "rime": "im"},
    {"nom": "enzyme", "genre": "f", "rime": "im"},
    {"nom": "régime", "genre": "m", "rime": "im"},
    {"nom": "estime", "genre": "f", "rime": "im"},
    {"nom": "anonyme", "genre": "m", "rime": "im"},
    {"nom": "victime", "genre": "f", "rime": "im"},
    {"nom": "sublime", "genre": "m", "rime": "im"},
    {"nom": "synonyme", "genre": "m", "rime": "im"},
    {"nom": "acronyme", "genre": "f", "rime": "im"},
    {"nom": "laid", "genre": "m", "rime": "è"},
    {"nom": "plaie", "genre": "f", "rime": "è"},
    {"nom": "volet", "genre": "m", "rime": "è"},
    {"nom": "reflet", "genre": "m", "rime": "è"},
    {"nom": "poulet", "genre": "m", "rime": "è"},
    {"nom": "anglais", "genre": "m", "rime": "è"},
    {"nom": "français", "genre": "m", "rime": "è"},
    {"nom": "ballet", "genre": "m", "rime": "è"},
    {"nom": "valet", "genre": "m", "rime": "è"},
    {"nom": "gilet", "genre": "m", "rime": "è"},
    {"nom": "galet", "genre": "m", "rime": "è"},
    {"nom": "mollet", "genre": "m", "rime": "è"},
    {"nom": "palais", "genre": "m", "rime": "è"},
    {"nom": "couplet", "genre": "m", "rime": "è"},
    {"nom": "amour", "genre": "f", "rime": "ur"},
    {"nom": "tourd", "genre": "m", "rime": "ur"},
    {"nom": "bourre", "genre": "m", "rime": "ur"},
    {"nom": "rebours", "genre": "m", "rime": "ur"},
    {"nom": "atour", "genre": "m", "rime": "ur"},
    {"nom": "séjour", "genre": "m", "rime": "ur"},
    {"nom": "discours", "genre": "m", "rime": "ur"},
    {"nom": "parcours", "genre": "m", "rime": "ur"},
    {"nom": "retour", "genre": "m", "rime": "ur"},
    {"nom": "jour", "genre": "m", "rime": "ur"},
    {"nom": "cour", "genre": "f", "rime": "ur"},
    {"nom": "four", "genre": "m", "rime": "ur"},
    {"nom": "sourd", "genre": "m", "rime": "ur"},
    {"nom": "secours", "genre": "m", "rime": "ur"},
    {"nom": "concours", "genre": "m", "rime": "ur"},
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
    print("Bienvenue au générateur de poème.\n-------------------\n\n")
    print("Veuillez prendre une option parmis les suivantes:\n1.AABB\n2.ABBA\n3.ABAB\n")
    choix = input()
    if choix == "1":
        print(rime_AABB())
    if choix == "2":
        print(rime_ABBA())
    if choix == "3":
        print(rime_ABAB())