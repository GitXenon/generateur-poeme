import unittest
import tempfile

from tinydb import TinyDB, Query
from tinydb.storages import MemoryStorage

from main import nombre_syllables, groupe_nominal
import wikitionnaire


class TestNombreSyllable(unittest.TestCase):
    def test_syllable_1(self):
        self.assertEqual(nombre_syllables("éléphant"), 3)
        self.assertEqual(nombre_syllables("chameau"), 2)
        self.assertEqual(nombre_syllables("boeuf"), 1)
        self.assertEqual(nombre_syllables("crocodile"), 4)
        self.assertEqual(nombre_syllables("hirondelle"), 4)

    def test_syllable_2(self):
        self.assertEqual(nombre_syllables("garçon"), 2)
        self.assertEqual(nombre_syllables("informer"), 3)
        self.assertEqual(nombre_syllables("argent"), 2)
        self.assertEqual(nombre_syllables("expert"), 2)

    def test_syllable_3(self):
        self.assertEqual(nombre_syllables("pomme"), 2)
        self.assertEqual(nombre_syllables("terre"), 2)
        self.assertEqual(nombre_syllables("tasse"), 2)
        self.assertEqual(nombre_syllables("accident"), 3)
        self.assertEqual(nombre_syllables("apprendre"), 3)

    def test_syllable_4(self):
        self.assertEqual(nombre_syllables("montre"), 2)
        self.assertEqual(nombre_syllables("capable"), 2)


