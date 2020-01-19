---
title: Jeedom | Plugin JeeRhasspy
description: Plugin pour le support de l'assistant vocal Rhasspy dans Jeedom
---

<img align="right" src="../images/jeerhasspy_icon.png" width="100">

# JeeRhasspy - Plugin pour Jeedom

Plugin pour le support de l'assistant vocal [Rhasspy](https://rhasspy.readthedocs.io/en/latest/) dans Jeedom.

## Changelog

*[Documentation](index.md)*

>*Remarque : en cas de mise à jour non listée ici, c'est que celle-ci ne comporte que des changements mineurs du type documentation ou corrections de bugs mineurs.*

### 19/01/2020
- Bug fix : Commande Ask.

### 16/01/2020
- New : Vue d'ensemble des Intentions.

### 15/01/2020
- New : Confidence minimale sur les Intents pour l'éxécution du scénario callback.

### 04/01/2020
- New : Configuration automatique de Rhasspy depuis le panel Assistant.

### 01/01/2020
- Mise à jour de la [Documentation](index.md).
- BugFix : Option *Filtrer les Intents Jeedom*.
- New : Affichage des intentions par groupes, comme les scénarios.
- New : Ajout d'un bouton sur la configuration des Intentions pour ouvrir le scénario callback dans un autre onglet.
- New : Variables rhasspyWakeWord / rhasspyWakeSiteId.

*Il faut éditer votre profile rhasspy pour bénéficier de cette fonction, voir [Documentation](index.md).*

### 28/12/2019
- New : commande *ask* voir [Documentation](index.md).

*Il faut réimporter l'assistant pour créer la commande sur le device Rhasspy*

### 22/12/2019
- New : commande *dynamic Speak* sur les devices Rhasspy.

*Il faut réimporter l'assistant pour créer la commande sur le device Rhasspy*

### 20/12/2019
- Première version (Beta).


## TODO
En attente de Rhasspy:
- Builtin Slots (Duration, DateTime, Number, etc.) -> slot duration totalMinutes pour les DANS
- Config Master / Satellite -> Commande speak avec siteid variable

