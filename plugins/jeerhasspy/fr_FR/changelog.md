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

- [Commits Github Beta](https://github.com/KiboOst/jeedom-jeerhasspy/commits/beta)
- [Commits Github Stable](https://github.com/KiboOst/jeedom-jeerhasspy/commits/master)


### 30/05/2020
- Support du TTS simultané sur plusieurs devices (site1,site2).

### 19/04/2020
- **Attention**: Le plugin supporte maintenant Rhasspy v2.5 minimum !
- Ajouter un satellite : récupération automatique du siteId et vérifications.
- New : Deux nouvelles commandes sur les devices Rhasspy:
	- ledOn : Allume les LEDs
	- ledOff : Etaint les LEDs
	Nécessite [HermesLedControl](https://github.com/project-alice-assistant/HermesLedControl/wiki)
	*Il faut réimporter l'assistant pour créer ces nouvelles commandes*

### 06/03/2020
- Support du moteur d'interaction de Jeedom.

### 03/03/2020
- Traduction du plugin en anglais (Jeedom V4).

### 02/02/2020
- Gestion manuelle des satellites.
    - Ajout / Suppression.
    - Édition automatique du profile Rhasspy.

### 31/01/2020
- Support expérimental des satellites.
Ils sont crée automatiquement suite à une demande sur chaque satellite.<br />
Il faut paramétrer manuellement le profile de chaque satellite : voir [doc](https://kiboost.github.io/jeedom_docs/plugins/jeerhasspy/fr_FR/#configuration-rhasspy)

### 19/01/2020
- Bug fix : Commande Ask.

### 16/01/2020
- New : Vue d'ensemble des Intentions.

### 15/01/2020
- New : Confidence minimale sur les Intents pour l’exécution du scénario callback.

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
