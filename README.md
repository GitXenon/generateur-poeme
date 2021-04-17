<p align="center">
    <a href="http://choosealicense.com/licenses/mit/"><img src="https://img.shields.io/badge/license-MIT-3C93B4.svg?style=flat" alt="MIT License"></a>
    <a href="https://github.com/psf/black"><img src="https://img.shields.io/badge/code%20style-black-000000.svg" alt="Code style: black"></a>
    <br />
    <br />
    <i>Une tentative d'un système automatisé pour générer des poèmes à l'aide d'un réseau de transition récursif</i>
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
phrase::  [groupe_verbal | groupe_nominal]
groupe_verbal:: groupe_prepositionnel " " verbe " " groupe_nominal
groupe_nominal:: determinant " " adjectif " " nom
groupe_prepositionnel:: preposition " " groupe_nominal
determinant::"le"
            | "la"
            | ...
nom::"français"
    |"sublime"
    |...
adjectif::"énumérateur"
         |"caméléonesque"
         |...
...
```
Quelques fonctions sont implémentés pour l'instant, comme générer un poème avec une structure de rime AABB ou ABAB ou ABBA.
```python
>>> python main.py
l'abime
ton cybercrime
un français
une plaie
```

J'ai aperçu rapidement qu'un des problèmes du projet est le manque de vocabulaire, ainsi que la possibilité d'avoir plusieurs caractéristiques des mots pour former des poèmes très complexes. Évidemment, il n'existe pas de dictionnaire en ligne assez sophistiqué pour mes besoins, je récupère donc les informations nécessaires sur wikitionnaire et j'ai quelques fonctions qui ajoutent des informations supplémentaires. Aussi, j'ai ajouté des fonctions tests, car le projet a pris une plus grosse tournure que j'avais initialement planifié.

### Et dans le futur ?
Nous sommes en 2024, les derniers poètes restant doivent maintenant travailler pour RoboPoème3000, l'ultime robot créateur de poème. Mon programme est devenu conscient et plus rien ne peut l'arrêter.

En réalité, je m'attends à construire une interface CLI pour mon programme, créer de nouvelles fonctions générateur de poèmes plus poussées et peut-être générer du code HTML pour visualiser les poèmes. Peut-être générer des poèmes selon un thème.