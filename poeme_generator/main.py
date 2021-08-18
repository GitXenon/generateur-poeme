import os, random


def ouvrir_lexique():
    """Ouvre le fichier contenant le lexique et retourne une liste contenant toutes les entrées du lexique."""
    # TODO : changer nom variable temp
    lexique = open("Lexique383.tsv", encoding="UTF-8")
    texte_lexique = lexique.read()
    liste_lexique = texte_lexique.splitlines()
    index = 0
    while index < len(liste_lexique):
        liste_lexique[index] = liste_lexique[index].split("\t")
        index += 1
    return liste_lexique


def retourner_liste_mots(cat_gram, genre, nombre):
    """Retourne une liste avec la catégorie grammaticale donnée, ainsi que le genre et le nombre"""
    nouveau_lexique = []
    lexique = ouvrir_lexique()
    for x in lexique:
        if (cat_gram in x[3]) and (x[4] == genre or x[4] == "") and (x[5] == nombre or x[5] == ""):
            nouveau_lexique.append(x)
    return nouveau_lexique

def retourner_liste_mots(cat_gram, genre, nombre, syllabes):
    """Retourne une liste avec la catégorie grammaticale donnée, ainsi que le genre et le nombre"""
    nouveau_lexique = []
    lexique = ouvrir_lexique()
    for x in lexique:
        if (cat_gram in x[3]) and (x[4] == genre or x[4] == "") and (x[5] == nombre or x[5] == "") and (int(x[23]) == syllabes):
            nouveau_lexique.append(x)
    return nouveau_lexique


def retourner_verbe(conjugaison):
    """Retourne un verbe au hasard avec la conjugaison désirée"""
    nouveau_lexique = []
    lexique = ouvrir_lexique()
    for x in lexique:
        if "VER" in x[3] and conjugaison in x[10]:
            nouveau_lexique.append(x)
    verbe = random.choice(nouveau_lexique)
    return verbe[0]

def retourner_verbe(conjugaison, syllabes):
    """Retourne un verbe au hasard avec la conjugaison désirée"""
    nouveau_lexique = []
    lexique = ouvrir_lexique()
    for x in lexique:
        if "VER" in x[3] and conjugaison in x[10] and int(x[23]) == syllabes:
            nouveau_lexique.append(x)
    verbe = random.choice(nouveau_lexique)
    return verbe[0]


def retourner_mot(lexique):
    """Retourne un mot au hasard selon un lexique donnée"""
    random.seed()
    return random.choice(lexique)[0]

def retourner_mot(cat_gram, genre, nombre, syllabes):
    liste_mots = retourner_liste_mots(cat_gram, genre, nombre, syllabes)
    random.seed()
    try:
        return random.choice(liste_mots)[0]
    except IndexError:
        print("Impossible de trouver un mot!")
        return ""

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
        remplacement_GV = [
            "GN_vb",
            "_pn_vb",
            "_dt_nn_vb",
            "GVGN",
            "GV_pn",
            "GVGPR",
            "GPRGV",
        ]
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

    liste_determinant = retourner_liste_mots("ART", genre, nombre)
    liste_nom = retourner_liste_mots("NOM", genre, nombre)
    liste_adjectif = retourner_liste_mots("ADJ", genre, nombre)
    liste_verbe = retourner_liste_mots("VER", genre, nombre)
    liste_pronom = retourner_liste_mots("PRO", genre, nombre)

    while "_dt" in chaine_lexical:
        random.seed()
        chaine_lexical = chaine_lexical.replace(
            "_dt", retourner_mot(liste_determinant) + " ", 1
        )
    while "_pn" in chaine_lexical:
        random.seed()
        chaine_lexical = chaine_lexical.replace(
            "_pn", retourner_mot(liste_determinant) + " ", 1
        )
    while "_nn" in chaine_lexical:
        random.seed()
        chaine_lexical = chaine_lexical.replace(
            "_nn", retourner_mot(liste_nom) + " ", 1
        )
    while "_vb" in chaine_lexical:
        random.seed()
        chaine_lexical = chaine_lexical.replace(
            "_vb", retourner_mot(liste_verbe) + " ", 1
        )
    while "_pr" in chaine_lexical:
        random.seed()
        chaine_lexical = chaine_lexical.replace(
            "_pr", retourner_mot(liste_pronom) + " ", 1
        )
    while "_adj" in chaine_lexical:
        random.seed()
        chaine_lexical = chaine_lexical.replace(
            "_adj", retourner_mot(liste_adjectif) + " ", 1
        )

    phrase = chaine_lexical
    return phrase

