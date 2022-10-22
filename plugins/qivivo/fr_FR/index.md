---
title: Jeedom | Plugin Qivivo
description: Intégration du Thermostat Qivivo.
---

<img align="right" src="../images/qivivo_icon.png" width="100">

# Qivivo - Plugin pour Jeedom

*[Lien market](https://www.jeedom.com/market/index.php?v=d&p=market&type=plugin&plugin_id=3551)*

Intégration du Thermostat [Qivivo / Comap.](https://www.comapsmarthome.com/fr/)

[Configuration](#configuration)
[Utilisation](#utilisation)
[Actions](#actions)
[Programmes](#programmes)
[Historique](#historique)
[Remarques](#remarques)
[Changelog](changelog.md)


## Configuration

Après installation, activez le plugin. Il apparaîtra alors dans le menu *Plugins > Confort*.
- Ouvrez la page du plugin, puis cliquez sur *Configuration*.
- Renseignez vos Login, password Qivivo / Comap.
- Cliquez sur *Synchroniser mes équipements*.

{% include lightbox.html src="qivivo/images/config2.jpg" data="qivivo" title="Configuration" imgstyle="width:550px;display: block;margin: 0 auto;" %}

Ceci aura pour effet d'installer votre thermostat, la passerelle (qui n'a ici aucune fonction), et vos modules fil-pilote, nommés par zone.
Il ne vous reste qu'à rafraîchir la page du plugin (F5) !

{% include lightbox.html src="qivivo/images/plugin2.jpg" data="qivivo" title="Plugin" imgstyle="width:550px;display: block;margin: 0 auto;" %}

## Utilisation

Renseignez pour chaque module, son nom et son Objet parent si nécessaire. Ils apparaîtront ainsi au bon endroit sur votre dashboard.

### Dashboard
Voici un exemple sur le dashboard:

{% include lightbox.html src="qivivo/images/dashboard2.jpg" data="qivivo" title="Dashboard" imgstyle="width:550px;display: block;margin: 0 auto;" %}

Vous pouvez ainsi visualiser:

- La température de consigne du thermostat.
- La température mesurée par le thermostat.
- Le taux d'humidité mesuré par le thermostat.
- La dernière présence relevée par le thermostat.
- Le programme en cours.
- L'ordre en cours par zone.
- La date de dernière communication du module avec les serveurs Qivivo / Comap.

> Quand vous changez la consigne du thermostat, l'affichage change sur le dashboard. Toutefois, la commande info de consigne n'est volontairement pas mise à jour. En effet, les programmes temporaires ne sont pas pris en compte immédiatement par Qivivo, cela peu prendre entre 1 et 5mins. De cette façon, l'historique de la consigne enregistrera les vraies valeurs de consigne du thermostat et sera mise à jour lors de la prise en compte par celui-ci.

Vous pouvez également:

- Changer la température de consigne (pendant 2h) du thermostat.
- Annuler une programmation temporaire du thermostat ou d'une zone.
- Changer l'ordre d'une zone.
- Changer de programme.

Vous pouvez bien sûr intégrer ces informations et actions dans des scénarios !

## Actions

Le thermostat dispose de plusieurs actions que vous pouvez intégrer normalement dans Jeedom, dans les scénarios par exemple.

{% include lightbox.html src="qivivo/images/thermostat_actions2.jpg" data="qivivo" title="Actions du thermostat" imgstyle="width:550px;display: block;margin: 0 auto;" %}

> La commande SetTempérature permet de lancer un programme temporaire, de la même manière que par le site Qivivo ou physiquement sur le thermostat. Le thermostat dispose dans Jeedom d'une info *DuréeOrdre* qui sera la durée du programme temporaire. Celle-ci se remet à 120mins (comme pour le thermostat physique) toutes les 15mins (ou 5mins si vous activez le cron5). Toutefois, si vous souhaitez spécifier une autre durée, lancer une commande *SetDuréeOrdre* avant la commande *SetTempérature*.
Vous pouvez également annuler un programme temporaire avec la commande *Annule_Ordre_Temp*.

Les modules de zone disposent également de leurs actions *SetMode* pour changer d'ordre, et *Annule_Ordre_Temp* pour annuler un ordre temporaire.
> Le module de la Zone Thermostat ne possède pas la commande *SetMode* puisqu'il est contrôlé par la consigne du thermostat.

## Équipements

### Thermostat

{% include lightbox.html src="qivivo/images/thermostat2.jpg" data="qivivo" title="Thermostat" imgstyle="width:550px;display: block;margin: 0 auto;" %}

Certaines informations sont visibles ici, notamment les réglages de température. Ce sont les mêmes que dans les réglages sur le site de Qivivo / Comap.

### Module fil-pilote

{% include lightbox.html src="qivivo/images/modulechauffage2.jpg" data="qivivo" title="Module chauffage" imgstyle="width:550px;display: block;margin: 0 auto;" %}

Le module fil-pilote possède une info *Ordre* affichant l'ordre courant sous forme lisible (*string*). Cette info n'est pas historisée, mais une autre info *OrdreNum* représente l'ordre sous forme de numéro de 1 à 6, et est historisée :

- Arrêt : 0
- Hors-Gel : 1
- Eco : 2
- Confort -2 : 3
- Confort -1 : 4
- Confort : 5

## Remarques

### Gestion des erreurs
Il peux arriver que les serveurs de Qivivo / Comap ne répondent pas:

Lors d'un rafraîchissement des informations, si l'appel à l'API Qivivo échoue trois fois de suite, un log d'erreur sera créé.

Lorsque vous passez une commande (une action), par le dashboard ou un scénario, un échec peut-être très embêtant. Si vous quittez la maison pendant une semaine et qu'un scénario passe votre Qivivo en programme absence, le risque est que le chauffage reste allumé toute la semaine.

Dans ce cas, vous avez deux possibilités, dans la configuration du plugin:

- ***Répéter l'action sur échec*** : le plugin répétera la même action 90sec plus tard en utilisant le système de cron de Jeedom. Lors de ce 2èm appel, si la commande échoue à nouveau (ou si vous décochez l'option), un log d'erreur est créé (et un message si l'option est cochée dans la configuration de Jeedom).
-  ***Actions sur erreur***: Vous pouvez définir ici des actions à exécuter si une commande ne passe pas. Par exemple, vous envoyer un email, une notification sur l'application mobile, etc. Vous pouvez spécifier dans un champ *Message* le raccourci #message# pour obtenir une description de la commande ayant échouée.

### Auto actualisation

Dans la page de configuration, onglet *Fonctionnalités*, l'option cron15 est activée par défaut. Ceci permet d'actualiser toutes les infos des modules et du thermostat toutes les 15 mins. Au regard de la réactivité du chauffage, c'est suffisant.
Toutefois, l'actualisation des données sur les serveurs Qivivo se faisant toutes les 5 minutes, vous pouvez si vous le souhaitez passer le cron à 5 mins.

### Eté / Hiver

A l'arrêt du chauffage, vous pouvez basculer le plugin en cron15 (voir même désactiver les cron) par un scénario, avec un bloc code:

```
config::save('functionality::cron5::enable', 0, 'qivivo');
config::save('functionality::cron15::enable', 1, 'qivivo');
```

### Debug

Si vous rencontrez des problèmes, l'équipement *passerelle* possède une commande action *debug*. Vous pouvez cliquer sur *Tester*, ce qui générera un log qivivo_debug. Vous pouvez l'envoyer à kiboost->free.fr (ou mp sur le forum Jeedom) avec:
- La description du problème.
- Une description de votre installation Qivivo avec si possible des screens du site Qivivo.
- Si vous êtes familier ou non du plugin outildev, pour pouvoir vous envoyer des correctifs de test plus facilement.
- Si vous avez accès aux plugins beta.


## Changelog

[Voir la page dédiée](changelog.md).


