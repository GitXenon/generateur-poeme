# Générateur de poème
[![Coverage Status](https://coveralls.io/repos/github/GitXenon/generateur-poeme/badge.svg?branch=main)](https://coveralls.io/github/GitXenon/generateur-poeme?branch=main)

Une implémentation de Recursive Transition Networks en Python pour générer des (terribles) poèmes. Pour l'instant il reste beaucoup de travail. Les phrases ont pour comme structure:
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