import unittest

from context import wikitionnaire

class TestScrapingAdjectif(unittest.TestCase):

    def test_recup_adjectif_amoureux(self):
        nouvel_adj = wikitionnaire.recup_mot("amoureux", "adjectif")
        self.assertEqual(nouvel_adj[0]["mot"], "amoureux")
        self.assertEqual(nouvel_adj[1]["mot"], "amoureux")
        self.assertEqual(nouvel_adj[2]["mot"], "amoureuse")
        self.assertEqual(nouvel_adj[3]["mot"], "amoureuses")

        self.assertEqual(nouvel_adj[0]["nb_syllabes"], 3)
        self.assertEqual(nouvel_adj[1]["nb_syllabes"], 3)
        self.assertEqual(nouvel_adj[2]["nb_syllabes"], 3)
        self.assertEqual(nouvel_adj[3]["nb_syllabes"], 3)

        self.assertEqual(nouvel_adj[0]["API"], "\\a.mu.ʁø\\")
        self.assertEqual(nouvel_adj[1]["API"], "\\a.mu.ʁø\\")
        self.assertEqual(nouvel_adj[2]["API"], "\\a.mu.ʁøz\\")
        self.assertEqual(nouvel_adj[3]["API"], "\\a.mu.ʁøz\\")

    def test_recup_adjectif_beau(self):
        nouvel_adj = wikitionnaire.recup_mot("beau", "adjectif")
        self.assertEqual(nouvel_adj[0]["mot"], "beau")
        self.assertEqual(nouvel_adj[1]["mot"], "beaux")
        self.assertEqual(nouvel_adj[2]["mot"], "belle")
        self.assertEqual(nouvel_adj[3]["mot"], "belles")

        self.assertEqual(nouvel_adj[0]["nb_syllabes"], 1)
        self.assertEqual(nouvel_adj[1]["nb_syllabes"], 1)
        self.assertEqual(nouvel_adj[2]["nb_syllabes"], 1)
        self.assertEqual(nouvel_adj[3]["nb_syllabes"], 1)

        self.assertEqual(nouvel_adj[0]["API"], "\\bo\\")
        self.assertEqual(nouvel_adj[1]["API"], "\\bo\\")
        self.assertEqual(nouvel_adj[2]["API"], "\\bɛl\\")
        self.assertEqual(nouvel_adj[3]["API"], "\\bɛl\\")

    def test_recup_adjectif_politique(self):
        nouvel_adj = wikitionnaire.recup_mot("politique", "adjectif")
        self.assertEqual(nouvel_adj[0]["mot"], "politique")
        self.assertEqual(nouvel_adj[1]["mot"], "politiques")
        self.assertEqual(nouvel_adj[2]["mot"], "politique")
        self.assertEqual(nouvel_adj[3]["mot"], "politiques")

        self.assertEqual(nouvel_adj[0]["nb_syllabes"], 3)
        self.assertEqual(nouvel_adj[1]["nb_syllabes"], 3)
        self.assertEqual(nouvel_adj[2]["nb_syllabes"], 3)
        self.assertEqual(nouvel_adj[3]["nb_syllabes"], 3)

        self.assertEqual(nouvel_adj[0]["API"], "\\pɔ.li.tik\\")
        self.assertEqual(nouvel_adj[1]["API"], "\\pɔ.li.tik\\")
        self.assertEqual(nouvel_adj[2]["API"], "\\pɔ.li.tik\\")
        self.assertEqual(nouvel_adj[3]["API"], "\\pɔ.li.tik\\")

    def test_recup_adjectif_mot_inexistant(self):
        dict_nom = wikitionnaire.recup_mot("kfajrijflp", "adjectif")
        self.assertEqual(dict_nom, None)

