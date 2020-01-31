---
title: Rhasspy Assistant Tips n Tricks
description: Snowboy-CustomMaker for Rhasspy Assistant.
---

<img align="right" src="../images/rhasspyLogoLong.png" width="160" style="top: 15px">

# Snowboy-CustomMaker

[← Main page](../index.md)

Snowboy-CustomMaker is a set of python script to help recording custom wakeword samples and generate pmdl file.

## Installation

This tool require python 3 and four python package that you will need to install:

- numpy
- pyaudio
- soundfile
- requests

SSH to your rhasspy device, on /home/pi folder.
Install python packages, download snowboyCustomMaker-list.txt, then download this list into SnowboyCustomMaker folder:


```bash
sudo apt-get install python3-numpy python3-pyaudio python3-soundfile python3-requests
wget https://raw.githubusercontent.com/KiboOst/jeedom_docs/master/other/Rhasspy/SnowboyCustomMaker/snowboyCustomMaker-list.txt
wget -P /home/pi/SnowboyCustomMaker -i snowboyCustomMaker-list.txt
cd SnowboyCustomMaker
```

You now have three python scripts:
- snowboyRecord.py: Used to record your custom wakeword samples as wav files.
- snowboyTrain.py: Used to generate the pmdl file from
- utils.py: Just keep it there, used by the snowbiyRecord script.

You can have a look at these files [here](https://github.com/KiboOst/jeedom_docs/tree/master/other/Rhasspy/SnowboyCustomMaker)

## snowboyRecord

This script is based on [snips-record-personal-hotword](https://github.com/snipsco/snips-record-personal-hotword)
It have been converted to python3, cleaned, and rhasspied!

It will guide you through recording thee wave sample file to later generate your custom wakeword pdml file for Rhasspy (or whatever use snowboy wakeword).

```bash
cd SnowboyCustomMaker
python3 snowboyRecord.py --wakeword myhotword
```
**myhotword** is an identifier for your wakeword. The three sample files with be saved into SnowboyCustomMaker/myhotword folder, and **snowboyTrain** will get them to generate myhotword.pmdl file. You can use *heyJarvis_Dady* then later record *heyJarvis_Mom*, etc.

### Tips for recoding wakeword

Recording a custom wakeword is something sensible to get good detection without false positive detection.

Here are a few rules from my experience with both Snips and Snowboy:

- Record your samples on the same device that will handle wakeword detection. If you have one Rhasspy master and several Satellites, all with same ReSpeaker 2mic PiHat for example, you can use same pmdl file for all, as the hardware (even mixing Pi4 / Pi0) are the same. But don't record it on your desktop ...
- Each room, even the most silent one (you don't live in an anechoic chamber ...), have its own background noise signature. So, it's better to record samples in a room where you don't plan to use this wakeword. Not having this background noise in the wakeword will prevent some false positive.
- Obviously, move your Rasp into your most silent room for recording. No fridge noise, no PC or NAS fan noise, just ... no noise ! If you can hear something, move!
- snowboyRecord or whatever you use will create samples with leading and trailing noise. You will have to clean this before generating pmdl file! You can use free Audacity tool or any wave file editor.

{% include lightbox.html src="../images/customWakeword_cut.jpg" data="Snowboy-CustomMaker" title="Cut samples leading/trailing noise." imgstyle="width:500px;display: block;margin: 0 auto;" %}

## snowboyTrain

get token from website

```bash
cd SnowboyCustomMaker
python3 snowboyTrain.py --token ccccc0000000ccccccccccccc --lang fr --gender M --age 3 --wakeword myhotword
```
