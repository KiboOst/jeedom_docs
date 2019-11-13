---
title: Jeedom v4 | Programmation du jour
description: Exemple de scénario de programmation journalière
---

<img align="right" src="../../images/logo-jeedom.png" width="100">

# Jeedom v4 | Programmation du jour

• [Astuces pour la personnalisation de l'interface](https://kiboost.github.io/jeedom_docs/jeedomV4Tips/Interface/fr_FR/)
• [Scénarios : Petits codes entre amis](https://kiboost.github.io/jeedom_docs/jeedomV4Tips/CodesScenario/fr_FR/)

## Introduction

Un sujet récurent pour les débutants de Jeedom, la programmation d’événements journaliers comme :

- Ouvrir les volets au levé du soleil.
- Fermer les volets au couché du soleil, si je ne suis pas là.
- Allumer la cafetière à 7h en semaine.
etc

Il y a bien sûr maintes manières de le faire. Nous allons ici voir comment gérer tout nos événements de la journée avec un scénario, qui se chargera de déclencher les bonnes actions au bon moment.

## Principe

Un scénario est une suite logique d'actions, principalement des commandes action donc, à l’exécution du scénario ou à un horaire plus tard, selon des conditions définies si nécessaire.

Un scénario peut être lancé de deux façons :
- En mode déclenché, donc n'importe quand, sur une action. Cette action peu-être un bouton sur l'interface, le changement d'une valeur comme la détection d'une présence, le lancement par un autre scénario, etc.
- En mode programmé, donc à des horaires fixes.

C'est le mode programmé qui va nous intéresser ici.

Je ne vais pas rentrer dans les détails des paramètres, puisque la doc est plutôt complète : [La doc des scénario](https://jeedom.github.io/core/fr_FR/scenario)

{% include lightbox.html src="../jeedomV4Tips/Tutos/ProgDuJour/images/scenario_general.jpg" data="Scénario" title="Onglet Général" imgstyle="width:550px;display: block;margin: 0 auto;" %}

Ce qui nous intéresse ici :
- Nous avons un déclenchement programmé : `20 4 * * *`. Cela veut dire que notre scénario va se déclencher tout les jours à 4h20. 4h20 pour deux raisons : Il faut qu'il se déclenche avant le levé du soleil le plus tôt de l'année, pour pouvoir prévoir des actions au levé du soleil voir un peu avant. Logique non ? Ensuite, pas 4h mais 4h20 car Jeedom exécute déjà certaines tâches toutes les heures, donc çà permet de ne pas chargé encore plus Jeedom à heure fixe. C'est insignifiant sur la plupart des configurations, mais sur certaines configurations chargées, çà permet d'optimiser un peu.


> **Tip**
>
> Le format des programmations horaire est un standard, une expression *cron*. Je vous conseille [crontab guru](https://crontab.guru/) pour en savoir plus.


## Réalisation

- Sur la page **Outils → Scénarios**, cliquez sur **Ajouter ** en nommant votre scénario *Prog du jour* (Par exemple...).
- Définissez son Mode sur programmé, ajoutez une programmation, et entrer `20 4 * * *`.
Pour les groupes et objet parent je vous maître, vérifiez simplement qu'il est **Actif**.

Nous avons donc notre scénario qui va se déclencher tout les jours à 4h20, et ... ne rien faire ! :sweat_smile:

La suite se passe dans l'onglet Scénario.

Ici, trois types de blocs vont nous être utile.
- Le bloc Si/Alors/Sinon : Il va nous permettre de gérer des conditions, par exemple si nous sommes Dimanche.
- Le bloc Action : Il contient des actions à exécuter (Une action n'est pas forcément dans un bloc Action !).
- Le bloc A : Celui-ci va programmer ce qu'on veux à une heure de la journée (intéressant :grin: ! )

### Allumer la cafetière

Commençons par un exemple très simple, allumer la cafetière le matin à 6h, les jours de la semaine.

Gardez en tête que ce scénario s’exécute tout les jours, à 4h20. Il faut donc *lire* ce scénario comme si nous étions n'importe quel jour, à 4h20.

On ne va pas allumer la cafetière les Samedi et Dimanche, donc nous allons d'abord vérifier le jour de la semaine.
Ensuite on va simplement dire, à 6h, fait çà.

> **Note**
>
> La programmation du scénario (le cron) nous permettrai de ne programmer le lancement que les Lundi, Mardi, Mercredi, Jeudi, Vendredi. Mais dans le cas d'un scénario de gestion journalière, il faut le lancer tout les jours, car d'autres actions pourront être effectuées / programmées le Samedi et le Dimanche.

Voici donc ce que çà donne :

{% include lightbox.html src="../jeedomV4Tips/Tutos/ProgDuJour/images/cafetiere.jpg" data="Scénario" title="Allumer la cafetière" imgstyle="width:550px;display: block;margin: 0 auto;" %}

> L'expression du SI, `#sjour# not in ['Samedi', 'Dimanche']` est équivalent à `#sjour# in ['Lundi', 'Mardi', 'Mercredi', 'Jeudi', 'Vendredi']`

Rien de bien méchant, vous en conviendrez ... :smiley:

> **Note**
>
> Notre scénario se déclenchant à 4h20, il n'aura pas de mal à programmer une tâche à 6h. Si vous programmez une tâche à un horaire passé, la tâche est programmée pour le lendemain.


### Mes volets

Dans le cas des volets en fonction des levés et couchés du soleil, nous allons avoir besoin des infos de ... levé et couché du soleil !
