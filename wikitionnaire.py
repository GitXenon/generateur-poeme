from bs4 import BeautifulSoup
from tinydb import TinyDB, Query
import requests


def recup_adjectif(mot):
    """Retourne une entrée complète

    Returns:
        nouvel_adj = Dictionnaire avec l'adjectif pour ajouter au DB
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

if __name__ == "__main__":
    db = TinyDB('db.json')
    Adjectif = db.table('adjectif')
    liste_adjectif_ajouté = ['platonique', 'charnel', 'romantique', 'sentimental', 'aimé', 'tendre', 'beau', 'éternel', 'fraternel', 'incoditionnel', 'passionnel', 'fou', 'immodéré']
    for item in liste_adjectif_ajouté:
        print('Ajout de ' + item + ' en cours...')
        nouvel_adj = recup_adjectif(item)
        if nouvel_adj is not None:
            Adjectif.insert(nouvel_adj)
            print(item + ' ajouté!')