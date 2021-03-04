# Générateur de poème

Une implémentation de Recursive Transition Networks en Python pour générer des (terribles) poèmes. Pour l'instant il reste beaucoup de travail. Les phrases ont pour comme structure:
```
phrase::  determinant nom
determinant::"le"
            | "la"
            | ...
nom::"français"
    |...
...
```
Une seule fonction est implémenter pour l'instant, celle de générer des poèmes rimés style AABB.
```python
>>> python main.py
l'abime
ton cybercrime
un français
une plaie
```

### Et dans le futur ?
Nous sommes en 2024, les derniers poètes restant doivent maintenant travailler pour RoboPoème3000, l'ultime robot créateur de poème. Mon programme est devenu conscient et plus rien ne peut l'arrêter.

En réalité, je m'attends à construire une interface CLI pour mon programme, créer de nouvelles fonctions générateur de poèmes plus poussées et peut-être générer du code HTML pour visualiser les poèmes. Peut-être générer des poèmes selon un thème.