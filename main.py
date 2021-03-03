import random

liste_nom = [{"nom":"armoire", 'genre':'f'},
            {'nom':'clé', 'genre':'f'},
            {'nom':'porte', 'genre':'f'},
            {'nom':'sonette', 'genre':'f'},
            {'nom':'lavabo', 'genre':'m'},
            {"nom": "allumette", "genre": "f"},
            {"nom": "anniversaire", "genre":"m"},
            {"nom": "appétit","genre":"m"},
            {"nom": "beurre", "genre":"m"},
            {"nom": "coquille", "genre": "f"},
            {"nom": "crêpe","genre":"f"},
            {"nom": "marionnette","genre":"f"},
            {"nom": "marteau", "genre":"m"},
            {"nom": "métal", "genre": "m"},
            {"nom": "mètre","genre":"m"},
]
liste_verbe = ['apporte', 'entre', "s'installe", "agace", "gratte", "vit", "grandit", "boit", "plante"]
liste_determinant_feminin = ["une", "la", "cette", "ta"]
liste_determinant_masculin = ["un", "le", "cet", "ton"]
liste_adjectif_feminin = ["adroite", "difficile", "dure", "facile", "lisse", "maladroite", "pointue", "rugueuse", "tordue", "absente", "assise", "basse", "couchée", "haute", "présente", "blonde", "brune", "calme", "curieuse", "différente", "douce", "énervée", "gentille", "grande", "handicapée", "inséparable", "jalouse", "moyenne", "muette", "noire", "nouvelle", "petite", "polie", "propre", "rousse", "sage", "sale", "sérieuse", "sourde", "tranquille"]
liste_adjectif_masculin = ["adroit", "difficile", "dur", "facile", "lisse", "maladroit", "pointu", "rugueux", "tordu", "absent", "assis", "bas", "couché", "haut", "présent", "blond", "brun", "calme", "curieux", "différent", "doux", "énervé", "gentil", "grand", "handicapé", "inséparable", "jaloux", "moyen", "muet", "noir", "nouveau", "petit", "poli", "propre", "roux", "sage", "sale", "sérieux", "sourd", "tranquille"]

def nouvelle_phrase():
    """Retourne une phrase selon une structure.

    Returns:
        Une phrase.
    """
    dict_nom1 = random.choice(liste_nom) # Retourne un nom au hasard dans la liste
    nom1 = dict_nom1['nom'] # prend l'attribut nom du dict
    det1 = nom_vers_determinant(dict_nom1) # retourne un dét du même genre
    dict_nom2 = random.choice(liste_nom)
    nom2 = dict_nom2['nom']
    det2 = nom_vers_determinant(dict_nom2)
    verbe = random.choice(liste_verbe)
    phrase = "{} {} {} {} {}".format(det1, nom1, verbe, det2, nom2)
    return phrase

def nom_vers_determinant(dict_nom):
    """Retourne un déterminant du même genre que le nom.

    Args:
        dict_nom: Un dictionnaire contenant un nom et son genre.

    Returns:
        Un déterminant du même genre que le nom passé en argument.
    """
    if dict_nom['genre'] == "f":
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
    if dict_nom['genre'] == "f":
        adjectif = random.choice(liste_adjectif_feminin)
    else:
        adjectif = random.choice(liste_adjectif_masculin)
    return adjectif

if __name__ == "__main__":
    print(nouvelle_phrase() + ",\n" + nouvelle_phrase() + ",\n" + nouvelle_phrase()+ ",\n" + nouvelle_phrase())