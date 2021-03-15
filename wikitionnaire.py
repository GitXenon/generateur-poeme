import re

from bs4 import BeautifulSoup
from tinydb import TinyDB, Query
import requests

# ce, mon, ton, son, notre, votre, leur, quel, du, un, aucun, plusieurs, tout, tel, lequel, auquel, duquel

def recup_determinant(mot):
    """Retourne une entrée complète

    Returns:
        dict_det (dict): Dictionnaires avec le déterminant à ajouter au DB
    """
    url = "https://fr.wiktionary.org/wiki/"
    page = requests.get(url + mot)
    soup = BeautifulSoup(page.text, "html.parser")
    regex = "(Adjectif|Article)_(défini|indéfini|démonstratif|possessif|interrogatif|exclamatif| partitif|numéral|quantitatif|relatif)"
    title_pronom = soup.find(id=re.compile(regex))
    if title_pronom == None:
        print("Mot n'est peut être pas un déterminant.")
        return None
    table = title_pronom.parent.next_sibling.next_sibling

    liste_mot = table.find_all('td')
    if len(liste_mot) == 5:
        premier_td = liste_mot[1].find_all('a')
        deuxieme_td = liste_mot[2].find_all('a')
        troisieme_td = liste_mot[3].find_all('a')
        quatrieme_td = liste_mot[4].find_all('a')
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
            'ms': {"mot": det_ms, "nb_syllabes": det_ms_syllabes, "API": det_ms_API},
            'mp': {"mot": det_mp, "nb_syllabes": det_ms_syllabes, "API": det_mp_API},
            'fs': {"mot": det_fs, "nb_syllabes": det_ms_syllabes, "API": det_fs_API},
            'fp': {"mot": det_fp, "nb_syllabes": det_ms_syllabes, "API": det_fp_API}
        }
    elif len(liste_mot) == 4:
        print("PAS ENCORE IMPLÉMENTER !!!")
        return None
    else:
        print("Impossible d'ajouté ce mot: " + mot + ". Problème !!!!")
        return None

    return dict_det

def recup_nom(mot):
    """Retourne une entrée complète

    Returns:
        nouveau_nom (liste): Liste de dictionnaires avec le nom pour ajouter au DB
    """
    url = "https://fr.wiktionary.org/wiki/"
    page = requests.get(url + mot)
    soup = BeautifulSoup(page.text, "html.parser")
    regex = "Nom_commun\w*"
    title_nom = soup.find(id=re.compile(regex))
    if title_nom == None:
        print("Mot n'est peut être pas un nom.")
        return None
    title_nom = title_nom.parent

    # On vérifie 
    definition = title_nom
    while definition.name != 'p':
        definition = definition.next_sibling
    if definition.b.text != mot:
        print("Impossible d'ajouté ce mot: " + mot)
        return None
    
    table = title_nom
    while table.name != 'table':
        table = table.next_sibling
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
        print(len(liste_mot))
        print("Impossible d'ajouté ce mot: " + mot + ". Problème nombre td.")
        return None

    if definition.i is None:
        definition = definition.next_sibling.next_sibling
        if definition.i is None:
            print("Problème avec ce mot.") #TODO: Fix recup_nom
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

def existe_dans_DB(mot, table):
    """Retourne true or false is existe déjà dans DB. Fonctionne avec déterminant et adjectif.

    Args:
        mot (str):
        table (table):

    Returns:
        is_in_database (bool):
    """

    if table.name == 'nom':
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

def ajouter_adjectif_DB(liste_adjectif):
    """Ajoute un adjectif au DB
    
    Args:
        liste_adjectif (list): Une liste d'adjectifs.
    """
    db = TinyDB('db.json')
    Adjectif = db.table('adjectif')
    for item in liste_adjectif:
        if existe_dans_DB(item, Adjectif) is True:
            print(item + ' est déjà dans la base de donnée !')
        else:
            print('Ajout de ' + item + ' en cours...')
            nouvel_adj = recup_adjectif(item)
            if nouvel_adj is not None:
                Adjectif.insert(nouvel_adj)
                print(item + ' ajouté!')
    db.close()

def ajouter_determinant_DB(liste_determinant):
    """Ajoute des déterminants au DB
    
    Args:
        liste_determinant (list): Une liste de déterminants.
    """
    db = TinyDB('db.json')
    Determinant = db.table('determinant')
    for item in liste_determinant:
        if existe_dans_DB(item, Determinant) is True:
            print(item + ' est déjà dans la base de donnée !')
        else:
            print('Ajout de ' + item + ' en cours...')
            nouveau_det = recup_determinant(item)
            if nouveau_det is not None:
                Determinant.insert(nouveau_det)
                print(item + ' ajouté!')
    db.close()

def ajouter_nom_DB(nom_a_ajouter):
    """Ajoute un adjectif au DB
    
    Args:
        nom_a_ajouter (str): Un nom à ajouter dans la DB.

    Returns:
        ajouter_dans_db (bool): true or false
    """
    db = TinyDB('db.json')
    Nom = db.table('nom')
    if existe_dans_DB(nom_a_ajouter, Nom) is True:
        print(nom_a_ajouter + ' est déjà dans la base de donnée !')
        ajouter_dans_db = False 
    else:
        print('Ajout de ' + nom_a_ajouter + ' en cours...')
        liste_mot = recup_nom(nom_a_ajouter)
        if liste_mot is not None:
            for dict_mot in liste_mot:
                #Nom.insert(dict_mot)
                ajouter_dans_db = True
        elif liste_mot is None:
            ajouter_dans_db = False
    db.close()
    return ajouter_dans_db


if __name__ == "__main__":
    #liste_det = ["ce", "mon", "ton", "son", "notre", "votre", "leur", "quel", "du", "un", "aucun", "plusieurs", "tout", "tel", "lequel", "auquel", "duquel"]
    liste_nom = ["amant", "tendresse", "passion", "amitié", "désir", "cœur", "vie", "amoureux", "bonheur", "philtre", "beauté", "amoureuse", "amante", "couple", "baiser", "sentiment", "joue", "gars", "fille", "poésie", "homme", "sensualité", "plaisir"]
    #liste_adj = ["amoureux", "platonique", "charnel", "romantique", "sentimentale", "aimé", "tendre", "beau", "éternel", "fraternel", "inconditionnel", "passionnel", "fou", "jeune", "sensuel", "heureux", "divine", "érotique", "conjugal", "intime", "douce", "fusionnel"]
    #ajouter_determinant_DB(liste_det)
    #ajouter_adjectif_DB(liste_adj)
    for item in liste_nom:
        ajouter_nom_DB(item)
