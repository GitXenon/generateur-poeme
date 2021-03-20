import re
import logging

from bs4 import BeautifulSoup
from tinydb import TinyDB, Query
import requests

logging.basicConfig(level=logging.INFO)


def recup_determinant(mot):
    """Retourne un dictionnaire complet avec les attributs du déterminant passé en argument.

    Args:
        mot (str): le mot à récupérer.

    Returns:
        dict_det (dict): Dictionnaires avec le déterminant à ajouter au DB
    """
    url = "https://fr.wiktionary.org/wiki/"
    page = requests.get(url + mot)
    soup = BeautifulSoup(page.text, "html.parser")
    regex = "(Adjectif|Article)_(défini|indéfini|démonstratif|possessif|interrogatif|exclamatif|partitif|numéral|quantitatif|relatif)"
    title_pronom = soup.find(id=re.compile(regex))
    if title_pronom == None:
        logging.error("Mot n'est peut être pas un déterminant.")
        return None
    table = title_pronom.parent.next_sibling.next_sibling

    liste_mot = table.find_all("td")
    if len(liste_mot) == 5:
        premier_td = liste_mot[1].find_all("a")
        deuxieme_td = liste_mot[2].find_all("a")
        troisieme_td = liste_mot[3].find_all("a")
        quatrieme_td = liste_mot[4].find_all("a")
        det_ms = premier_td[0].text
        det_ms_API = premier_td[1].text
        det_mp = deuxieme_td[0].text
        det_mp_API = deuxieme_td[1].text
        det_fs = troisieme_td[0].text
        det_fs_API = troisieme_td[1].text
        det_fp = quatrieme_td[0].text
        det_fp_API = quatrieme_td[1].text

        det_ms_syllabes = det_ms_API.count(".") + 1
        det_mp_syllabes = det_mp_API.count(".") + 1
        det_fs_syllabes = det_fs_API.count(".") + 1
        det_fp_syllabes = det_fp_API.count(".") + 1

        dict_det = {
            "ms": {"mot": det_ms, "nb_syllabes": det_ms_syllabes, "API": det_ms_API},
            "mp": {"mot": det_mp, "nb_syllabes": det_ms_syllabes, "API": det_mp_API},
            "fs": {"mot": det_fs, "nb_syllabes": det_ms_syllabes, "API": det_fs_API},
            "fp": {"mot": det_fp, "nb_syllabes": det_ms_syllabes, "API": det_fp_API},
        }
    elif len(liste_mot) == 4:
        logging.error("PAS ENCORE IMPLÉMENTER !!!")
        return None
    else:
        logging.error("Impossible d'ajouté ce mot: " + mot + ". Problème !!!!")
        return None

    return dict_det


def recup_nom(mot):
    """Retourne une liste de dictionnaires avec les attributs du nom passé en argument.

    Args:
        mot (str): le mot à récupérer.

    Returns:
        nouveau_nom (liste): Liste de dictionnaires avec le nom pour ajouter au DB
    """
    url = "https://fr.wiktionary.org/wiki/"
    page = requests.get(url + mot)
    soup = BeautifulSoup(page.text, "html.parser")
    regex = "Nom_commun\w*"
    title_nom = soup.find(id=re.compile(regex))
    if title_nom == None:
        logging.error("Mot n'est peut être pas un nom.")
        return None
    title_nom = title_nom.parent

    definition = title_nom
    while definition.name != "p":
        # On passe au prochain sibling jusqu'à atteindre une classe html 'p'
        definition = definition.next_sibling
    if definition.b.text != mot:
        logging.error("Impossible d'ajouté ce mot: " + mot)
        return None

    table = title_nom
    while table.name != "table":
        table = table.next_sibling
    liste_mot = table.find_all("td")
    if len(liste_mot) == 1:
        resultat = liste_mot[0].find_all("a")
        nom_s = resultat[0].text.rstrip()
        nom_p = nom_s
        nom_API = resultat[1].text
    elif len(liste_mot) == 3:
        nom_s = liste_mot[0].a.text
        nom_p = liste_mot[1].a.text
        nom_API = liste_mot[2].a.text
    else:
        logging.error("Impossible d'ajouté ce mot: " + mot + ". Problème nombre td.")
        return None

    if definition.i is None:
        definition = definition.next_sibling.next_sibling
        if definition.i is None:
            logging.error("Problème avec ce mot.")  # TODO: Fix recup_nom
            return None
    genre = definition.i.text
    if genre == "masculin":
        nom_syllabes = nom_API.count(".") + 1
        nouveau_nom = [
            {
                "mot": nom_s,
                "nb_syllabes": nom_syllabes,
                "genre": "m",
                "nombre": "s",
                "API": nom_API,
            },
            {
                "mot": nom_p,
                "nb_syllabes": nom_syllabes,
                "genre": "m",
                "nombre": "p",
                "API": nom_API,
            },
        ]
    elif genre == "féminin":
        nom_syllabes = nom_API.count(".") + 1
        nouveau_nom = [
            {
                "mot": nom_s,
                "nb_syllabes": nom_syllabes,
                "genre": "f",
                "nombre": "s",
                "API": nom_API,
            },
            {
                "mot": nom_p,
                "nb_syllabes": nom_syllabes,
                "genre": "f",
                "nombre": "p",
                "API": nom_API,
            },
        ]
    else:
        logging.error("Problème de genre avec ce mot: " + mot)
        return None

    return nouveau_nom


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


def ajouter_dans_DB(mot_a_ajouter, categorie_mot):
    """Une fonction pour ajouter un mot dans la base de donnée.

    Args:
        mot_a_ajouter (str): Un mot.
        categorie_mot (str): La catégorie ('déterminant', 'nom', etc.) que mot_a_ajouter appartient.
    """
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
