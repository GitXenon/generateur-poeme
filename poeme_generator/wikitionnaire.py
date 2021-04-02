import re
import logging

from bs4 import BeautifulSoup
from tinydb import TinyDB, Query
import requests

logging.basicConfig(level=logging.INFO)

def creation_dictionnaire(mot, nb_syllabes, genre, nombre, mot_API):
    dictionnaire = {"mot": mot,
                "nb_syllabes": nb_syllabes,
                "genre": genre,
                "nombre": nombre,
                "API": mot_API,}
    return dictionnaire

def recup_mot(mot, categorie_mot):
    """Retourne une liste de dictionnaires avec les attributs du nom passé en argument.

    Args:
        mot (str): le mot à récupérer.
        categorie_mot (str): La catégorie qu'appartient l'argument mot.

    Returns:
        nouveau_nom (liste): Liste de dictionnaires avec le nom pour ajouter au DB
    """
    url = "https://fr.wiktionary.org/wiki/"

    # TODO: Regarder si le mot est du bon format

    page = requests.get(url + mot)
    soup = BeautifulSoup(page.text, "html.parser")

    # On attribut un regex selon la catégorie du mot
    if categorie_mot == "nom":
        regex = "Nom_commun\w*"
    elif categorie_mot == "adjectif":
        regex = "Adjectif\w*"
    elif categorie_mot == "determinant":
        regex = "(Adjectif|Article)_(défini|indéfini|démonstratif|possessif|interrogatif|exclamatif|partitif|numéral|quantitatif|relatif)"
    else:
        logging.error("Catégorie n'est pas encore implémenter.")

    title_nom = soup.find(id=re.compile(regex))  # Un span contenant la catégorie du mot
    if title_nom == None:
        # Si la catégorie n'est pas trouvable dans la page on retourne rien
        logging.error("Mot n'est peut être pas un nom.")
        return None
    definition = title_nom.parent  # parent du <span> est <h3>

    while definition.name != "p":
        # On passe au prochain sibling jusqu'à atteindre une classe html 'p'
        definition = definition.next_sibling
    if definition.b.text != mot:
        # Si la partie <b> n'est pas le mot recherché, on conclut que la page n'est pas bonne.
        logging.error(
            "Mot en bold dans paragraphe trouvé n'est pas le même que: " + mot
        )
        return None

    table = title_nom.parent
    while table.name != "table":
        # On itère les classes jusqu'à trouver une <table>
        table = table.next_sibling
        # TODO: Catch error if no table found

    liste_mot = []  # On initialise une liste vide qu'on va ajouter les mots
    liste_table_mot = table.find_all("td")
    if len(liste_table_mot) == 1:
        resultat = liste_table_mot[0].find_all("a")
        mot = resultat[0].text.rstrip()
        mot_API = resultat[1].text
        nb_syllabes = mot_API.count(".") + 1
        if 'masculin' in definition.text and ('singulier' in definition.text or 'invariable' in definition.text):
            dict_mot = creation_dictionnaire(mot,nb_syllabes, 'm', 's', mot_API)
            liste_mot.append(dict_mot)
        if 'masculin' in definition.text and ('pluriel' in definition.text or 'invariable' in definition.text):
            dict_mot = creation_dictionnaire(mot,nb_syllabes, 'm', 'p', mot_API)
            liste_mot.append(dict_mot)
        if 'féminin' in definition.text and ('singulier' in definition.text or 'invariable' in definition.text):
            dict_mot = creation_dictionnaire(mot,nb_syllabes, 'f', 's', mot_API)
            liste_mot.append(dict_mot)
        if 'féminin' in definition.text and ('pluriel' in definition.text or 'invariable' in definition.text):
            dict_mot = creation_dictionnaire(mot,nb_syllabes, 'f', 'p', mot_API)
            liste_mot.append(dict_mot)
    elif len(liste_table_mot) == 2:
        for i in range(2):
            liste_a = liste_table_mot[i].find_all("a")
            mot = liste_a[0].text
            mot_API = liste_a[1].text
            nb_syllabes = mot_API.count(".") + 1
            if 'masculin' in definition.text:
                genre = 'm'
            elif 'féminin' in definition.text:
                genre = 'f'
            else:
                genre = liste_table_mot[i].previous_sibling.previous_sibling.text[:-1] 
            if i == 0:
                nombre = "s"
            elif i == 1:
                nombre = "p"
            dict_mot = creation_dictionnaire(mot, nb_syllabes, genre, nombre, mot_API)
            liste_mot.append(dict_mot)
    elif len(liste_table_mot) == 3:
        for i in range(2):
            mot = liste_table_mot[i].a.text
            mot_API = liste_table_mot[2].find_all("a")[0].text
            nb_syllabes = mot_API.count(".") + 1
            if 'masculin' in definition.text:
                genre = 'm'
            elif 'féminin' in definition.text:
                genre = 'f'
            if i == 0:
                nombre = "s"
            elif i == 1:
                nombre = "p"
            dict_mot = creation_dictionnaire(mot, nb_syllabes, genre, nombre, mot_API)
            liste_mot.append(dict_mot)
    elif len(liste_table_mot) == 4:
        logging.error(
            "Impossible d'ajouté ce mot: "
            + mot
            + ". Nombre <td> n'est pas implémenter."
        )
        return None  # TODO: Implémenter cette partie.
    elif len(liste_table_mot) == 5:
        for i in range(1, 5):
            liste_a = liste_table_mot[i].find_all("a")
            mot = liste_a[0].text
            mot_API = liste_a[1].text
            nb_syllabes = mot_API.count(".") + 1
            if i == 1 or i == 2:
                genre = "m"
            elif i == 3 or i == 4:
                genre = "f"
            if i == 1 or i == 3:
                nombre = "s"
            elif i == 2 or i == 4:
                nombre = "p"
            dict_mot = creation_dictionnaire(mot, nb_syllabes, genre, nombre, mot_API)
            liste_mot.append(dict_mot)
    else:
        logging.error(
            "Impossible d'ajouté ce mot: "
            + mot
            + ". Nombre <td> n'est pas implémenter."
        )
        return None

    return liste_mot


