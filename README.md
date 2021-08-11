<p align="center">
    <a href="http://choosealicense.com/licenses/mit/"><img src="https://img.shields.io/badge/license-MIT-3C93B4.svg?style=flat" alt="MIT License"></a>
    <a href="https://github.com/psf/black"><img src="https://img.shields.io/badge/code%20style-black-000000.svg" alt="Code style: black"></a>
    <br />
    <br />
    <i>Une implémentation d'une grammaire non contextuelle en Python pour générer des poèmes</i>
    <br />
<br />
    <i><b>Auteur</b>:
        <a href="https://github.com/GitXenon">Xavier B.</a>
    </i>
<br />
</p>
<hr />
 Les phrases ont pour comme structure:
```
phrase :=  [groupe_verbal | groupe_nominal]
groupe_verbal := groupe_prepositionnel " " verbe " " groupe_nominal
groupe_nominal := determinant " " adjectif " " nom
groupe_prepositionnel := preposition " " groupe_nominal
determinant :=  "le"
                | "la"
                | ...
nom :=          "français"
                |"sublime"
                |...
adjectif :=     "énumérateur"
                |"caméléonesque"
                |...
...
```

La sémantique des phrases n'est pas tout à fait parfaite pour l'instant :
```python
>>> python main.py
Dans lui nulles explication attendis il certain
>>> python main.py
Celui lurent que auquel
```

### Et dans le futur ?
Nous sommes en 2024, les derniers poètes restant doivent maintenant travailler pour RoboPoème3000, l'ultime robot créateur de poème. Mon programme est devenu conscient et plus rien ne peut l'arrêter.

En réalité, je m'attends à construire une interface CLI pour mon programme, créer de nouvelles fonctions générateur de poèmes plus poussées et peut-être générer du code HTML pour visualiser les poèmes. Peut-être générer des poèmes selon un thème.