class TestScrapingNom(unittest.TestCase):
    
    def test_recup_nom_mot_inexistant(self):
        dict_nom = wikitionnaire.recup_mot("kfajrijflp", 'nom')
        self.assertEqual(dict_nom, None)

    def test_recup_nom_voix(self):
        nouveau_nom = wikitionnaire.recup_mot("voix", 'nom')
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

    def test_recup_nom_amant(self):
        nouveau_nom = wikitionnaire.recup_mot("amant", 'nom')
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

    def test_recup_nom_tendresse(self):
        nouveau_nom = wikitionnaire.recup_mot("tendresse", 'nom')
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

    def test_recup_nom_vie(self):
        nouveau_nom = wikitionnaire.recup_mot("vie", 'nom')
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

    def test_recup_nom_gars(self):
        nouveau_nom = wikitionnaire.recup_mot("gars", "nom")
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

    def test_recup_nom_wc(self):
        dict_nom = wikitionnaire.recup_mot("w.-c.", "nom")
        self.assertEqual(dict_nom[0]["mot"], "w.-c.")
        self.assertEqual(dict_nom[0]["genre"], "m")
        self.assertEqual(dict_nom[0]["nombre"], "p")
        self.assertEqual(dict_nom[0]["nb_syllabes"], 2)
        self.assertEqual(dict_nom[0]["API"], "\\ve.se\\")

    def test_recup_nom_gomme(self):
        dict_nom = wikitionnaire.recup_mot("gomme", "nom")
        self.assertEqual(dict_nom[0]["mot"], "gomme")
        self.assertEqual(dict_nom[1]["mot"], "gommes")

        self.assertEqual(dict_nom[0]["genre"], "f")
        self.assertEqual(dict_nom[0]["nombre"], "s")

        self.assertEqual(dict_nom[1]["genre"], "f")
        self.assertEqual(dict_nom[1]["nombre"], "p")

        self.assertEqual(dict_nom[0]["nb_syllabes"], 1)
        self.assertEqual(dict_nom[1]["nb_syllabes"], 1)

        self.assertEqual(dict_nom[0]["API"], "\\ɡɔm\\")
        self.assertEqual(dict_nom[1]["API"], "\\ɡɔm\\")

    def test_recup_nom_rayure(self):
        dict_nom = wikitionnaire.recup_mot("rayure", "nom")
        self.assertEqual(dict_nom[0]["mot"], "rayure")
        self.assertEqual(dict_nom[1]["mot"], "rayures")

        self.assertEqual(dict_nom[0]["genre"], "f")
        self.assertEqual(dict_nom[0]["nombre"], "s")

        self.assertEqual(dict_nom[1]["genre"], "f")
        self.assertEqual(dict_nom[1]["nombre"], "p")

        self.assertEqual(dict_nom[0]["nb_syllabes"], 2)
        self.assertEqual(dict_nom[1]["nb_syllabes"], 2)
        
        self.assertEqual(dict_nom[0]["API"], "\\ʁɛ.jyʁ\\")
        self.assertEqual(dict_nom[1]["API"], "\\ʁɛ.jyʁ\\")

    def test_recup_nom_trampoline(self):
        dict_nom = wikitionnaire.recup_mot("trampoline", "nom")
        self.assertEqual(dict_nom[0]["mot"], "trampoline")
        self.assertEqual(dict_nom[1]["mot"], "trampolines")

        self.assertEqual(dict_nom[0]["genre"], "m") # En France, mais au Québec c'est féminin
        self.assertEqual(dict_nom[0]["nombre"], "s")

        self.assertEqual(dict_nom[1]["genre"], "m")
        self.assertEqual(dict_nom[1]["nombre"], "p")

        self.assertEqual(dict_nom[0]["nb_syllabes"], 3)
        self.assertEqual(dict_nom[1]["nb_syllabes"], 3)
        
        self.assertEqual(dict_nom[0]["API"], "\\tʁɑ̃.pɔ.lin\\")
        self.assertEqual(dict_nom[1]["API"], "\\tʁɑ̃.pɔ.lin\\")

