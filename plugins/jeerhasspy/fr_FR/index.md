---
title: Jeedom | Plugin JeeRhasspy
description: Plugin pour le support de l'assistant vocal Rhasspy dans Jeedom
---

<img align="right" src="../images/jeerhasspy_icon.png" width="100">

# JeeRhasspy - Plugin pour Jeedom

Plugin pour le support de l'assistant vocal [Rhasspy](https://rhasspy.readthedocs.io/en/latest/) dans Jeedom.
Vous devez au préalable avoir un système Rhasspy fonctionnel !

[Changelog](changelog.md)<br />

## Configuration du plugin JeeRhasspy

Après installation du plugin, il vous suffit de l’activer.
Il apparaîtra alors dans le menu *Plugins > Communication*.

Vous devez alors renseigner, sur la page de configuration du plugin :

{% include lightbox.html src="jeerhasspy/images/config.jpg" data="jeerhasspy" title="Configuration" imgstyle="width:550px;display: block;margin: 0 auto;" %}

- Adresse : L'adresse IP de votre Rhasspy (comprenant http:// ou https://).
- Port : Le Port de votre Rhasspy (par défaut 12101).
- Feedback : Une phrase que Rhasspy dira si il ne trouve pas de scénario correspondant à l'Intent souhaité.
- Filtrer les Intents Jeedom : A l'importation de l'assistant, seuls les Itents donc le nom finit pas *jeedom* seront crées (**TurnOnJeedom**, **LightSetJeedom**, etc).
- Variables rhasspyWakeWord / rhasspyWakeSiteId : Quand le wakeword est détecté, le plugin renseigne ces deux variables avec le wakewordId et siteId. Vous pouvez alors déclencher un scénario sur `#variable(rhasspyWakeWord)#` pour par exemple couper la musique le temps de votre demande.


## Utilisation

Une fois le plugin configuré, il faut une première fois importer l'assistant Rhasspy.

A l'importation, il y a trois options possible:
*Lors de la première importantation, ces options n'ont pas d'incidence*.
- Conserver toutes les Intentions : Ne supprime aucun Intent, et crée ceux non présent dans Jeedom.
- Supprimer les Intentions qui ne sont plus dans l'assistant : Supprime seulement les Intents de Jeedom qui ne sont plus dans Rhasspy.
- Supprimer et recréer toutes les Intentions : Supprime tous les Intents de Jeedom, avant de recréer les Intents présents sur Rhasspy.

L'importation de l'assistant va créer :

- Un Device : C'est votre machine Rhasspy, permettant notamment de lancer une commande **TTS** ou **Ask**.
- Vos Intentions : Chaque Intent présent sur votre assistant Rhasspy.

> Tip
> Vous pouvez supprimer des intentions de trois façons:
> - En réimportant votre assistant, suivant l'option choisie (voir ci-dessus).
> - En utilisant le bouton **Supprimer les intentions**, qui supprimera tous vos Intents actuels du plugin.
> - Sur une intention, utilisez le bouton **Supprimer**.

En cliquant sur un Device Rhasspy, vous pouvez effectuer un test TTS sur ce device.

## Configuration Rhasspy

Pour que Rhasspy envoie les événements souhaités à Jeedom, vous devez ensuite lui indiquer l'url du plugin, indiquée dans la partie Assistant.

{% include lightbox.html src="jeerhasspy/images/assistant_configure.jpg" data="jeerhasspy" title="Configuration de Rhasspy" imgstyle="width:550px;display: block;margin: 0 auto;" %}


### Intent recognized

Rhasspy envoie directement l'Intent reconnu sur une url (ici, le plugin).

Vous pouvez le faire:
- **Automatiquement** : *Plugins > Communication > jeeRhasspy* Dans le panel **Assistant** cliquez sur le bouton **Configurer** à droite de l'url à utiliser.
- Par l'interface de Rhasspy, onglet *Settings*, puis *Intent Handling* : Use a remote HTTP server to handle intents : cochez l'option et renseignez l'url.

{% include lightbox.html src="jeerhasspy/images/rhasspy_config.jpg" data="jeerhasspy" title="Configuration Rhasspy" imgstyle="width:550px;display: block;margin: 0 auto;" %}

- En éditant le fichier `.config\rhasspy\profiles\fr\profile.json`

```json
	"handle": {
        "system": "remote",
        "remote": {
            "url": "http://x.x.x.x:80/core/api/jeeApi.php?plugin=jeerhasspy&apikey=---apikey---&plugin=jeerhasspy&type=jeerhasspy"
        }
    },

```

> Tip
> Actuellement pour nommer votre device Rhasspy, vous devez :
> - Sur l'interface de Rhasspy, aller sur l'onglet **Settings**
> - Cliquer sur MQTT et cocher *Enable MQTT*
> - Renseigner un nom dans le champ **Site ID**
> - Décocher *Enable MQTT* si vous ne l'utilisez pas, puis sauver les settings.

### Wakeword detected

Si vous utilisez l'option permettant de renseigner les variables rhasspyWakeWord / rhasspyWakeSiteId sur détection du wakeword, vous devez éditer votre profile Rhasspy. Cette option n'est pas disponible par l'interface de Rhasspy.

- **Automatiquement** : *Plugins > Communication > jeeRhasspy* Dans le panel **Assistant** cliquez sur le bouton **Configurer** à droite de l'option *Wake event*.
- En éditant le fichier `.config\rhasspy\profiles\fr\profile.json`