def recup_adjectif(mot):
    """Retourne un dictionnaire complet avec les attributs de l'adjectif passé en argument.

    Args:
        mot (str): L'adjectif à récupérer.

    Returns:
        nouvel_adj (dict): Dictionnaire avec l'adjectif pour ajouter au DB
    """
    url = "https://fr.wiktionary.org/wiki/"
    page = requests.get(url + mot)

    soup = BeautifulSoup(page.text, "html.parser")

    table_genre_nombre = soup.find(class_="flextable flextable-fr-mfsp")
    try:
        liste_genre_nombre = table_genre_nombre.find_all("tr")
    except AttributeError:
        logging.error("Impossible d'ajouté ce mot: " + mot)
        return None
    try:
        if liste_genre_nombre[1]["class"] == ["flextable-fr-m"]:
            liste_mot = liste_genre_nombre[1].find_all("a")
            try:
                if liste_genre_nombre[1].td["colspan"] == "2":
                    nom_ms = liste_mot[0].text
                    nom_ms_API = liste_mot[1].text
                    nom_mp = nom_ms
                    nom_mp_API = nom_ms_API
            except KeyError:
                nom_ms = liste_mot[0].text
                nom_ms_API = liste_mot[1].text
                nom_mp = liste_mot[2].text
                nom_mp_API = liste_mot[3].text

        if liste_genre_nombre[2]["class"] == ["flextable-fr-f"]:
            liste_mot = liste_genre_nombre[2].find_all("a")
            try:
                if liste_genre_nombre[2].td["colspan"] == "2":
                    nom_fs = liste_mot[0].text
                    nom_fs_API = liste_mot[1].text
                    nom_fp = nom_fs
                    nom_fp_API = nom_fs_API
            except KeyError:
                nom_fs = liste_mot[0].text
                nom_fs_API = liste_mot[1].text
                nom_fp = liste_mot[2].text
                nom_fp_API = liste_mot[3].text
    except KeyError:
        liste_mot = liste_genre_nombre[1].find_all("a")
        liste_mot_API = liste_genre_nombre[2].find_all("a")

        nom_ms = liste_mot[0].text
        nom_mp = liste_mot[1].text
        nom_fs = nom_ms
        nom_fp = nom_mp
        nom_ms_API = liste_mot_API[0].text
        nom_mp_API = nom_ms_API
        nom_fs_API = nom_ms_API
        nom_fp_API = nom_ms_API

    nom_ms_syllabes = nom_ms_API.count(".") + 1
    nom_mp_syllabes = nom_mp_API.count(".") + 1
    nom_fs_syllabes = nom_fs_API.count(".") + 1
    nom_fp_syllabes = nom_fp_API.count(".") + 1
    nouvel_adj = {
        "ms": {"mot": nom_ms, "nb_syllabes": nom_ms_syllabes, "API": nom_ms_API},
        "fs": {"mot": nom_fs, "nb_syllabes": nom_fs_syllabes, "API": nom_fs_API},
        "mp": {"mot": nom_mp, "nb_syllabes": nom_mp_syllabes, "API": nom_mp_API},
        "fp": {"mot": nom_fp, "nb_syllabes": nom_fp_syllabes, "API": nom_fp_API},
    }
    return nouvel_adj


