---
title: Jeedom | Plugin Qivivo
description: Intégration du Thermostat Qivivo.
---

<img align="right" src="../images/qivivo_icon.png" width="100">

# Qivivo - Plugin pour Jeedom

Intégration du Thermostat [Qivivo.](https://www.qivivo.com/fr/)

## Changelog

*[Documentation](index.md)*

>*En cas de mise à jour non listée ici, c'est que celle-ci ne comporte que des changements mineurs du type documentation ou corrections de bugs mineurs.*

### 15/01/2019
- Ajout de l'attribut *data-category* sur les tuiles.

### 11/01/2019
- Amélioration des tuiles des modules sur le dashboard/design
  - Flat design (iOS)
  - Compatibilité core 3.3.7

### 05/01/2019 Version Stable !
- Amélioration des tuiles d'affichage
- Tuiles *flat-design* sur les design sous iOS
- Ajout de la fonction *télécharger* dans la fenêtre d'import de programmes

### 04/01/2019 (beta)
- Export programme: date en début de nom de fichier pour éviter les doublons
- Les commandes du thermostat n'update plus l'info consigne (voir [doc](https://kiboost.github.io/jeedom_docs/plugins/qivivo/fr_FR/#utilisation))
- Ajustement des templates dashboard/mobile du thermostat

### 03/01/2019 (beta)
- Fonction d'import / export de programme

### 31/12/2018 (beta)
- Gestion d'erreurs API
  - Configuration *Répéter l'action*
  - Configuration *Actions sur erreur*
- Update de la doc

### 30/12/2018 (beta)
- Thermostat : nouvelle commande info *Chauffe*, historisée (0 ou ordre).

### 29/12/2018 (beta)
- Intégration API multi-zone
  - Changement des ordres des modules / zones
  - Création, édition, changement de programmes multiple par zone
  - Nommage des modules par zone

### 23/12/2018 (beta)
- Création de tuiles dédiées dashboard et mobile
- Commandes Thermostat -1, +1 degré pendant 2h, et annulation du programme temporaire 
- Ordre des module en français (plus court et lisible)
- Passerelle : Firmware et LastMsg (commandes info)
- cron15 (défaut) ou cron5 au choix
- Update de la doc

### 21/12/2018 (beta)

- Première version beta.
