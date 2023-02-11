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

### 11/02/2023
- Bug fix ouverture de la modale d'un équipement.
- Fin du support Core pré 4.2.


### 12/12/2021
- Compatibilité *event* Core 4.2.

*Il faut refaire la configuration des devices Rhasspy depuis le plugin (bouton orange sur chaque device)*.

### 21/02/2021
- On peut maintenant cliquer sur l'icône d'un device rhasspy pour éditer ses paramètres (Nom, Objet parent, Catégorie) et accéder à sa configuration avancée.
- Support des entities multiple. Si on demande d'allumer un slot house_room dans le salon et dans la cuisine, le tag #house_room# sera alors *salon,cuisine*.


### 20/02/2021
- Réécriture complète de la gestion interne des Intents. Ceux-ci ne sont plus enregistrés comme des *équipements* mais comme des *jeerhasspy_intent* à part entière, avec leur classe et leur table en DB.
- Migration des Intentions en DB à l'update du plugin.
- Suppression de l'objet Rhasspy-Intents, qui n'a plus lieu d'être !
- Les Devices rhasspy seront donc sans objet parents. Vous pouvez changer l'objet parent par le résumé domotique (Glisser/Déposer).

- Passage en stable de la beta du 18/02

### 18/02/2021
- **Nécessite de réimporter l'assistant dans le plugin.**
- **La commande SetVolume des devices rhasspy est maintenant de 0 à 100.**
- On peut maintenant renommer les devices Rhasspy (Dashboard, mode édition, ou résumé domotique).
- On peut maintenant changer l'objet parent des devices Rhasspy (Glisser/Déposer résumé domotique).
- On peut maintenant renommer l'objet Rhasspy-Intents.
- Attention à ne pas supprimer l'objet Rhasspy-Intents, ni déplacer les Intent qui sont dedans !

### 09/02/2021
- Affichage tableau Core v4.2

### 13/12/2020
- **Nécessite de réimporter l'assistant dans le plugin.**
- Nouvelle commande `repeatTTS`.

### 26/11/2020
- **Nécessite de réimporter l'assistant dans le plugin.**
- Nouvelle commande `SetVolume`.

### 30/05/2020
- Support du TTS simultané sur plusieurs devices (site1,site2).

### 19/04/2020
- **Attention**: Le plugin supporte maintenant Rhasspy v2.5 minimum !
- Ajouter un satellite : récupération automatique du siteId et vérifications.
- New : Deux nouvelles commandes sur les devices Rhasspy:
	- `ledOn` : Allume les LEDs
	- `ledOff` : Etaint les LEDs
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
- Bug fix : Commande `Ask`.

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
- **Nécessite de réimporter l'assistant dans le plugin.**
- New : commande *ask* voir [Documentation](index.md).

### 22/12/2019
- **Nécessite de réimporter l'assistant dans le plugin.**
- New : commande *dynamic Speak* sur les devices Rhasspy.

### 20/12/2019
- Première version (Beta).