def existe_dans_DB(mot, table):
    """Retourne true or false is existe déjà dans DB. Fonctionne avec déterminant et adjectif.

    Args:
        mot (str): Un mot.
        table (table): Une table dans la TinyDB où chercher le mot.

    Returns:
        is_in_database (bool): true or false.
    """

    if table.name == "nom":
        Nom = Query()
        search_ms = table.search(Nom.mot == mot)
        if len(search_ms) != 0:
            is_in_database = True
        else:
            is_in_database = False
    else:
        Nom = Query()
        search_ms = table.search(Nom.ms.mot == mot)
        search_mp = table.search(Nom.mp.mot == mot)
        search_fs = table.search(Nom.fs.mot == mot)
        search_fp = table.search(Nom.fp.mot == mot)
        if (len(search_ms) or len(search_mp) or len(search_fs) or len(search_fp)) != 0:
            is_in_database = True
        else:
            is_in_database = False

    return is_in_database


def ajouter_dans_DB(mot_a_ajouter, categorie_mot, db=None):
    """Une fonction pour ajouter un mot dans la base de donnée.

    Args:
        mot_a_ajouter (str): Un mot.
        categorie_mot (str): La catégorie ('déterminant', 'nom', etc.) que mot_a_ajouter appartient.
        db: Ouverture d'un fichier json contenant une TinyDB. TinyDB("db.json")
    """
    if db is None:
        db = TinyDB("db.json")

    if categorie_mot == "nom":
        Table_categorie = db.table("nom")
    elif categorie_mot == "determinant":
        Table_categorie = db.table("determinant")
    elif categorie_mot == "adjectif":
        Table_categorie = db.table("adjectif")

    if existe_dans_DB(mot_a_ajouter, Table_categorie):
        logging.info(mot_a_ajouter + " est déjà dans la base de donnée !")
    else:
        logging.info("Ajout de " + mot_a_ajouter + " en cours...")

        if categorie_mot == "nom":
            dict_a_ajouter = recup_nom(mot_a_ajouter)
        elif categorie_mot == "determinant":
            dict_a_ajouter = recup_determinant(mot_a_ajouter)
        elif categorie_mot == "adjectif":
            dict_a_ajouter = recup_adjectif(mot_a_ajouter)
        if dict_a_ajouter is not None:
            if categorie_mot == "nom":
                for dict_nom in dict_a_ajouter:
                    Table_categorie.insert(dict_nom)
                    logging.info(dict_nom["mot"] + " ajouté!")
            else:
                Table_categorie.insert(dict_a_ajouter)
                logging.info(mot_a_ajouter + " ajouté!")

    db.close()


if __name__ == "__main__":
    liste = ["le", "un", "ton", "de", "cet"]
    for item in liste:
        ajouter_dans_DB(item, "determinant")
