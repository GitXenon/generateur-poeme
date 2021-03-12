import unittest
from main import nombre_syllables
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


class Test_wikitionnaire(unittest.TestCase):
    def test_wikitionnaire_1(self):
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

    def test_wikitionnaire_2(self):
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

    def test_wikitionnaire_3(self):
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


if __name__ == "__main__":
    unittest.main()
