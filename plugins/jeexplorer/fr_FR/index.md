---
title: Jeedom | Plugin JeeXplorer
description: Explorateur / éditeur de fichiers pour Jeedom
---

<img align="right" src="../images/jeexplorer_icon.png" width="100">

# JeeXplorer - Plugin pour Jeedom

Explorateur / éditeur de fichiers pour Jeedom.

[Changelog](changelog.md)<br />

## Configuration du plugin JeeXplorer

Après installation du plugin, il vous suffit de l’activer.
Il apparaitra alors dans le menu *Plugins > Programmation*

Vous pouvez également:
- Changer la langue de l'explorateur de fichiers.
- Ouvrir l'explorateur sur le dernier répertoire consulté.
- Collapser le code à l'ouverture des fichiers.
- Vérifier les versions des librairies utilisées.

{% include lightbox.html src="jeexplorer/images/config_03.jpg" data="jeexplorer" title="Configuration" imgstyle="width:550px;display: block;margin: 0 auto;" %}

## Explorateur de fichiers

Le plugin propose assez simplement un explorateur de fichier.

Sur la droite, en haut, vous trouverez une zone *Places* vous permettant de stocker des raccourcis.
En dessous, la liste des dossiers

Dans la fenêtre de droite, les sous-dossiers et les fichiers.

Vous pouvez créer, supprimer, renommer, éditer etc des dossiers et fichiers grâce aux options dans la barre du haut, et au clic droit sur les dossiers/fichiers.

{% include lightbox.html src="jeexplorer/images/jeexplorer_screenshot4.jpg" data="jeexplorer" title="Explorateur" imgstyle="width:550px;display: block;margin: 0 auto;" %}

#### Sur l'édition d'un fichier, vous pouvez rechercher dans son contenu:

{% include lightbox.html src="jeexplorer/images/jeexplorer_screenshot3.jpg" data="jeexplorer" title="Search" imgstyle="width:550px;display: block;margin: 0 auto;" %}

- Rechercher : Ctrl + F puis Enter
- Résultat suivant : Ctrl + G
- Résultat précédent : Ctrl + Shift + G

#### Code Folding:

- Ctrl + Y : fermer tout les blocs collapsables
- Ctrl + I : ouvrir tout les blocs collapsables

*Nous ne voyons pas d'autres explications ...*


## Attention

Comme tout explorateur de fichiers, celui-ci vous permet d'accéder et d'éditer tous les fichiers présent dans le répertoire racine de Jeedom.
Attention donc aux mauvaises manipulations qui pourraient rendre votre Jeedom complètement inopérant !

### Pour rappel, voici la structure des dossiers:

- 3rdparty : dossier comprenant les librairies externe utilisées par Jeedom (Jquery, CodeMirror, etc).
- backup : dossier de vos sauvegardes de Jeedom (à toujours dupliquer sur un autre système !)
- core : dossier comprenant le moteur de Jeedom, le Core, et toutes ses fonctions internes.
- data : dossier comprenant vos données (Rapports, Vues, css/js de PErsonnalisation Avancée, Design 3D, etc).
- desktop : dossier comprenant toutes les pages affichées (l'interface) en desktop et leurs fonctions.
- docs : documentation.
- install : fichiers d'installation de Jeedom.
- log : dossier comprenant tous les logs (http.error, update, etc) et ceux des scénarios (sous-dossier scenarioLog, nommés par id)
- mobile : dossier comprenant toutes les pages affichées (l'interface webapp) en mobile et leurs fonctions.
- plugins : dossier comprenant tout les plugins installés.
- script :
- support :
- vendor :

Les configurations de Jeedom et de vos plugins sont, elles, stockées en base de données.

Vous pouvez bien sûr créer votre propre dossier, comprenant vos scripts, librairies etc.