class TestScrapingDeterminant(unittest.TestCase):

    def test_recup_determinant_mot_inexistant(self):
        dict_nom = wikitionnaire.recup_mot("kfajrijflp", "determinant")
        self.assertEqual(dict_nom, None)

    def test_recup_determinant_le(self):
        dict_det = wikitionnaire.recup_mot("le", "determinant")
        self.assertEqual(dict_det[0]["mot"], "le")
        self.assertEqual(dict_det[1]["mot"], "les")
        self.assertEqual(dict_det[2]["mot"], "la")
        self.assertEqual(dict_det[3]["mot"], "les")

        self.assertEqual(dict_det[0]["nb_syllabes"], 1)
        self.assertEqual(dict_det[1]["nb_syllabes"], 1)
        self.assertEqual(dict_det[2]["nb_syllabes"], 1)
        self.assertEqual(dict_det[3]["nb_syllabes"], 1)

        self.assertEqual(dict_det[0]["API"], "\\lə\\")
        self.assertEqual(dict_det[1]["API"], "\\le\\")
        self.assertEqual(dict_det[2]["API"], "\\la\\")
        self.assertEqual(dict_det[3]["API"], "\\le\\")

    def test_recup_determinant_ce(self):
        dict_det = wikitionnaire.recup_mot("ce", "determinant")
        self.assertEqual(dict_det[0]["mot"], "ce")
        self.assertEqual(dict_det[1]["mot"], "ces")
        self.assertEqual(dict_det[2]["mot"], "cette")
        self.assertEqual(dict_det[3]["mot"], "ces")

        self.assertEqual(dict_det[0]["nb_syllabes"], 1)
        self.assertEqual(dict_det[1]["nb_syllabes"], 1)
        self.assertEqual(dict_det[2]["nb_syllabes"], 1)
        self.assertEqual(dict_det[3]["nb_syllabes"], 1)

        self.assertEqual(dict_det[0]["API"], "\\sə\\")
        self.assertEqual(dict_det[1]["API"], "\\se\\")
        self.assertEqual(dict_det[2]["API"], "\\sɛt\\")
        self.assertEqual(dict_det[3]["API"], "\\se\\")

    def test_recup_determinant_mon(self):
        dict_det = wikitionnaire.recup_mot("mon", "determinant")
        self.assertEqual(dict_det[0]["mot"], "mon")
        self.assertEqual(dict_det[1]["mot"], "mes")
        self.assertEqual(dict_det[2]["mot"], "ma")
        self.assertEqual(dict_det[3]["mot"], "mes")

        self.assertEqual(dict_det[0]["nb_syllabes"], 1)
        self.assertEqual(dict_det[1]["nb_syllabes"], 1)
        self.assertEqual(dict_det[2]["nb_syllabes"], 1)
        self.assertEqual(dict_det[3]["nb_syllabes"], 1)

        self.assertEqual(dict_det[0]["API"], "\\mɔ̃\\")
        self.assertEqual(dict_det[1]["API"], "\\mɛ\\")
        self.assertEqual(dict_det[2]["API"], "\\ma\\")
        self.assertEqual(dict_det[3]["API"], "\\mɛ\\")

    def test_recup_determinant_aucun(self):
        dict_det = wikitionnaire.recup_mot("aucun", "determinant")
        self.assertEqual(dict_det[0]['mot'], "aucun")
        self.assertEqual(dict_det[1]['mot'], "aucuns")
        self.assertEqual(dict_det[2]['mot'], "aucune")
        self.assertEqual(dict_det[3]['mot'], "aucunes")

        self.assertEqual(dict_det[0]['genre'], "m")
        self.assertEqual(dict_det[1]['genre'], "m")
        self.assertEqual(dict_det[2]['genre'], "f")
        self.assertEqual(dict_det[3]['genre'], "f")
        
        self.assertEqual(dict_det[0]['nombre'], "s")
        self.assertEqual(dict_det[1]['nombre'], "p")
        self.assertEqual(dict_det[2]['nombre'], "s")
        self.assertEqual(dict_det[3]['nombre'], "p")

        self.assertEqual(dict_det[0]["nb_syllabes"], 2)
        self.assertEqual(dict_det[1]["nb_syllabes"], 2)
        self.assertEqual(dict_det[2]["nb_syllabes"], 2)
        self.assertEqual(dict_det[3]["nb_syllabes"], 2)

        self.assertEqual(dict_det[0]["API"], "\\o.kœ̃\\")
        self.assertEqual(dict_det[1]["API"], "\\o.kœ̃\\")
        self.assertEqual(dict_det[2]["API"], "\\o.kyn\\")
        self.assertEqual(dict_det[3]["API"], "\\o.kyn\\")

    def test_recup_determinant_un(self):
        dict_det = wikitionnaire.recup_mot("un", "determinant")
        self.assertEqual(dict_det[0]['mot'], "un")
        self.assertEqual(dict_det[1]['mot'], "une")

        self.assertEqual(dict_det[0]["nb_syllabes"], 1)
        self.assertEqual(dict_det[1]["nb_syllabes"], 1)

        self.assertEqual(dict_det[0]["API"], "\\œ̃\\")
        self.assertEqual(dict_det[1]["API"], "\\yn\\")