class TestWikitionnaire(unittest.TestCase):

    def test_recup_adjectif_1(self):
        nouvel_adj = wikitionnaire.recup_adjectif("amoureux")
        self.assertEqual(nouvel_adj["ms"]["mot"], "amoureux")
        self.assertEqual(nouvel_adj["mp"]["mot"], "amoureux")
        self.assertEqual(nouvel_adj["fs"]["mot"], "amoureuse")
        self.assertEqual(nouvel_adj["fp"]["mot"], "amoureuses")

        self.assertEqual(nouvel_adj["ms"]["nb_syllabes"], 3)
        self.assertEqual(nouvel_adj["mp"]["nb_syllabes"], 3)
        self.assertEqual(nouvel_adj["fs"]["nb_syllabes"], 3)
        self.assertEqual(nouvel_adj["fp"]["nb_syllabes"], 3)

        self.assertEqual(nouvel_adj["ms"]["API"], "\\a.mu.ʁø\\")
        self.assertEqual(nouvel_adj["mp"]["API"], "\\a.mu.ʁø\\")
        self.assertEqual(nouvel_adj["fs"]["API"], "\\a.mu.ʁøz\\")
        self.assertEqual(nouvel_adj["fp"]["API"], "\\a.mu.ʁøz\\")

    def test_recup_adjectif_2(self):
        nouvel_adj = wikitionnaire.recup_adjectif("beau")
        self.assertEqual(nouvel_adj["ms"]["mot"], "beau")
        self.assertEqual(nouvel_adj["mp"]["mot"], "beaux")
        self.assertEqual(nouvel_adj["fs"]["mot"], "belle")
        self.assertEqual(nouvel_adj["fp"]["mot"], "belles")

        self.assertEqual(nouvel_adj["ms"]["nb_syllabes"], 1)
        self.assertEqual(nouvel_adj["mp"]["nb_syllabes"], 1)
        self.assertEqual(nouvel_adj["fs"]["nb_syllabes"], 1)
        self.assertEqual(nouvel_adj["fp"]["nb_syllabes"], 1)

        self.assertEqual(nouvel_adj["ms"]["API"], "\\bo\\")
        self.assertEqual(nouvel_adj["mp"]["API"], "\\bo\\")
        self.assertEqual(nouvel_adj["fs"]["API"], "\\bɛl\\")
        self.assertEqual(nouvel_adj["fp"]["API"], "\\bɛl\\")

    def test_recup_adjectif_3(self):
        nouvel_adj = wikitionnaire.recup_adjectif("politique")
        self.assertEqual(nouvel_adj["ms"]["mot"], "politique")
        self.assertEqual(nouvel_adj["mp"]["mot"], "politiques")
        self.assertEqual(nouvel_adj["fs"]["mot"], "politique")
        self.assertEqual(nouvel_adj["fp"]["mot"], "politiques")

        self.assertEqual(nouvel_adj["ms"]["nb_syllabes"], 3)
        self.assertEqual(nouvel_adj["mp"]["nb_syllabes"], 3)
        self.assertEqual(nouvel_adj["fs"]["nb_syllabes"], 3)
        self.assertEqual(nouvel_adj["fp"]["nb_syllabes"], 3)

        self.assertEqual(nouvel_adj["ms"]["API"], "\\pɔ.li.tik\\")
        self.assertEqual(nouvel_adj["mp"]["API"], "\\pɔ.li.tik\\")
        self.assertEqual(nouvel_adj["fs"]["API"], "\\pɔ.li.tik\\")
        self.assertEqual(nouvel_adj["fp"]["API"], "\\pɔ.li.tik\\")

    def test_recup_nom_1(self):
        nouveau_nom = wikitionnaire.recup_nom("voix")
        self.assertEqual(nouveau_nom[0]["mot"], "voix")
        self.assertEqual(nouveau_nom[1]["mot"], "voix")

        self.assertEqual(nouveau_nom[0]["genre"], "f")
        self.assertEqual(nouveau_nom[0]["nombre"], "s")
        self.assertEqual(nouveau_nom[1]["genre"], "f")
        self.assertEqual(nouveau_nom[1]["nombre"], "p")

        self.assertEqual(nouveau_nom[0]["nb_syllabes"], 1)
        self.assertEqual(nouveau_nom[1]["nb_syllabes"], 1)

        self.assertEqual(nouveau_nom[0]["API"], "\\vwa\\")
        self.assertEqual(nouveau_nom[1]["API"], "\\vwa\\")

    def test_recup_nom_2(self):
        nouveau_nom = wikitionnaire.recup_nom("amant")
        self.assertEqual(nouveau_nom[0]["mot"], "amant")
        self.assertEqual(nouveau_nom[1]["mot"], "amants")

        self.assertEqual(nouveau_nom[0]["genre"], "m")
        self.assertEqual(nouveau_nom[0]["nombre"], "s")
        self.assertEqual(nouveau_nom[1]["genre"], "m")
        self.assertEqual(nouveau_nom[1]["nombre"], "p")

        self.assertEqual(nouveau_nom[0]["nb_syllabes"], 2)
        self.assertEqual(nouveau_nom[1]["nb_syllabes"], 2)

        self.assertEqual(nouveau_nom[0]["API"], "\\a.mɑ̃\\")
        self.assertEqual(nouveau_nom[1]["API"], "\\a.mɑ̃\\")

    def test_recup_nom_3(self):
        nouveau_nom = wikitionnaire.recup_nom("tendresse")
        self.assertEqual(nouveau_nom[0]["mot"], "tendresse")
        self.assertEqual(nouveau_nom[1]["mot"], "tendresses")

        self.assertEqual(nouveau_nom[0]["genre"], "f")
        self.assertEqual(nouveau_nom[0]["nombre"], "s")
        self.assertEqual(nouveau_nom[1]["genre"], "f")
        self.assertEqual(nouveau_nom[1]["nombre"], "p")

        self.assertEqual(nouveau_nom[0]["nb_syllabes"], 2)
        self.assertEqual(nouveau_nom[1]["nb_syllabes"], 2)

        self.assertEqual(nouveau_nom[0]["API"], "\\tɑ̃.dʁɛs\\")
        self.assertEqual(nouveau_nom[1]["API"], "\\tɑ̃.dʁɛs\\")

    def test_recup_nom_4(self):
        nouveau_nom = wikitionnaire.recup_nom("vie")
        self.assertEqual(nouveau_nom[0]["mot"], "vie")
        self.assertEqual(nouveau_nom[1]["mot"], "vies")

        self.assertEqual(nouveau_nom[0]["genre"], "f")
        self.assertEqual(nouveau_nom[0]["nombre"], "s")
        self.assertEqual(nouveau_nom[1]["genre"], "f")
        self.assertEqual(nouveau_nom[1]["nombre"], "p")

        self.assertEqual(nouveau_nom[0]["nb_syllabes"], 1)
        self.assertEqual(nouveau_nom[1]["nb_syllabes"], 1)

        self.assertEqual(nouveau_nom[0]["API"], "\\vi\\")
        self.assertEqual(nouveau_nom[1]["API"], "\\vi\\")

    def test_recup_nom_5(self):
        nouveau_nom = wikitionnaire.recup_nom("gars")
        self.assertEqual(nouveau_nom[0]["mot"], "gars")
        self.assertEqual(nouveau_nom[1]["mot"], "gars")

        self.assertEqual(nouveau_nom[0]["genre"], "m")
        self.assertEqual(nouveau_nom[0]["nombre"], "s")
        self.assertEqual(nouveau_nom[1]["genre"], "m")
        self.assertEqual(nouveau_nom[1]["nombre"], "p")

        self.assertEqual(nouveau_nom[0]["nb_syllabes"], 1)
        self.assertEqual(nouveau_nom[1]["nb_syllabes"], 1)

        self.assertEqual(nouveau_nom[0]["API"], "\\ga\\")
        self.assertEqual(nouveau_nom[1]["API"], "\\ga\\")

    def test_recup_determinant_1(self):
        dict_det = wikitionnaire.recup_determinant("le")
        self.assertEqual(dict_det["ms"]["mot"], "le")
        self.assertEqual(dict_det["mp"]["mot"], "les")
        self.assertEqual(dict_det["fs"]["mot"], "la")
        self.assertEqual(dict_det["fp"]["mot"], "les")

        self.assertEqual(dict_det["ms"]["nb_syllabes"], 1)
        self.assertEqual(dict_det["mp"]["nb_syllabes"], 1)
        self.assertEqual(dict_det["fs"]["nb_syllabes"], 1)
        self.assertEqual(dict_det["fp"]["nb_syllabes"], 1)

        self.assertEqual(dict_det["ms"]["API"], "\\lə\\")
        self.assertEqual(dict_det["mp"]["API"], "\\le\\")
        self.assertEqual(dict_det["fs"]["API"], "\\la\\")
        self.assertEqual(dict_det["fp"]["API"], "\\le\\")

    def test_recup_determinant_2(self):
        dict_det = wikitionnaire.recup_determinant("ce")
        self.assertEqual(dict_det["ms"]["mot"], "ce")
        self.assertEqual(dict_det["mp"]["mot"], "ces")
        self.assertEqual(dict_det["fs"]["mot"], "cette")
        self.assertEqual(dict_det["fp"]["mot"], "ces")

        self.assertEqual(dict_det["ms"]["nb_syllabes"], 1)
        self.assertEqual(dict_det["mp"]["nb_syllabes"], 1)
        self.assertEqual(dict_det["fs"]["nb_syllabes"], 1)
        self.assertEqual(dict_det["fp"]["nb_syllabes"], 1)

        self.assertEqual(dict_det["ms"]["API"], "\\sə\\")
        self.assertEqual(dict_det["mp"]["API"], "\\se\\")
        self.assertEqual(dict_det["fs"]["API"], "\\sɛt\\")
        self.assertEqual(dict_det["fp"]["API"], "\\se\\")

    def test_recup_determinant_3(self):
        dict_det = wikitionnaire.recup_determinant("mon")
        self.assertEqual(dict_det["ms"]["mot"], "mon")
        self.assertEqual(dict_det["mp"]["mot"], "mes")
        self.assertEqual(dict_det["fs"]["mot"], "ma")
        self.assertEqual(dict_det["fp"]["mot"], "mes")

        self.assertEqual(dict_det["ms"]["nb_syllabes"], 1)
        self.assertEqual(dict_det["mp"]["nb_syllabes"], 1)
        self.assertEqual(dict_det["fs"]["nb_syllabes"], 1)
        self.assertEqual(dict_det["fp"]["nb_syllabes"], 1)

        self.assertEqual(dict_det["ms"]["API"], "\\mɔ̃\\")
        self.assertEqual(dict_det["mp"]["API"], "\\mɛ\\")
        self.assertEqual(dict_det["fs"]["API"], "\\ma\\")
        self.assertEqual(dict_det["fp"]["API"], "\\mɛ\\")

    def test_recup_determinant_4(self):
        dict_det = wikitionnaire.recup_determinant("aucun")
        self.assertEqual(dict_det["ms"]["mot"], "aucun")
        self.assertEqual(dict_det["mp"]["mot"], "aucuns")
        self.assertEqual(dict_det["fs"]["mot"], "aucune")
        self.assertEqual(dict_det["fp"]["mot"], "aucunes")

        self.assertEqual(dict_det["ms"]["nb_syllabes"], 2)
        self.assertEqual(dict_det["mp"]["nb_syllabes"], 2)
        self.assertEqual(dict_det["fs"]["nb_syllabes"], 2)
        self.assertEqual(dict_det["fp"]["nb_syllabes"], 2)

        self.assertEqual(dict_det["ms"]["API"], "\\o.kœ̃\\")
        self.assertEqual(dict_det["mp"]["API"], "\\o.kœ̃\\")
        self.assertEqual(dict_det["fs"]["API"], "\\o.kyn\\")
        self.assertEqual(dict_det["fp"]["API"], "\\o.kyn\\")

class TestDatabase(unittest.TestCase):
    
    def setUp(self):
        # DB temporaire dans la mémoire pour le temps des tests
        self.db = TinyDB(storage=MemoryStorage)
        self.User = Query()
    
    def test_1(self):
        # Example de test
        self.db.insert({'name': 'John', 'age': 22})
        req = self.db.search(self.User.name == 'John')
        self.assertEqual(req, [{'name': 'John', 'age': 22}])


if __name__ == "__main__":
    unittest.main()
