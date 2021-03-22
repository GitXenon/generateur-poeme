import unittest

from tinydb import TinyDB, Query
from tinydb.storages import MemoryStorage

from context import poeme_generator
from context import wikitionnaire

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
    
    def test_double_1(self):
        wikitionnaire.ajouter_dans_DB('amour', 'nom', self.db) # On ajoute le nom amour
        Nom = self.db.table('nom') # Une table contenant tous les noms
        liste_nom = Nom.all() # On fait une copie de tous les noms dans la db
        wikitionnaire.ajouter_dans_DB('amour', 'nom', self.db) # On ajoute le même nom qu'au début
        self.assertEqual(Nom.all(), liste_nom) # On vérifie que la liste de tous les noms n'a pas changé
    
    def test_double_2(self):
        wikitionnaire.ajouter_dans_DB('de', 'determinant', self.db)
        Det = self.db.table('determinant')
        liste_det = Det.all()
        wikitionnaire.ajouter_dans_DB('de', 'determinant', self.db)
        self.assertEqual(Det.all(), liste_det)

    def test_double_2(self):
        wikitionnaire.ajouter_dans_DB('intelligent', 'adjectif', self.db)
        Adj = self.db.table('adjectif')
        liste_adj = Adj.all()
        wikitionnaire.ajouter_dans_DB('intelligent', 'adjectif', self.db)
        self.assertEqual(Adj.all(), liste_adj)


if __name__ == "__main__":
    unittest.main()
