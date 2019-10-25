---
title: Jeedom v4 | Astuces
description: Scénarios : Petits codes entre amis
---

<img align="right" src="../../images/logo-jeedom.png" width="100">

# Jeedom v4 | Scénarios : Petits codes entre amis

• [Astuces pour la personnalisation de l'interface](https://kiboost.github.io/jeedom_docs/jeedomV4Tips/Interface/fr_FR/)

#### Introduction

Vous le savez, un scénario est constitué de différents blocs (SI, A, DANS, etc), utilisés en fonction de ce que l'on désire faire.
L'un d'entre eux est le bloc CODE, peu engageant à première vue, mais pourtant bien pratique.

{% include lightbox.html src="../jeedomV4Tips/CodesScenario/images/code_example.jpg" data="dev tools" title="Bloc CODE" imgstyle="width:60 0px;display: block;margin: 0 auto;" %}

Ce type de bloc permet d'écrire du code php que le scénario va interpreter. par exemple :

```php
$trigger = $scenario->getTrigger();
$cmdID = str_replace('#', '', $trigger[0]);
$eq = cmd::byId($cmdID)->getEqLogic();
$eq->setIsEnable(0)->save()
```

C'est bien jolie, mais qu'est-ce qu'on peux faire avec ? Tout simplement accéder à toutes les fonctions php, mais aussi à la plupart des fonctions du core de Jeedom lui même, et donc aux équipements et à leurs commanders notamment.

Voici un lien vers la [doc de l'API Jeedom](https://jeedom.github.io/documentation/phpdoc/), qui permet de retrouver facilement les fonctions souhaitées. Vous pouvez également regarder directement dans le code source du core.


Il faut considérer un bloc Code comme un script php que vous éxécuter sur un serveur. Vous pouvez ainsi facilement récupérer des données de votre Jeedom, mais aussi des données sur Internet, dans un fichier sur un site ou autre. Même si pour des cas complexes, je préfère créer un Script avec le plugin Script.

Pour communiquer entre ce bloc CODE et le reste de votre scénarios, vous avez différentes options:

- Renseigner une variable de scénario, que vous pourrez ensuite tester / utiliser plus tard dans le scénario
```php
$scenario->setData('maVariable', '1');
```
- Mettre à jour la valeur d'une info d'un équipement, virtuel ou autre.
```php
cmd::byString('#[Maison][Planning][Mode]#')->event('Vacances');
```


### Quelques exemples

- Créer un message dans le centre de message
```php
$title = 'php testing';
$message = 'small message';
message::add($title, $message);
```

- Récupérer la valeur d'une variable
```php
$myVar = $scenario->getData('maVariable');
```

- Mettre à jour une commande info
```php
cmd::byString('#[Maison][infos][test]#')->event(100);
```

- Récupérer la valeur d'une commande info
```php
$value = cmd::byString('#[Maison][infos][test]#')->execCmd();
```

- Exécuter une commande action (même chose que pour une info)
```php
cmd::byString('#[Maison][actions][actionOn]#')->execCmd();
```

- Exécuter une commande action de type slider
```php
$options = array('slider'=>100);
cmd::byString('#[Salon][Lumière Salon][Intensité]#')->execCmd($options, $cache=0));
```

- Exécuter une commande action de type message
```php
$options = array('title'=>'pièce', 'message'=> 'Hello, how is it today ?');
cmd::byString('#[Maison][TTS][Speak]#')->execCmd($options, $cache=0));
```

- Récupérer la date de dernière mise à jour d'une info
```php
$cmd = cmd::byString('#[Maison][infos][test]#');
$collectDate = $cmd->getCollectDate();
```

- Ecrire dans un log
*Le niveau de log doit correspondre*
```php
log::add('maison', 'error', $value.'  : '.$collectDate);
```

- Ecrire dans le log du scénario
```php
$scenario->setLog('__'.$collectDate.' -> '.$value);
```

- Changer le cron d'un plugin. Je m'en sert pour passer le plugin Qivivo en cron15 hors période de chauffe
```php
config::save('functionality::cron5::enable', 0, 'qivivo');
config::save('functionality::cron15::enable', 1, 'qivivo');
```

- Faire un reset du swap de votre Jeedom
```php
$cmd = 'sudo swapoff -a && sudo swapon -a';
$result = exec($cmd);
$scenario->setLog($result);
```

- Masquer un objet
```php
object::byName('Cuisine')->setIsVisible(0)->save();
```

*To be continued...*
