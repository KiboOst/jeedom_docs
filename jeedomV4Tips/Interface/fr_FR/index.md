---
title: Jeedom v4 | Interface
description: Astuces pour la personnalisation de l'interface de Jeedom v4
---

<img align="right" src="../../images/logo-jeedom.png" width="100">

# Jeedom v4 | Astuces pour la personnalisation de l'interface

• [Scénarios : Programmation du jour](https://kiboost.github.io/jeedom_docs/jeedomV4Tips/Tutos/ProgDuJour/fr_FR/)<br>
• [Scénarios : Petits codes entre amis](https://kiboost.github.io/jeedom_docs/jeedomV4Tips/CodesScenario/fr_FR/)<br>

[Introduction](#introduction)<br />
[Plugin Mode coloré](#plugin-mode-color)<br />
[Changer certaines couleurs de l’interface](#changer-certaines-couleurs-de-linterface)<br />
[Autre exemples](#autre-exemples)<br />
[Affichage des scénarios sur un design](#affichage-des-scnarios-sur-un-design)<br />
[Couleur d’arrière plan des designs](#couleur-darrire-plan-des-designs)<br />
[Des dummies sur le Dashboard](#des-emdummiesem-sur-le-dashboard)<br />

## Introduction

Plusieurs choses sont paramétrables nativement dans ***Réglages / Système / Configuration, Interface***.

{% include lightbox.html src="../jeedomV4Tips/Interface/images/interface_settings.jpg" data="interface" title="Paramètres d'Interface" imgstyle="width:550px;display: block;margin: 0 auto;" %}
Référez vous à la documentation, ou à l'aide sur chaque paramètre.

Jeedom propose aussi d'inclure des ***Personnalisation avancée***.
Vous pouvez ainsi paramétrer vos propres fonctions javascript et/ou règles css, pour le desktop ou la webapp (mobile).
Pour y accéder : ***Réglages / Système / Personnalisation avancée***

Concernant les règles css, vous aurez probablement besoin de connaître les bons sélecteurs (sur quels éléments s'appliquent les règles css définies). Pour cela, quasiment tous les navigateurs proposent des *Outils de développement*, généralement accessibles par Ctrl+Shift+I (ou par le menu bien sûr).

Voici un exemple dans Firefox. En cliquant sur l'icône en haut à gauche, puis en pointant le curseur sur l'élément de la page que vous souhaitez, vous accédez directement à son code html, où vous pouvez voir ses classes css, id, sa structure, etc.

{% include lightbox.html src="../jeedomV4Tips/Interface/images/devTools.jpg" data="interface" title="Outils de développement Firefox" imgstyle="width:550px;display: block;margin: 0 auto;" %}

### Remarque

Depuis la version 4.1 de Jeedom, vous pouvez ajouter une classe CSS en Desktop et/ou Mobile sur un équipement.
Pour cela, allez sur la page de votre équipement, configuration avancée, onglet Affichage. Ajoutez un Paramètre Optionnel sur la Tuile avec comme nom *dashboard_class* et/ou *mobile_class* et comme valeur la classe CSS que vous souhaitez.

Sur le Dashboard, une Vue, un Design, ou une page Equipements en Mobile, cette tuile aura alors la classe CSS que vous avez définit.

Cela permet ensuite, en customisation avancée, de définir des règles CSS sur cette tuile, ou toutes les tuiles qui auront cette class CSS !

## Plugin Mode coloré

Si vous souhaitez ne pas avoir toutes les icônes de l'interface colorées, il vous suffit de décocher l'option *icônes widgets colorées* dans les réglages.
Avec ce paramètre, aucun widget, ni objet, ni plugin n'aura d'icône colorée.
Si toutefois vous souhaitez disposer quand même des modes colorés du plugin Mode, voici ce qu'il suffit d'ajouter en ***Personnalisation avancée***, css desktop et/ou mobile:

```css
[data-eqtype="mode"] .icon_blue { color: var(--al-info-color) !important; }
[data-eqtype="mode"] .icon_green { color: var(--bt-success-color) !important; }
[data-eqtype="mode"] .icon_orange { color: var(--al-warning-color) !important; }
[data-eqtype="mode"] .icon_red { color: var(--al-danger-color) !important; }
[data-eqtype="mode"] .icon_yellow { color: var(--lb-yellow-color) !important; }
```
Vous pouvez adapter ce code à n'importe quel plugin supportant les icônes colorées en modifiant le sélecteur ```[data-eqtype="mode"]``` (voir introduction ci dessus).

## Changer certaines couleurs de l'interface
La v4 de Jeedom est une réécriture complète de son design et de la façon dont il est appliqué. Les versions précédentes s'appuyaient énormément sur du code css sur les éléments (*inline style*), alors que la v4 possède un système de design et de thème global, plus efficace (et moderne). Ce système s'appuie notamment sur l'utilisation de variables css, utilisées par les différents thèmes pour changer les couleurs. Ce qui va nous permettre de jouer aussi sur ces couleurs, toujours dans la partie css des ***Personnalisation avancée***.

> Vous verrez dans les exemples suivant que les couleurs sont parfois définies en rgb(x,x,x) ou directement en x,x,x. Veuillez à respecter le format original.

#### Les couleurs de catégories d'équipement
Voici les couleurs de catégories de la v3. Ce n'est qu'un exemple, puisque bien sûr les couleurs de catégories des thèmes Light et Dark sont différentes, pour s'intégrer au mieux à chaque thème dans son ensemble.
```css
:root {
  --cat-security-color: 155, 75, 70;
  --cat-heating-color: 46, 141, 205;
  --cat-automatism-color: 128, 128, 128;
  --cat-light-color: 243, 156, 18;
  --cat-multimedia-color: 52, 73, 94;
  --cat-energy-color: 46, 176, 75;
  --cat-other-color: 25, 188, 156;
  --cat-scenario-color: 127, 140, 141;
}
```
#### Les couleurs de blocs de scénarios
Avec la v4, les couleurs des blocs de scénarios ne sont plus attribuées aléatoirement mais par type de bloc. La correspondances avec la v3 n'est donc pas possible, et je suis plus pour s'adapter que pour l'immobilisme dans le passé, mais voici par exemple celle du thème v4 Dark. A noter qu'en V3 il était totalement impossible de changer ces couleurs :wink:.

```css
:root {
  --scBlocIF: rgb(65,90,110);
  --scBlocElse: rgb(50,75,95);
  --scBlocACTION: rgb(132,120,112);
  --scBlocIN: rgb(75,128,62);
  --scBlocAT: rgb(92,122,132);
  --scBlocFOR: rgb(152,116,22);
  --scBlocCODE: rgb(160,60,25);
  --scBlocCOM: rgb(60,60,60);

  --scBlocSep: rgb(35,35,35);
}
```
## Autre exemples

Parce que l'équipe se doit de faire des choix, et qu'ils peuvent ne pas correspondre à tout le monde dans les dizaines de milliers d'utilisateurs, voici quelques exemples que vous pouvez appliquer sur votre Jeedom :sweat_smile:.

<br/>• Aligner les noms des objets à gauche sur le *Dashboard*:
```css
[data-page="dashboard"] legend {
  text-align: left !important;
}
```

<br/>• Conserver la barre de recherche en haut du *Dashboard*:
```css
#dashTopBar {
  position: fixed;
  top: 55px;
  z-index: 5000;
  width: calc(100% - 36px);
}
```

<br/>• Supprimer des éléments du menu **Accueil** (Ici, aucun ne sera visible !):
```css
#bt_gotoOverview,
#bt_gotoDashboard,
#bt_gotoView,
#bt_gotoPlan,
#bt_gotoPlan3d {
  display: none;
}
```

<br/>• Arrondi différent en Desktop et Mobile:
Réglez **Réglages → Système → Configuration / Interface** à 0,2 pour le Desktop, puis en personnalisation, onglet Mobile:
```css
body {
  --border-radius:0.6rem !important;
}
```

<br/>• Changement du background des tuiles sur le *Dashboard* (ici couleur v4 thème dark) :
```css
:root {
  --eq-bg-color: 38, 38, 38;
}
```

<br/>• Changement du background des pages (ici couleur v4 thème dark) :
```css
:root {
  --bg-color: 25, 25, 25;
}
```

<br/>• Changement des couleurs de texte et de lien (ici couleur v4 thème dark) :
```css
:root {
  --linkHover-color: rgb(228, 228, 228);
  --linkHoverLight-color: rgb(230, 230, 230);
}
```

<br/>• Changement de la taille de police des résumés (barre de menu):
```css
.objectSummaryParent {
	font-size: 14px;
}
```

<br/>• Changement de la couleur du bandeau d'un équipement en particulier:
```css
[data-eqlogic_id="670"] .widget-name {
	background-color: rgb(50,60,80);
}
/* for dark theme only*/
[data-theme="core2019_Dark"] [data-eqlogic_id="3"] .widget-name {
	background-color: rgb(50,60,80);
}
```

<br/>• Dashboard sur deux colonnes (ici, au delà de 1400px de large):
```css
@media screen and (min-width: 1400px) {
  [data-page="dashboard"] #div_displayObject .row div.col-md-12 {
    width: 50% !important;
  }
}
```

<br/>• Spécial développeurs et beta-testeurs : Toujours afficher le badge d'update :
```css
#span_nbUpdate[style*="display : none"] {
  display: block !important;
  visibility: hidden;
}
#span_nbUpdate[style*="display : none"]:after {
  font-family: "Font Awesome 5 Free";
  font-weight: 900;
  content:'\f021';
  font-size: 8px;
  visibility: visible;
  display: block;
  position: absolute;
  background-color: var(--al-danger-color);
  padding: 4px;
  top: 18px;
  left: 32px;
  border-radius: var(--border-radius) !important;
}
```


### Affichage des logs

Vous pouvez changer la manière dont les logs sont affichés sur la page Analyse / Logs:
```css
#pre_globallog {
  font-family: "verdana";
  font-size: 14px;
  letter-spacing: 0.1em;
  line-height: 14px;
}
```

Et pour inclure les logs de scénarios:
```css
#pre_globallog,
#pre_scenariolog {
	...
```

## Affichage des scénarios sur un design

Les scénarios sont affichés sur les *designs* de la même façon que sur le *Dashboard*, sous forme de tuile. On peux leur donner un visuel beaucoup plus compact:
{% include lightbox.html src="../jeedomV4Tips/Interface/images/scenario_design.jpg" data="interface" title="Scénario compact" imgstyle="width:508px;display: block;margin: 0 auto;" %}
```css
/* scenario display design */
[data-page="plan"] .scenario-widget.scenario {
  min-width: 75px;
  height: 25px!important;
  background-color: rgba(var(--cat-scenario-color), var(--opacity)) !important;
}
[data-page="plan"] .scenario-widget.scenario a[class~="changeScenarioState"] {
  position: absolute;
  top: 7px;
  left: 5px;
  height: 22px;
}
[data-page="plan"] .scenario-widget.scenario a[class~="changeScenarioState"] { padding: 3px }
[data-page="plan"] .scenario-widget.scenario a[data-state="start"] { left: 40px; }
[data-page="plan"] .scenario-widget.scenario .widget-name {
  position: absolute;
  top: 0;
  left: 80px;
  background: transparent !important;
}
[data-page="plan"] .scenario-widget.scenario .iconCmd i {
  position: absolute;
  top: 10px;
  right: 5px;
  font-size: 16px !important;
  color: var(--sc-lightTxt-color) !important;
}
```

## Couleur d'arrière plan des designs

Si vous affichez les images de fonds, celles-ci peuvent perturber la lisibilité des designs sur fond transparent. Mais si vous spécifiez une couleur, celle-ci est la même quel que soit le thème.
Vous pouvez ou spécifier la variable de couleur de fond du thème, ou une couleur définie par thème:

```css
[data-page="plan"] .div_displayObject {
  background-color: rgb(var(--bg-color)) !important;
}

/* by theme color */
[data-page="plan"][data-theme="core2019_Light"] .div_displayObject {
  background-color: rgb(235,235,235) !important;
}
[data-page="plan"][data-theme="core2019_Dark"] .div_displayObject {
  background-color: rgb(35,35,35) !important;
}
```

## Des *dummies* sur le Dashboard

Si vous souhaitez avoir des tuiles invisible sur le Dashboard pour créer des espaces entre deux tuiles, voici comment créer un dummy :

{% include lightbox.html src="../jeedomV4Tips/Interface/images/dummy.jpg" data="interface" title="Dummy sur le Dashboard" imgstyle="width:508px;display: block;margin: 0 auto;" %}

- Installez le plugin [HTML Display](https://www.jeedom.com/market/index.php?v=d&p=market&type=plugin&plugin_id=3843).
- Créez un équipement avec comme parent l'objet où vous voulez l'insérer.
- Mettez ceci en code (onglet Dashboard):

```
<div id="dummy"></div>
<script>
  $('#dummy').closest('.eqLogic-widget').addClass('dummy')
</script>
```

Pour comme css:
```css
[data-page="dashboard"] .dummy:not(.editingMode) {
  opacity: 0;
}
```

Sur la Dashboard, passez en Mode Edition et déplacez / redimensionnez le comme vous voulez :kissing:.

*To be continued...*

Vous pouvez jeter un œil au fichier css du core comportant, pour chaque thème, les variables définies :
[colors.css thème Dark](https://github.com/jeedom/core/blob/alpha/core/themes/core2019_Dark/desktop/colors.css)
