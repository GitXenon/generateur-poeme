import unittest

from tinydb import TinyDB, Query

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

class TestGroupe(unittest.TestCase):

    def setUp(self):
        self.db = TinyDB('db.json')

    def test_groupe_nominal_1(self):
        Nom = self.db.table('nom')
        Determinant = self.db.table('determinant')
        dict_nom = Nom.all()[0] # mot: amour
        dict_determinant = Determinant.all()[0] # mot: le/la/les
        gn = groupe_nominal(dict_determinant, dict_nom)
        self.assertEqual(gn, "l'amour")
        self.db.close()
    
    def test_groupe_nominal_2(self):
        Nom = self.db.table('nom')
        Determinant = self.db.table('determinant')
        dict_nom = Nom.all()[6] # mot: désir
        dict_determinant = Determinant.all()[2] # mot: ton/ta/tes
        gn = groupe_nominal(dict_determinant, dict_nom)
        print(gn)
        self.assertEqual(gn, "ton désir")
        self.db.close()


if __name__ == "__main__":
    unittest.main()