```json
	"webhooks": {
		"awake": ["http://x.x.x.x:80/core/api/jeeApi.php?plugin=jeerhasspy&apikey=---apikey---&plugin=jeerhasspy&type=jeerhasspy"]
	},

```

## Callback Scénario

Pour chaque Intention (Intent), vous devez :

- Renseigner un scénario qui sera exécuté à la détection de cet Intent par Rhasspy.
- Renseigner l'action à réaliser sur le scénario (start, ...).
- Cocher les informations comprises dans l'Intent, qui seront passées au scénario sous forme de tags.
- Renseigner éventuellement d'autres tags spécifiques.

{% include lightbox.html src="jeerhasspy/images/intent_config.jpg" data="jeerhasspy" title="Configuration d'une Intention" imgstyle="width:550px;display: block;margin: 0 auto;" %}


### Exemple de scénario

Voici un exemple de scénario.

{% include lightbox.html src="jeerhasspy/images/scenario_01.jpg" data="jeerhasspy" title="Exemple de scénario" imgstyle="width:550px;display: block;margin: 0 auto;" %}

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
	"text": "allume les lumière de la cuisine",
	"wakeId": "snowboy\/hey_brigitte.pmdl",
	"siteId": "salon"
}
```
Le plugin sait donc de qu'elle intention il s'agit, et lance alors le scénario correspondant avec les tags suivant :

```
Start : Lancement provoque. Tags : {"#intent#":"lightsTurnOnJeedom","#confidence#":"1","#wakeword#":"snowboy\/hey_brigitte.pmdl","#query#":"allume les lumière de la cuisine","#siteId#":"salon","#house_room#":"cuisine"}
```

Donc si on pas de tag(house_room), car on peut simplement lui demander d'allumer la lumière sans préciser où, on a deux solutions :
- Soit le siteId n'est pas renseigné dans Rhasspy, donc on donne le nom de notre device de base (master) Rhasspy, ici dans le *salon*.
- Soit le siteId est renseigné, et on l'utilise.
Et si on a le tag(house_room), on l'utilise.
On a donc maintenant tag(rhasspy_room) qui correspond à la pièce souhaitée.

Le deuxième bloc SI n'est pas obligatoire. Vous pouvez lancer le même scénario pour plusieurs intents, et il sert donc à filtrer l'intent souhaité.
Par exemple si on veux allumer ou éteindre une lumière.

Finalement, on vérifie de quelle lumière il s'agit : `SI tag(rhasspy_room) matches "/cuisine\|maison/"`

En matchant cuisine ou maison, on pourra aussi demander :

> Allume les lumières de la maison

On peut aussi différencier *en bas*, *en haut* pour pouvoir demander :

> Allume les lumières en bas

Avec `SI tag(rhasspy_room) matches "/cuisine\|maison\|en bas/"`

Et ainsi de suite ...

## Commandes

Sur chaque device Rhasspy, il y a trois commandes:

- **Speak** : Permet d'énoncer un texte.
- **dynamic Speak** : Permet d'énoncer un texte construit dynamiquement.
- **Ask** : Permet d'utiliser la fonction **Ask** de Jeedom.

### Commande *dynamic Speak*

Cette commande permet de construire un texte dynamique en fonction d'informations d'équipements dans Jeedom.

{% include lightbox.html src="jeerhasspy/images/dynspeak.jpg" data="jeerhasspy" title="dynamic Speak" imgstyle="width:550px;display: block;margin: 0 auto;" %}

Par exemple, vous voulez demander à Rhasspy si le volet est ouvert. L'information dans Jeedom étant le pourcentage d'ouverture, ou 0 / 1, la réponse ne sera pas très *waf*.

Vous pourriez faire trois blocs SI :
```
SI #[Salon][Volet Terrasse][Etat]# == 0 THEN speak Le volet est fermé
SINON
	SI #[Salon][Volet Terrasse][Etat]# == 99 THEN speak Le volet est ouvert
	SINON speak Le volet est ouvert à #[Salon][Volet Terrasse][Etat]# pour cent
```
Certes, çà fonctionnera, mais çà complexifie énormément les scénarios.

La commande *dynamic Speak* va vous permettre de faire simplement :

> Le volet de la salle est {#[Salon][Volet Terrasse][Etat]#\|0:fermé\|<99:ouvert à #[Salon][Volet Terrasse][Etat]# pourcent\|99:ouvert}

Donc, on passe d'abord l'information dans un **{}** puis, séparés par des **\|**, on passe les conditions si:alors avec le si comme valeur et le alors comme texte.
Dès qu'une condition est trouvée, l'évaluation s'arrête. Si le volet est à 0 c'est bien 'fermé' qui sera énoncé, car <99 ne sera pas évalué.

Un autre exemple pour demander si une lumière est allumée ou éteinte :

> La lumière est actuellement {#[Cuisine][Lumière][Etat]#\|0:éteinte\|1:allumée}

### Commande *Ask*

Vous pouvez utiliser la commande interne de Jeedom **Ask** pour que votre Rhasspy vous pose une question, et attende votre réponse. Votre scénario pourra ensuite agir en fonction de votre réponse.

Pour cela vous devez indiquer :
- Dans le champ **Réponse** : Le nom du *slot* contenant la réponse, tel que définit dans rhasspy.
- Dans le champ **Commandes** : La commande **Ask** du device rhasspy.

Voici un exemple :

{% include lightbox.html src="jeerhasspy/images/scenario_ask.jpg" data="jeerhasspy" title="Commande Ask" imgstyle="width:550px;display: block;margin: 0 auto;" %}




