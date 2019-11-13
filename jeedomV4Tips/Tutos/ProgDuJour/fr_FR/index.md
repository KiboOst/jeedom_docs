---
title: Jeedom v4 | Programmation du jour
description: Exemple de scénario de programmation journalière
---

<img align="right" src="../../../images/logo-jeedom.png" width="100">

# Jeedom v4 | Programmation du jour

{% capture my_include %}{% include ../../../common.md %}{% endcapture %}
{{ my_include | markdownify }}


## Introduction

Un sujet récurent pour les débutants de Jeedom, la programmation d’événements journaliers comme :

- Allumer la cafetière à 7h en semaine.
- Ouvrir les volets au lever du soleil.
- Fermer les volets au coucher du soleil, si je ne suis pas là.
- etc.

Il y a bien sûr maintes manières de le faire. Nous allons ici voir comment gérer tous nos événements de la journée avec un scénario, qui se chargera de déclencher les bonnes actions au bon moment.

## Principe

Un scénario est une suite logique d'actions, principalement des commandes action donc, à l’exécution du scénario ou à un horaire plus tard, selon des conditions définies si nécessaire.

Un scénario peut être lancé de deux façons :
- En mode déclenché, donc n'importe quand, sur une action. Cette action peu-être un bouton sur l'interface, le changement d'une valeur comme la détection d'une présence, le lancement par un autre scénario, etc.
- En mode programmé, donc à des horaires fixes.

C'est le mode programmé qui va nous intéresser ici.

