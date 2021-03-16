import unittest
import tempfile

from tinydb import TinyDB, Query
from tinydb.storages import MemoryStorage

from context import poeme_generator

class TestNombreSyllable(unittest.TestCase):
    def test_syllable_1(self):
        self.assertEqual(poeme_generator.nombre_syllables("éléphant"), 3)
        self.assertEqual(poeme_generator.nombre_syllables("chameau"), 2)
        self.assertEqual(poeme_generator.nombre_syllables("boeuf"), 1)
        self.assertEqual(poeme_generator.nombre_syllables("crocodile"), 4)
        self.assertEqual(poeme_generator.nombre_syllables("hirondelle"), 4)

    def test_syllable_2(self):
        self.assertEqual(poeme_generator.nombre_syllables("garçon"), 2)
        self.assertEqual(poeme_generator.nombre_syllables("informer"), 3)
        self.assertEqual(poeme_generator.nombre_syllables("argent"), 2)
        self.assertEqual(poeme_generator.nombre_syllables("expert"), 2)

    def test_syllable_3(self):
        self.assertEqual(poeme_generator.nombre_syllables("pomme"), 2)
        self.assertEqual(poeme_generator.nombre_syllables("terre"), 2)
        self.assertEqual(poeme_generator.nombre_syllables("tasse"), 2)
        self.assertEqual(poeme_generator.nombre_syllables("accident"), 3)
        self.assertEqual(poeme_generator.nombre_syllables("apprendre"), 3)

    def test_syllable_4(self):
        self.assertEqual(poeme_generator.nombre_syllables("montre"), 2)
        self.assertEqual(poeme_generator.nombre_syllables("capable"), 2)

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
