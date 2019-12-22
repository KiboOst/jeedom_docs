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
Il apparaîtra alors dans le menu *Plugins > Communication*.

Vous devez d'abord renseigner sur la page de configuration:

{% include lightbox.html src="jeerhasspy/images/config.jpg" data="jeelog" title="Configuration" imgstyle="width:550px;display: block;margin: 0 auto;" %}


- Adresse : L'adresse IP de votre Rhasspy (comprenant http:// ou https://).
- Port : Le Port de votre Rhasspy (par défaut 12101).
- Feedback : Une phrase que Jeedom dira si il ne trouve pas de scénario correspondant à l'Intent souhaité.
- Filtrer les Intents Jeedom : A l'importation de l'assistant, seuls les Itents donc le nom finit pas *jeedom* seront crées (**TurnOnJeedom**, **LightSetJeedom**, etc).


## Utilisation

Une fois configuré, il faut une première fois importer l'assistant Rhasspy.

A l'important il y a trois options possible:
- Conserver toutes les Intentions : Ne supprime aucun Intent, et crée ceux non présent dans Jeedom.
- Supprimer les Intentions qui ne sont plus dans l'assistant : Supprime seulement les Intents de Jeedom qui ne sont plus dans Rhasspy.
- Supprimer et recréer toutes les Intentions : Supprime tous les Intents de Jeedom, avant de recréer les Intents présents sur Rhasspy.


L'importation de l'assistant va créer :

- Un Device : C'est votre machine Rhasspy, permettant notamment de lancer une commande TTS.
- Vos Intentions : Chaque Intent de votre assistant.

> Tip
> Vous pouvez supprimer des intentions de trois façons:
> - En réimportant votre assistant, suivant l'option choisie (voir ci-dessus).
> - En utilisant le bouton **Supprimer les intentions**, qui supprimera tous vos Intents actuels.
> - Sur une intention, utilisez le bouton **Supprimer**.

En cliquant que un Device Rhasspy, vous pouvez lancer un test TTS sur ce device.

## Configuration Rhasspy

Pour que Rhasspy envoi les événements souhaités à Jeedom, vous devez ensuite lui indiquer l'url du plugin, indiquée dans la partie Assistant.
Vous pouvez le faire:
- Par l'interface de Rhasspy, onglet *Settings*, puis *Intent Handling* : Use a remote HTTP server to handle intents : cochez l'option et renseignez l'url.

{% include lightbox.html src="jeerhasspy/images/rhasspy_config.jpg" data="jeelog" title="Configuration Rhasspy" imgstyle="width:550px;display: block;margin: 0 auto;" %}

Ou manuellement:
- Par l'interface de Rhasspy, onglet *Advanced* ou,
- En éditant le fichier `.config\rhasspy\profiles\fr\profile.json`

```json
	"handle": {
        "system": "remote",
        "remote": {
            "url": "http://127.0.0.1:80/core/api/jeeApi.php?plugin=jeerhasspy&apikey=---apikey---&plugin=jeerhasspy&type=jeerhasspy"
        }
    }

```

## Callback Scénario

Pour chaque Intention (Intent), vous devez :

- Renseigner un scénario qui sera exécuté à la détection de cet Intent par Rhasspy.
- Renseigner l'action à réaliser sur le scénario (start, ...).
- Cocher les informations comprises dans l'Intent, qui seront passées au scénario sous forme de tags.
- Renseigner éventuellement d'autres tags spécifiques.

{% include lightbox.html src="jeerhasspy/images/intent_config.jpg" data="jeelog" title="Configuration d'une Intention" imgstyle="width:550px;display: block;margin: 0 auto;" %}


### Exemple de scénario

Voici un exemple de scénario.

{% include lightbox.html src="jeerhasspy/images/scenario_01.jpg" data="jeelog" title="Exemple de scénario" imgstyle="width:550px;display: block;margin: 0 auto;" %}

Le premier bloc SI sera commun à la plupart de ce type de scénario : On veut savoir d'où vient la demande pour pouvoir la traiter correctement. *house_room* est un slot de rhasspy, par exemple, si on lui demande :

> Allume la lumière de la cuisine

Voici ce que rhasspy va envoyer au plugin :

```json
{
	"intent": {
		"name": "lightsTurnOnJeedom",
		"confidence": 1
	},
	"entities": [{
			"entity": "house_room",
			"value": "cuisine",
		}
	],
	"text": "allume les lumi\u00e8re de le cuisine",
	"wakeId": "snowboy\/hey_brigitte.pmdl",
	"siteId": "salon"
}
```
Le plugin sait donc de qu'elle intention il s'agit, et lance alors le scénario correspondant avec les tags suivant :

```
Start : Lancement provoque. Tags : {"#intent#":"lightsTurnOnJeedom","#confidence#":"1","#wakeword#":"snowboy\/hey_brigitte.pmdl","#query#":"allume les lumi\u00e8re de le cuisine","#siteId#":"salon","#house_room#":"cuisine"}
```

Donc si on pas de tag(house_room), car on peux simplement lui demander d'allumer la lumière sans préciser où, on a deux solutions :
- Soit le siteId n'est pas renseigné dans Rhasspy, donc on donne le nom de notre device de base (master) Rhasspy, ici dans le *salon*.
- Soit le siteId est renseigné, et on l'utilise.
Et si on a le tag(house_room), on l'utilise.
On a donc maintenant tag(rhasspy_room) qui correspond à la pièce souhaitée.

Le deuxième bloc SI n'est pas obligatoire. Vous pouvez lancer le même scénario pour plusieurs intents, et il sert donc à filtrer l'intent souhaité.
Par exemple si on veux allumer ou éteindre une lumière.

Finalement, on vérifie de quelle lumière il s'agit : SI tag(rhasspy_room) matches "/cuisine|maison/"

En matchant cuisine ou maison, on pourra aussi demander :

> Allume les lumière de la maison

On peut aussi différencier *en bas*, *en haut* pour pouvoir demander :

> Allume les lumière en bas

Avec SI tag(rhasspy_room) matches "/cuisine|maison|en bas/"

Et ainsi de suite ...
