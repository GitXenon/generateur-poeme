from bs4 import BeautifulSoup
from tinydb import TinyDB, Query
import requests

def recup_nom(mot):
    """Retourne une entrée complète

    Returns:
        nouveau_nom (liste): Liste de dictionnaires avec le nom pour ajouter au DB
    """
    url = "https://fr.wiktionary.org/wiki/"
    page = requests.get(url + mot)
    soup = BeautifulSoup(page.text, "html.parser")

    table_nombre = soup.find(class_="flextable")

    definition = soup.p
    if definition.b.text != mot:
        print("Impossible d'ajouté ce mot: " + mot)
        return None

    table = soup.find(class_='flextable')
    liste_mot = table.find_all('td')
    if len(liste_mot) == 1:
        resultat = liste_mot[0].find_all('a')
        nom_s = resultat[0].text.rstrip()
        nom_p = nom_s
        nom_API = resultat[1].text
    elif len(liste_mot) == 3:
        nom_s = liste_mot[0].a.text
        nom_p = liste_mot[1].a.text
        nom_API = liste_mot[2].a.text
    else:
        print("Impossible d'ajouté ce mot: " + mot + ". Problème nombre td.")
        return None

    genre = definition.i.text
    if genre == 'masculin':
        nom_syllabes = nom_API.count(".") + 1
        nouveau_nom = [
            {"mot": nom_s, "nb_syllabes": nom_syllabes,"genre":"m","nombre":"s","API": nom_API},
            {"mot": nom_p, "nb_syllabes": nom_syllabes,"genre":"m","nombre":"p","API": nom_API}
            ]
    elif genre == 'féminin':
        nom_syllabes = nom_API.count(".") + 1
        nouveau_nom = [
            {"mot": nom_s, "nb_syllabes": nom_syllabes,"genre":"f","nombre":"s","API": nom_API},
            {"mot": nom_p, "nb_syllabes": nom_syllabes,"genre":"f","nombre":"p","API": nom_API}
            ]
    else:
        print('Problème de genre avec ce mot: ' + mot)
        return None

    return nouveau_nom

def recup_adjectif(mot):
    """Retourne une entrée complète

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
        print("Impossible d'ajouté ce mot: " + mot)
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

def exist_database(mot, table):
    """Retourne true or false is existe déjà dans DB

    Args:
        mot (str):
        table (table):

    Returns:
        is_in_database (bool):
    """
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
    
def ajouter_adjectif_DB(liste_adjectif):
    """Ajoute un adjectif au DB
    
    Args:
        liste_adjectif (list): Une liste d'adjectifs.
    """
    db = TinyDB('db.json')
    Adjectif = db.table('adjectif')
    for item in liste_adjectif:
        if exist_database(item, Adjectif) is True:
            print(item + ' est déjà dans la base de donnée !')
        else:
            print('Ajout de ' + item + ' en cours...')
            nouvel_adj = recup_adjectif(item)
            if nouvel_adj is not None:
                Adjectif.insert(nouvel_adj)
                print(item + ' ajouté!')
    db.close()

def ajouter_nom_DB(liste_nom):
    """Ajoute un adjectif au DB
    
    Args:
        liste_adjectif (list): Une liste de noms.
    """
    db = TinyDB('db.json')
    Nom = db.table('nom')
    for item in liste_nom:
        if exist_database(item, Nom) is True:
            print(item + ' est déjà dans la base de donnée !')
        else:
            print('Ajout de ' + item + ' en cours...')
            liste_nom = recup_nom(item)
            if liste_nom is not None:
                for dict_mot in liste_nom:
                    Nom.insert(dict_mot)
                    print(item + ' ajouté!')
    db.close()


if __name__ == "__main__":
    pass
