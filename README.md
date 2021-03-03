# Générateur de poème

Une implémentation de Recursive Transition Networks en Python pour générer des (terribles) poèmes. Pour l'instant il reste beaucoup de travail. Les phrases ont pour comme structure:
```
sentence::  determinant nom verbe determinant nom
determinant::"le"
            | "la"
            | ...
...
```

```python
>>> python main.py
le appétit apporte un mètre,
un appétit grandit cette coquille,
ta porte vit cet beurre,
cette crêpe gratte ta allumette
```