def constrained_sum_sample_pos(n, total):
    """Return a randomly chosen list of n positive integers summing to total.
    Each such list is equally likely to occur."""

    dividers = sorted(random.sample(range(1, total), n - 1))
    return [a - b for a, b in zip(dividers + [total], [0] + dividers)]

if __name__ == "__main__":
    os.chdir("./poeme_generator")
    print(
        """---------------------------------------                                   
 ___ ___ ___ ___ ___ ___ ___ _____ ___ 
| . | -_|   | . | . | . | -_|     | -_|
|_  |___|_|_|___|  _|___|___|_|_|_|___|
|___|           |_|                    
---------------------------------------"""
    )
    print("Faites un choix parmis les options suivantes:\n" +
        "1. Générer un poème randomisé\n" +
        "2. Générer un poème à partir d'une structure déjà établis\n" +
        "3. Fill-in the blank\n" +
        "4. Haiku\n" +
        "0. Quitter\n"
    )
    while True:
        choix_utilisateur = input("Entrez votre choix : ")
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
            liste_adjectif_masculin_singulier = retourner_liste_mots("ADJ", "m", "s")
            liste_adjectif_feminin_singulier = retourner_liste_mots("ADJ", "f", "s")
            print(retourner_mot(liste_adjectif_masculin_singulier), end="")
            liste_nom_masculin_singulier = retourner_liste_mots("NOM", "m", "s")
            liste_nom_feminin_singulier = retourner_liste_mots("NOM", "f", "s")
            liste_nom_feminin_pluriel = retourner_liste_mots("NOM", "f", "p")
            print(", ce " + retourner_mot(liste_nom_masculin_singulier) + ".")
            print("💛")
            print(
                "C'est une "
                + retourner_mot(liste_nom_feminin_singulier)
                + ", un "
                + retourner_mot(liste_nom_masculin_singulier)
                + " "
                + retourner_mot(liste_adjectif_masculin_singulier)
            )
            print(
                retourner_verbe("inf")
                + " et "
                + retourner_verbe("inf")
                + " tour à tour.\n💛"
            )
            print(
                "Se "
                + retourner_verbe("inf")
                + " et "
                + retourner_verbe("inf")
                + " et "
                + retourner_verbe("inf")
            )
            print(
                "Et avoir de la "
                + retourner_mot(liste_nom_feminin_singulier)
                + ". c'est "
                + retourner_verbe("inf")
                + ".\n💛"
            )
            print(
                "C'est un ensemble de "
                + retourner_mot(liste_nom_masculin_singulier)
                + " et de "
                + retourner_mot(liste_nom_masculin_singulier)
            )
            print(
                "C'est le battement du "
                + retourner_mot(liste_nom_masculin_singulier)
                + " dans la "
                + retourner_mot(liste_nom_feminin_singulier)
                + ".\n💛"
            )
            print(
                "Un "
                + retourner_mot(liste_adjectif_masculin_singulier)
                + " "
                + retourner_mot(liste_nom_masculin_singulier)
                + ", et des "
                + retourner_mot(liste_nom_feminin_pluriel)
            )
            print(
                "Un "
                + retourner_mot(liste_nom_masculin_singulier)
                + ", et une "
                + retourner_mot(liste_adjectif_feminin_singulier)
                + " "
                + retourner_mot(liste_nom_feminin_singulier)
                + "."
            )
        elif choix_utilisateur == "4":
            liste_nb_syllabes_1 = constrained_sum_sample_pos(2,4)
            liste_nb_syllabes_2 = constrained_sum_sample_pos(2,5)
            print(liste_nb_syllabes_1, liste_nb_syllabes_2)
            print("Un " +
                retourner_mot("ADJ", "m", "s", liste_nb_syllabes_1[0]) +
                " " +
                retourner_mot("NOM", "m", "s", liste_nb_syllabes_1[1])
            )
            print("Une " +
                retourner_mot("NOM", "f", "s", liste_nb_syllabes_2[0]) +
                " qui " +
                retourner_verbe("ind:pre:1s", liste_nb_syllabes_2[1])
            )
            print("Le " +
                retourner_mot("NOM", "m", "s", 4)
            )
            
        else:
            print("Ceci n'est pas une option!")
