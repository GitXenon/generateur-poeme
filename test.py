import unittest
from main import nombre_syllables

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

if __name__ == '__main__':
    unittest.main()