Je ne vais pas rentrer dans les détails des paramètres, puisque la doc est plutôt complète : [La doc des scénario](https://jeedom.github.io/core/fr_FR/scenario)

{% include lightbox.html src="../jeedomV4Tips/Tutos/ProgDuJour/images/scenario_general.jpg" data="Scénario" title="Onglet Général" imgstyle="width:550px;display: block;margin: 0 auto;" %}

Nous avons un déclenchement programmé : `20 4 * * *`. Cela veut dire que notre scénario va se déclencher tout les jours à 4h20.
4h20 pour deux raisons : Il faut qu'il se déclenche avant le lever du soleil le plus tôt de l'année, pour pouvoir prévoir des actions au lever du soleil voir un peu avant. Logique non ?
Ensuite, pas 4h mais 4h20 car Jeedom exécute déjà certaines tâches toutes les heures, donc çà permet de ne pas charger encore plus Jeedom ce moment là. Ce sera insignifiant sur la plupart des configurations, mais sur certaines configurations chargées, çà permet d'optimiser un peu.


> **Tip**
>
> Le format des programmations horaire est un standard, une expression *cron*. Voir [crontab guru](https://crontab.guru/) pour en savoir plus.


## Réalisation

- Sur la page **Outils → Scénarios**, cliquez sur **Ajouter** en nommant votre scénario *Prog du jour* (Par exemple...).
- Définissez son Mode sur programmé, ajoutez une programmation, et entrer `20 4 * * *`.

Pour les groupes et objet parent je vous maître, vérifiez simplement qu'il est **Actif**.

Nous avons donc notre scénario qui va se déclencher tous les jours à 4h20, et ... ne rien faire ! :sweat_smile:

La suite se passe dans l'onglet **Scénario**.

Ici, trois types de blocs vont nous être utile.
- Le bloc **Si/Alors/Sinon** : Il va nous permettre de gérer des conditions, par exemple si nous sommes Dimanche.
- Le bloc **Action** : Il contient des actions à exécuter (Une action n'est pas forcément dans un bloc Action !).
- Le bloc **A** : Celui-ci va programmer ce qu'on veux à une heure précise de la journée (intéressant :grin: ! )

### Allumer la cafetière

Commençons par un exemple très simple, allumer la cafetière le matin à 6h, les jours ouvrées de la semaine.

Gardez en tête que ce scénario s’exécute tous les jours, à 4h20. Il faut donc *lire* ce scénario comme si nous étions n'importe quel jour, à 4h20.

On ne va pas allumer la cafetière les Samedi et Dimanche, donc nous allons d'abord vérifier le jour de la semaine.
Ensuite on va simplement dire, à 6h, fait çà.

> **Note**
>
> La programmation du scénario (le cron) nous permettrai de ne programmer le lancement que les Lundi, Mardi, Mercredi, Jeudi, Vendredi. Mais dans le cas d'un scénario de gestion journalière, il faut le lancer tous les jours, car d'autres actions pourront être effectuées / programmées le Samedi et le Dimanche.

Voici donc ce que çà donne :

{% include lightbox.html src="../jeedomV4Tips/Tutos/ProgDuJour/images/cafetiere.jpg" data="Scénario" title="Allumer la cafetière" imgstyle="width:550px;display: block;margin: 0 auto;" %}

> L'expression du SI, `#sjour# not in ['Samedi', 'Dimanche']` est équivalent à `#sjour# in ['Lundi', 'Mardi', 'Mercredi', 'Jeudi', 'Vendredi']`

Rien de bien méchant, vous en conviendrez ... :smiley:

> **Note**
>
> Notre scénario se déclenchant à 4h20, il n'aura pas de mal à programmer une tâche à 6h. Si vous programmez une tâche à un horaire passé, la tâche est programmée pour le lendemain.


### Mes volets

Dans le cas des volets en fonction des lever et coucher du soleil, nous allons avoir besoin des infos de ... lever et coucher du soleil !

> **Note**
>
> Les volets sont souvent ouverts à heure fixe le matin, pour éviter de se faire réveiller à 5h en été. Nous verrons donc ici le cas du coucher du soleil, mais le principe est exactement le même.

L'heure de coucher du soleil dépend de la date bien sûr, mais surtout de votre localisation (généralement, vos coordonnées GPS).
- Plusieurs plugins permettent d'avoir cette info. Le plus simple est sans doute le plugin [Weather](https://www.jeedom.com/market/index.php?v=d&p=market&type=plugin&plugin_id=7). Une fois installé et configuré, vous aurez alors l'info `#[Maison][Météo][Coucher du soleil]#`.
- Vous pouvez très simplement, sans aucun plugin, créer un bloc Code avec quelques lignes de php pour renseigner deux variables, que vous pourrez alors utiliser dans n'importe quel scénario.

Rendez-vous sur Google Map, placez un repère sur votre habitation, notez les coordonnées GPS qui s'affichent en bas.
Créez un bloc Code en début du scénario avec comme code (remplacer vos coordonnées) :

```php
$lat = 45.808;
$long = 4.872;
$sun_info = date_sun_info(time(), $lat, $long);
$sunrise = date("Hi", $sun_info["sunrise"]);
$sunset = date("Hi", $sun_info["sunset"]);
$scenario->setData('sunrise', $sunrise);
$scenario->setData('sunset', $sunset);
```

{% include lightbox.html src="../jeedomV4Tips/Tutos/ProgDuJour/images/suncode.jpg" data="Scénario" title="bloc Code lever/coucher du soleil" imgstyle="width:550px;display: block;margin: 0 auto;" %}

Ce code va simplement calculer les heures de lever et coucher du soleil et les renseigner dans deux variables, *sunrise* et *sunset*.

Aucun besoin de plugin, d'internet, d'API etc. Vous pouvez ensuite collapser le bloc et l'oublier :grin:
Les variables sont accessibles comme des commandes infos avec `variable(sunrise)`, et visible dans **Outils → Variables**

Il nous reste donc tout simplement à programmer notre fermeture des volets pour le soir :

{% include lightbox.html src="../jeedomV4Tips/Tutos/ProgDuJour/images/sunsetShutters.jpg" data="Scénario" title="Fermeture des volets au coucher du soleil" imgstyle="width:550px;display: block;margin: 0 auto;" %}

> *Quoi ? Et c'est tout ? Tout çà pour çà alors ?*

:stuck_out_tongue_winking_eye:

Ici, nous programmons A `time_op(variable(sunset), 60)`

La fonction **time_op** permet décaler un horaire. Ici on prend l'heure de coucher du soleil et on décale de 60 minutes, les volets se fermeront donc 1h après le coucher du soleil.
- Au coucher du soleil : `variable(sunset)`
- 20 mins avant le coucher du soleil : `time_op(variable(sunset), -20)`
- Bien sur, çà marche avec une commande info : `time_op(#[Maison][Météo][sunset]#, 60)`

### Volets automatique ou manuel

Allons un peu plus loin avec une gestion automatique ou manuelle des volets.

Pour çà, installez le plugin [Mode](https://www.jeedom.com/market/index.php?v=d&p=market&type=plugin&plugin_id=1929)
- Créez un nouveau Mode "Volets".
- Créez alors deux modes, "Auto" et "Manuel". Pas besoin d'action ou quoique ce soit d'autre dans notre cas.

Vous pourrez changer ce Mode par une action sur le Dashboard, par un scénario, avec Snips, etc.

Dans notre scénario, nous allons donc simplement vérifier que les volets sont en gestion automatique pour la fermeture.

{% include lightbox.html src="../jeedomV4Tips/Tutos/ProgDuJour/images/sunsetShuttersAuto.jpg" data="Scénario" title="Mode Volets auto" imgstyle="width:550px;display: block;margin: 0 auto;" %}

Et voilà, donc 1h après le coucher du soleil, si la gestion est bien automatique, alors le volet se fermera.

> **Tip**
>
> La condition `#[Maison][Volets][Mode]# == 'Auto' ` est placée dans le bloc A, ce qui veux dire que celle-ci sera vérifiée à l'heure de fermeture des volets. En effet, vous pourriez mettre le SI avant, mais rappelez vous que le scénario s’exécute à 4h20. Donc si à 4h20 vous êtes en gestion manuelle, la fermeture ne sera pas programmée. Donc même si vous passez en gestion auto dans la journée, il ne se fermera pas. En mettant la condition à l'heure de fermeture, elle sera vérifiée à cette heure et tiendra donc compte d'un changement de gestion dans la journée.

:innocent:
