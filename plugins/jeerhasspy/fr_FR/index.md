---
title: Jeedom | Plugin JeeRhasspy
description: Plugin pour le support de l'assistant vocal Rhasspy dans Jeedom
---

<img align="right" src="../images/jeerhasspy_icon.png" width="100">

# JeeRhasspy - Plugin pour Jeedom

Plugin pour le support de l'assistant vocal Rhasspy dans Jeedom.

[Changelog](changelog.md)<br />

## Configuration du plugin JeeRhasspy

Après installation du plugin, il vous suffit de l’activer.
Il apparaîtra alors dans le menu *Plugins > Communication*

Vous devez d'abord renseigner sur la page de configuration:
- Adresse : L'adresse IP de votre Rhasspy (comprenant http:// ou https://).
- Port : Le Port de votre Rhasspy (par défaut 12101).
- Feedback : Une phrase que Jeedom dira si il ne trouve pas de scénario correspondant à l'Intent souhaité.
- Filtrer les Intents Jeedom : A l'importation de l'assistant, seuls les Itents donc le nom finit pas *jeedom* seront crées (**TurnOnJeedom**, **LightSetJeedom**, etc).


## Utilisation

Une fois configuré, il faut une première fois importer l'assistant Rhasspy.

A l'important il y a trois options possible:
- Conserver tous les Intents : Ne supprimme aucun Intent, et crée ceux non présent dans Jeedom.
- Supprimer les Intents qui ne sont plus dans l'assistant : Supprime seulement les Intents de Jeedom qui ne sont plus dans Rhasspy.
- Supprimer et recréer tous les Intents : Supprime tous les Intents de Jeedom, avant de recréer les Intents présents sur Rhasspy.


L'important de l'assistant va créer :

- Un Device : C'est votre machine Rhasspy, permettant notamment de lancer une commande TTS.
- Vos Intents : Chaque Intent de votre assistant.
- Supprimer Intents : Supprime tous les Intents du plugin (Aucune action sur les Intents de Rhasspy !).

En cliquant que un Device Rhasspy, vous pouvez lancer un test TTS.

## Configuration Rhasspy

Pour que Rhasspy envoit les évènements souhaités à Jeedom, vous devez ensuite lui indiquer l'url du plugin, indiquée dans la partie Assistant.
Vous pouvez le faire:
- Par l'interface de Rhasspy, onglet *Settings*, puis *Intent Handling* : Use a remote HTTP server to handle intents : cochez l'option et renseignez l'url.
- Par l'interface de Rhasspy, onglet *Advanced* ou,
- En éditant le fichier `.config\rhasspy\profiles\fr\profile.json`

```json
	"handle": {
        "system": "remote",
        "remote": {
            "url": "http://127.0.0.1:80/core/api/jeeApi.php?plugin=jeerhasspy&apikey=---apiky---&plugin=jeerhasspy&type=jeerhasspy"
        }
    }

```


### Callback Scénario

Pour chaque Intent, vous devez :

- Renseigner un scénario qui sera éxécuté à la détection de cet Intent par Rhasspy.
- Renseigner l'action à réaliser sur le scénario (start, ...).
- Cocher les informations comprises dans l'Intent, qui seront passées au scénario sous forme de tags.
- Renseigner éventuellement d'autres tags spécifiques.


