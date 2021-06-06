# Création d'un lexique

* Décideur: Xavier Bussière
* Date: 2021-06-06

## Contexte et énoncé du problème

Un poème est une forme de texte, ce qui nécessite des mots pour former les phrases qu'il contient. Il faut donc donner à notre programme un vocabulaire pour qu'il puisse s'exprimer.

## Options envisagées

* Entrer manuellement des mots
* Prendre l'information automatiquement d'Antidote
* Prendre l'information automatiquement de Wikitionnaire
* Utilisé un lexicon déjà existant

## Résultat de la décision

Option choisie: Nous avons choisi d'**utiliser un lexique déjà existant**, soit le *Lefff* (Lexique des Formes Fléchies du Français). Nous avons choisi cette option puisque cette option coupe de plusieurs heures le travail nécessaire pour la création d'un lexique. Nous avons qu'à apprendre comment se servir du lexique pour remplir la structure de phrase voulue. Pour trouver la rime d'un mot, une décision future pourrait se prendre quant à concevoir une solution hybride avec notre méthode Wikitionnaire et le *Lefff*.

### Entrer manuellement des mots

Au début du projet, nous avons débuté par cette option puisqu'elle nécessite le moins de temps technique et le moins de réflexion. Cette option était exploratoire pour mieux comprendre la méthode la plus efficace pour stocker les mots.

✔️  Nécessite aucune programmation 

❌  Prend beaucoup de temps

❌  N'échelle (*scale*) pas bien

### Prendre l'information automatiquement d'Antidote

Antidote est un logiciel tout inclus pour la rédaction du français. Il y a des dictionnaires et une fonction recherche très avancée qui permet de chercher les mots par le nombre de syllabes, la rime, niveau de langue, domaine du mot, etc. Il serait donc très facile de former des poèmes très personnalisés. Par contre, après quelques recherches, Antidote (sur Windows) n'a aucun API pour accéder à ces informations. De plus, il est presque impossible pour un programme de "grimper" (*crawl*) puisque son interface utilisateur n'est pas structurée. Avec *Accessibility Insights* de Microsoft, nous avons remarqué qu'il n'y a aucun lien entre les différents éléments du programme, ce qui le rend impossible à être contrôlé à moins d'utiliser du *computer vision*, comme OpenCV.

✔️  Beaucoup de caractéristiques avec les mots

❌  Nécessite beaucoup de temps technique, accumule une dette technique pour s'assurer que tout fonctionne

❌  Nécessite Antidote installé sur l'ordinateur, n'est pas un logiciel gratuit

❌  Très difficile de retirer de l'information du logiciel

### Prendre l'information automatiquement de Wikitionnaire

Pour notre première tentative d'automatisation de la tâche, nous avons utilisé le site Wikitionnaire pour trouver les caractéristiques d'un mot donné et ensuite les entrées dans une base de données. Il était encore nécessaire d'entrer les mots voulus, mais maintenant les informations s'entraient automatiquement dans la base de données et entraient aussi les différentes formes du mot (masculin, féminin, singulier et pluriel). Avec cette option, il était possible de trouver la structure de rime du mot avec l'alphabet phonétique internationale (API). Par contre, il y avait différents problèmes avec certains mots, ce qui nécessitait de modifier notre code pour contenir les exceptions.

✔️  Adapté à nos besoins

❌  Nécessite beaucoup de temps technique, accumule une dette technique pour s'assurer que tout fonctionne

❌  N'inclus pas tous les mots du dictionnaire français

### Utilisé un lexique déjà existant

Il existe déjà un lexique français distribué sous la licence gratuite LGPL-LR (Lesser General Public License For Linguistic Resources) intitulé *Lefff* (Lexique des Formes Fléchies du Français). Cette option comporte la grande majorité des mots français, ce qui nous facilite le travail. Nous avons déjà écrit du code pour l'option Wikitionnaire, ce qui va devoir être remplacé pour cette nouvelle option.

✔️  Grande majorité du travail préalablement accompli

✔️  Licence gratuite LGPL-LR

➖  Manque l'alphabet phonétique pour la prononciation des mots

❌  Apprentissage nécessaire

❌  Restructuration du code actuel