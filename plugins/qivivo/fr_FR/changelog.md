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

- [Commits Github Beta](https://github.com/KiboOst/jeedom-qivivo/commits/beta)
- [Commits Github Stable V4](https://github.com/KiboOst/jeedom-qivivo/commits/stableV4)

### 24/10/2021
- Beta: Support de courbe sur les tuiles Thermostat et Module de zone (Core v4.2).

### 24/05/2021
- Beta: Depuis la tuile du thermostat, les boutons -1 et +1 affichent maintenant un popup pour régler la température souhaitée et la durée.

### 22/05/2021
- Beta: Changement de système d'authentification par Comap (Aws Cognito).

### 09/02/2021
- Affichage tableau Core v4.2 (beta)

### 23/09/2020
- Version beta:
	- Support des configurations Monozone

### 15/09/2020
- Version Stable suite à la refonte complète des site, app, et API Qivivo / Comap.
Attention :
	- Vous devez avoir déjà migré sur la nouvelle interface [Comap](https://app.comapsmarthome.com/real-time).
	- Suppression des modules existants ! Vous devrez refaire une synchronisation puis adapter vos design, scenarios, résumés, etc. (aidez vous de Analyse / Équipements / Commandes orphelines).
	- Suppression de toute la partie programmation. Les programmes sont repris depuis l'interface Qivivo/Comap, et sont maintenant synchronisés avec le plugin. Pensez à faire vos programmes sur l'interface Qivivo/Comap avant la mise à jour du plugin si possible.
	- Le changement de programme se fait maintenant par le thermostat.

### 08/09/2020 (beta)
- [Première beta](https://community.jeedom.com/t/qivivo-comap-update-interface-comap-09-2020-v2/36490) pour l'adaptation aux nouvelles interfaces Qivivo/Comap.
	- La doc n'est pas à jour avec la beta, elle le sera une fois le plugin en stable.
	- Suppression de l'ancienne API officielle qui ne dialogue plus avec les modules.
	- Refonte complète de l'[API custom](https://github.com/KiboOst/php-qivivoAPI), basée de la future API officielle utilisée par le nouveau site et apps Qivivo/Comap.
	- Suppression lors de l'update de tout les modules ! Il faut donc refaire une synchro, les renommer etc correctement, et vérifier / updater les commandes orphelines.
	- Suppression de toute la partie programmation. Les programmes sont repris depuis l'interface Qivivo/Comap, et sont maintenant synchronisés avec le plugin.
	- Changement de programme par le thermostat (plus sur les zones).
	- Testée avec 1 résidence, 1 thermostat, plusieurs modules de zones.

### 06/03/2020
- Suppression de la vérification du certificat. *Certificat expiré pour l'API officielle Qivivo depuis 4j et aucun mouvement de leur part...*.

### 03/03/2020
- Traduction du plugin en anglais (Jeedom V4).

### 15/02/2020
- Amélioration des logs de debug.
- Plus d'infos sur la commande debug de la passerelle.
- Support des programmes sur les installations non multi-zone.

### 06/09/2019
- Création de la version Stable Jeedom V4
- Passage de la beta sur Jeedom V4
>   *Pour Jeedom V3, restez dorénavant en version Stable. Le market sélectionne automatiquement la stable V3 ou V4 en fonction de votre version de Jeedom.*

### 15/03/2019
- Configuration du type de batteries (3x1.5V AAA).

### 07/03/2019
- Remontée du pourcentage de batterie (thermostat), et info Batterie dans analyse/équipements.
*Le niveau de batterie sera renseigné au prochain refresh du thermostat, cron ou manuel.*

### 25/02/2019
- Ajout d'un bouton *Appliquer* dans les programmes.

### 05/02/2019
- Ajout des types génériques Consigne, Température mesurée, Chauffe.

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
