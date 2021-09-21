---
title: Jeedom v4 | Petits codes entre amis
description: Scénarios - Petits codes entre amis
---

<img align="right" src="../../images/logo-jeedom.png" width="100">

# Jeedom v4 | Scénarios : Petits codes entre amis

• [Astuces pour la personnalisation de l'interface](https://kiboost.github.io/jeedom_docs/jeedomV4Tips/Interface/fr_FR/)<br>
• [Scénarios : Programmation du jour](https://kiboost.github.io/jeedom_docs/jeedomV4Tips/Tutos/ProgDuJour/fr_FR/)<br>


[Introduction](#introduction)<br />
[Quelques exemples](#quelques-exemples)<br />
[Ajout de fonction php](#ajout-de-fonction-php)<br />
[pyJeedom](#pyjeedom)<br />

## Introduction

Vous le savez, un scénario est constitué de différents blocs (SI, A, DANS, etc), utilisés en fonction de ce que l'on désire faire.
L'un d'entre eux est le bloc CODE, peu engageant à première vue, mais pourtant bien pratique.

{% include lightbox.html src="../jeedomV4Tips/CodesScenario/images/code_example.jpg" data="codes" title="Bloc CODE" imgstyle="width:600px;display: block;margin: 0 auto;" %}

Ce type de bloc permet d'écrire du code php que le scénario va interpréter. par exemple :

```php
$trigger = $scenario->getTrigger();
$cmdID = str_replace('#', '', $trigger[0]);
$eq = cmd::byId($cmdID)->getEqLogic();
$eq->setIsEnable(0)->save()
```

C'est bien jolie, mais qu'est-ce qu'on peux faire avec ? Tout simplement accéder à toutes les fonctions php, mais aussi à la plupart des fonctions du core de Jeedom lui même, et donc aux équipements et à leurs commandes notamment.

Voici un lien vers la [doc de l'API Jeedom](https://jeedom.github.io/documentation/phpdoc/), qui permet de retrouver facilement les fonctions souhaitées. Vous pouvez également regarder directement dans le code source du core.


Il faut considérer un bloc Code comme un script php que vous exécuter sur un serveur. Vous pouvez ainsi facilement récupérer des données de votre Jeedom, mais aussi des données sur Internet, dans un fichier sur un site ou autre. Même si pour des cas complexes, je préfère créer un Script avec le plugin Script.

Pour communiquer entre ce bloc CODE et le reste de votre scénarios, vous avez différentes options:

- Renseigner une variable de scénario, que vous pourrez ensuite tester / utiliser plus tard dans le scénario
```php
$scenario->setData('maVariable', '1');
```
- Renseigner un tag du scénario
```php
$tags = $scenario->getTags();
$tags['#monTag#'] = 'Hello';
$scenario->setTags($tags);
```
- Mettre à jour la valeur d'une info d'un équipement, virtuel ou autre.
```php
cmd::byString('#[Maison][Planning][Mode]#')->event('Vacances');
```

#### Remarques

Concernant php, je ne pourrai que conseiller de s'y familiariser un minimum. Pour çà il existe plein de sites, blogs et la doc sur Internet. En dehors des fonctions propres à Jeedom, l'étendu de php est extrêmement large, et vous familiariser avec les opérations les plus courante (manipulation de chaînes, boucles, conditions, dates etc) est un plus si vous vous engagez sur ce chemin ;-)

Quelques remarques
```php
$message = 'message';
message::add("Titre", 'Message: '.$message);
```
Deux lignes qui illustrent plusieurs choses.
- $message est une variable php que vous définissez ($xx)
- message tout court (message::add) est une classe php, ici une classe définit par Jeedom (html/core/class/message.class.php)
- "string" ou 'string' sont des chaînes de caractères. Toutefois, notez la différence entre les double-quote et simple-quote. Dans une "string", php va rechercher des variables pour les traduire, ce sera donc plus lent qu'une 'string'. Donc utilisez toujours des simple-quote dans ce cas, sauf si vous savez pourquoi.
ex:
```php
$var = 'bibi';
$msg1 = 'message de $var';
$msg2 = "message de $var";
```
$msg1 sera égal à : message de $var<br/>
$msg2 sera égal à : message de bibi

Et enfin, la concaténation de chaîne étant différente d'un langage à l'autre, vous pouvez aussi faire:
```php
$var = 'bibi';
$msg = 'message de '.$var;
```

Un autre exemple, que j'ai publié il y a 2 ans déjà, avec des virtuels, un script php, et un gros bloc CODE en scénario pour récupérer les levé/couché du soleil, date, azimut, élévation, ensoleillement de façades etc: [php-sunPos - Jeedom](https://github.com/KiboOst/php-sunPos/tree/master/Jeedom). Vous y trouverez notamment des manipulations de dates qui pourront vous intéresser.


*Si vous n'avez pas encore lâché, vous pouvez continuer avec quelques exemples !*

## Quelques exemples

<br/>• Créer un message dans le centre de message
```php
$title = 'php testing';
$message = 'small message';
message::add($title, $message);
```

<br/>• Récupérer la valeur d'une variable
```php
$myVar = $scenario->getData('maVariable');
```

<br/>• Mettre à jour une commande info
```php
cmd::byString('#[Maison][infos][test]#')->event(100);
```

<br/>• Récupérer la valeur d'une commande info
```php
$value = cmd::byString('#[Maison][infos][test]#')->execCmd();
```

<br/>• Exécuter une commande action (même chose que pour une info)
```php
cmd::byString('#[Maison][actions][actionOn]#')->execCmd();
```

<br/>• Exécuter une commande action de type slider
```php
$options = array('slider'=>100);
cmd::byString('#[Salon][Lumière Salon][Intensité]#')->execCmd($options, $cache=0);
```

<br/>• Exécuter une commande action de type message
```php
$options = array('title'=>'pièce', 'message'=> 'Hello, how is it today ?');
cmd::byString('#[Maison][TTS][Speak]#')->execCmd($options, $cache=0);
```

<br/>• Récupérer la date de dernière mise à jour d'une info
```php
$cmd = cmd::byString('#[Maison][infos][test]#');
$collectDate = $cmd->getCollectDate();
```

<br/>• Écrire dans un log<br/>
*Le niveau de log doit correspondre*
```php
log::add('maison', 'error', $value.'  : '.$collectDate);
```

<br/>• Écrire dans le log du scénario
```php
$scenario->setLog('__'.$collectDate.' -> '.$value);
```

<br/>• Changer le cron d'un plugin. Je m'en sert pour passer le plugin Qivivo en cron15 hors période de chauffe
```php
config::save('functionality::cron5::enable', 0, 'qivivo');
config::save('functionality::cron15::enable', 1, 'qivivo');
```

<br/>• Faire un reset du swap de votre Jeedom
```php
$cmd = 'sudo swapoff -a && sudo swapon -a';
$result = exec($cmd);
$scenario->setLog($result);
```

<br/>• Masquer un objet
```php
object::byName('Cuisine')->setIsVisible(0)->save();
```

<br/>• Récupérer le dernier message d'update<br/>
*Avec un scénario en action sur message, vous pouvez vous envoyer un mail ou une notification quand il y a une update*

{% include lightbox.html src="../jeedomV4Tips/CodesScenario/images/msgFilter.jpg" data="codes" title="Notification d'update" imgstyle="width:800px;display: block;margin: 0 auto;" %}

```php
$msgs = message::byPlugin('update');
$msg = $msgs[0];
$text = $msg->getDate() . ': ' . $msg->getPlugin() . ': ' . $msg->getMessage();
scenario::setData('MsgFilter', $text);
```

<br/>• Récupérer un tag
```php
$tags = $scenario->getTags();
$montag = $tags['#monTag#'];
```

<br/>• Attribuer un tag au scénario<br/>
*Les tags n'existent que lors de l’exécution du scénario, vous n'avez donc pas besoin de le supprimer ensuite, comme pour une variable*
```php
$tags = $scenario->getTags();
$tags['#monTag#'] = 'Hello';
$scenario->setTags($tags);
```
*C'est, je pense, la meilleure solution pour passer le résultat d'un bloc CODE au scénario et faire ensuite des tests en fonction*

{% include lightbox.html src="../jeedomV4Tips/CodesScenario/images/tags.jpg" data="codes" title="Tags" imgstyle="width:800px;display: block;margin: 0 auto;" %}


<br/>• Renseigner des variables lever et coucher du soleil<br/>
*Rendez-vous sur Google Map, placez un repère sur votre habitation, notez les coordonnées GPS qui s'affichent en bas*
```php
$lat = 45.808;
$long = 4.872;
$sun_info = date_sun_info(time(), $lat, $long);
$sunrise = date("Hi", $sun_info["sunrise"]);
$sunset = date("Hi", $sun_info["sunset"]);
$scenario->setData('sunrise', $sunrise);
$scenario->setData('sunset', $sunset);
```
cf [Scénarios : Programmation du jour](https://kiboost.github.io/jeedom_docs/jeedomV4Tips/Tutos/ProgDuJour/fr_FR/)


## Ajout de fonction php

Jeedom permet également d'ajouter des fonctions utilisables directement dans les scénarios.
[Doc officielle](https://jeedom.github.io/core/fr_FR/scenario#tocAnchor-1-15)

Pour cela il faut éditer le fichier `/data/user.function.class.php`.
Vous pouvez utiliser l'éditeur de Jeedom (voir doc) ou le plugin [JeeXplorer](https://www.jeedom.com/market/index.php?v=d&p=market&type=plugin&plugin_id=3690)

Un petit exemple qui va nous permettre de tester et de récupérer un paramètre de configuration de Jeedom ou d'un plugin dans un scénario.

Le fichier `/data/user.function.class.php`:
```php
<?php
require_once dirname(__FILE__) . '/../../core/php/core.inc.php';

class userFunction {
	public static function getConfigByKey($_key='', $_type='core', $_default = '', $_forceFresh = false) {
		$_key = self::stripQuotes($_key);
		$_type = self::stripQuotes($_type);
		$_default = self::stripQuotes($_default);
		return config::byKey($_key, $_type, $_default, $_forceFresh);;
	}

	/* INTERNAL FUNCTIONS */
	static function stripQuotes($text) {
		return preg_replace('/(^[\"\']|[\"\']$)/', '', $text);
	}
}
```
> La fonction stripQuotes() permet d'appeller getConfigByKey(name, core) ou getConfigByKey("name", "core"), evitant les erreurs ;-)

Ce qui nous permet d’appeler la fonction getConfigByKey() dans un scénario:

{% include lightbox.html src="../jeedomV4Tips/CodesScenario/images/user_getConfigByKey.jpg" data="codes" title="getConfigByKey" imgstyle="width:800px;display: block;margin: 0 auto;" %}

Ou dans un bloc code:

```php
require_once dirname(__FILE__) . '/../../data/php/user.function.class.php';
$var = userFunction::getConfigByKey('info::latitude');
```

## pyJeedom

Si vous êtes un habitué du Python, le module pyJeedom permet d'accéder aux fonctions de l'api jsonrpc en python : [pyJeedom](https://github.com/KiboOst/pyJeedom)

<br/><br/>
*To be continued...*

