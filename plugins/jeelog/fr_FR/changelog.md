---
title: Jeedom | Plugin JeeLog
description: Plugin de journalisation d’activité
---

<img align="right" src="../images/jeelog_icon.png" width="100">

# JeeLog - Plugin pour Jeedom

## Changelog

*[Documentation](index.md)*

>*Remarque : en cas de mise à jour non listée ici, c'est que celle-ci ne comporte que des changements mineurs du type documentation ou corrections de bugs mineurs.*

- [Commits Github Beta](https://github.com/KiboOst/jeedom-jeelog/commits/beta)
- [Commits Github Stable V4](https://github.com/KiboOst/jeedom-jeelog/commits/stableV4)

### 27/11/2020
- Ajout de la possibilité de mettre des paramètres optionnel sur la tuile. Par exemple, mobile_class -> col2

### 03/03/2020
- Traduction du plugin en anglais (Jeedom V4).

### 06/09/2019
- Création de la version Stable Jeedom V4
- Passage de la beta sur Jeedom V4
>   *Pour Jeedom V3, restez dorénavant en version Stable. Le market sélectionne automatiquement la stable V3 ou V4 en fonction de votre version de Jeedom.*

### 05/02/2019
- Tuile redimensionnable depuis le dashboard.
- L'importation de commandes n'importe plus les commandes déjà présentes, pour éviter les doublons.

### 27/11/2018
  - Nouvelle option pour limiter le nombre de lignes pour les fichiers de log Jeedom.

### 26/11/2018
  - Ajout de la possibilité d'afficher un fichier de log Jeedom.
>   *Attention: Si vous ajoutez un fichier de log (bouton "Ajouter Log"), toutes les autre commandes et scénarios seront  supprimés du log quand vous sauvegarderez celui-ci. En effet, le fonctionnement n'est pas le même, puisque dans ce cas il  n'y a pas d’événement triés par date etc. mais simplement le continu du fichier.*

### 08/05/2018

  - Ajout d'une option pour afficher le détail des scénarios.
  - Ajout des options de couleur de fond et texte css pour les *designs* (rgba(0,0,0,0) pour fond transparent).
  - Les données de log sont maintenant enregistrées dans un fichier, et non plus dans la configuration de l'équipement.

### 03/05/2018

  - Ajout d'une option *Ne pas répéter* pour les commandes infos.
  - Bugfix: Erreur si commande ou scénario supprimé dans le log.

### 02/05/2018

  - Ajout d'une option pour le format de date dans le log (format php).
  - Import infos: bugfix #cmd#
  - Import infos: Ajout d'un champ Rechercher.
  - Import infos: Ajout d'un texte commande historisée ou non.
  - Ajout de logs en debug.
  - Mise à jour de la doc.

### 30/04/2018

- Ajout d'une option d'importation de commandes infos.
- Bugfix affichage de la checkbox *Inverser* sous Chrome.
- Nouvelle option pour afficher ou non la date/heure de mise à jour du log.

### 29/04/2018

- Ajout de l'option *Inverser* pour les commandes.
- Ajout 'Off / On' pour les commandes.
- Compatibilité avec les *designs*.
- Bugfix chemins nginx (merci Nebz !).
- Bugfix des noms vides sur les infos (affiche le nom de la commande).
- Corrections mineures.

### 27/04/2018

- Première version (Beta).
