---
title: Rhasspy Assistant Tips n Tricks
description: Snowboy-CustomMaker for Rhasspy Assistant.
---

<img align="right" src="../images/rhasspyLogoLong.png" width="160" style="top: 15px">

# Snowboy-CustomMaker

[← Main page](../index.md)

Snowboy-CustomMaker is a set of python scripts and tips to help recording custom wakeword samples and generate pmdl file.

## Installation

This tool require python 3 and four python packages to run:

- numpy
- pyaudio
- soundfile
- requests

SSH to your rhasspy device, on /home/pi folder.

Install python packages, download *snowboyCustomMaker-list.txt*, then download this list into SnowboyCustomMaker folder:


```bash
sudo apt-get install python3-numpy python3-pyaudio python3-soundfile python3-requests
wget https://raw.githubusercontent.com/KiboOst/jeedom_docs/master/other/Rhasspy/SnowboyCustomMaker/snowboyCustomMaker-list.txt
wget -P /home/pi/SnowboyCustomMaker -i snowboyCustomMaker-list.txt
cd SnowboyCustomMaker
```

You should get three python scripts:
- **snowboyRecord.py**: Used to record your custom wakeword samples as wav files.
- **snowboyTrain.py**: Used to generate the pmdl file from
- utils.py: Just keep it there, used by the snowboyRecord script.

You can have a look at these files [here](https://github.com/KiboOst/jeedom_docs/tree/master/other/Rhasspy/SnowboyCustomMaker)

## snowboyRecord

This script is based on [snips-record-personal-hotword](https://github.com/snipsco/snips-record-personal-hotword).

It have been converted to python3, cleaned, enhanced and snowboyed!

It will guide you through recording three wave sample files to later generate your custom wakeword pdml file for Rhasspy (or whatever use snowboy wakeword).

<details>
<summary>Why not just record samples with arecord ?</summary>

Indeed, we can use arecord to get our three sample wav files:

```bash
arecord -D 'sysdefault:CARD=seeed2micvoicec' -r 16000 -f S16_LE -c 1 -t wav > 0.wav
ctrl C
```

snowboyRecord script check each recorded sample for noise, and if there is too much noise it will display a warning and record a new one.
If there is too much noise in the room, you will simply be unable to validate your records. Which will avoid generating a pmdl file that will cause many false positive!

It will also check duration consistency between samples. So you can end up recording not three, but more ...

Finally, snowboyRecord will also automatically cut leading and trailing noise/silence in the wav file, to ensure better wakeword definition.

</details>

First you will have to free-up access to microphone, so shutdown Rhasspy: `docker stop rhasspy-server`

Then, run snowboyRecord:

```bash
cd SnowboyCustomMaker
python3 snowboyRecord.py --wakeword myhotword
```
**myhotword** is an identifier for your wakeword.

The three sample files with be saved into SnowboyCustomMaker/myhotword folder, and **snowboyTrain** will get them to generate **myhotword.pmdl** file.

You can use for example *heyJarvis_Dady* then later record *heyJarvis_Mom*, etc.

> While running the script with a previously used identifier, it will delete previous saved folder!

At the end you will end-up with a *myhotword* folder with six wav files: three samples, two files per sample. For each sample you will have a x_uncut.wav which is the original recorded wav. The x.wav has been cut (leading and trailing noise/silence) by snowboyRecord.


### Tips for recoding wakeword

Recording a custom wakeword is something sensible to get good detection without false positive detection.

Here are a few rules from my experience with both Snips and Snowboy:

- Record your samples on the same device that will handle wakeword detection. If you have one Rhasspy master and several Satellites, all with same ReSpeaker 2mic PiHat for example, you can use same pmdl file for all, as the hardware (even mixing Pi4 / Pi0) are the same. But don't record it on your desktop ...
- Each room, even the most silent one (you don't live in an anechoic chamber ...), have its own background noise signature. So, it's better to record samples in a room where you don't plan to use this wakeword. Not having this background noise in the wakeword will prevent some false positive.
- Obviously, move your Rasp into your most silent room for recording. No fridge noise, no PC or NAS fan noise, just ... no noise ! If you can hear something, move!
- snowboyRecord will automatically cut leading and trailing noise/silence in your sample. If you use arecord or another tool, you will have to clean each sample before generating pmdl file! You can use free Audacity tool or any wave file editor. Check a x_uncut.wav sample for example.

{% include lightbox.html src="../other/Rhasspy/images/customWakeword_cut.jpg" data="Snowboy-CustomMaker" title="Cut samples leading/trailing noise." imgstyle="width:500px;display: block;margin: 0 auto;" %}

## snowboyTrain

snowboyTrain will load your previously recorded samples and connect to snowboy.kitt.ai API to generate corresponding pmdl file.

> Don't forget to clean each samples! See above *Tips for recoding wakeword*

You will need an API token for this : go to [snowboy.kitt.ai](https://snowboy.kitt.ai/) and login (you can login with Github account), then get your token from your profile.

{% include lightbox.html src="../other/Rhasspy/images/snowboy_token.jpg" data="Snowboy-CustomMaker" title="Get your API token." imgstyle="width:500px;display: block;margin: 0 auto;" %}

Then, start snowboyTrain with your token and your previously recorded wakeword identifier (see above).

```bash
cd SnowboyCustomMaker
python3 snowboyTrain.py --token ccccc0000000ccccccccccccc --lang fr --gender M --age 30 --wakeword myhotword
```

> run `python3 snowboyTrain.py -h` to see arguments options.

You should now have your pmdl file in `/home/pi/SnowboyCustomMaker/myhotword/myhotword.pmdl`.

Move it in your Rhasspy profile like `/home/pi/.config/rhasspy/profiles/fr/snowboy/myhotword.pmdl` and set it in Rhasspy settings (snowboy/myhotword.pmdl).

Don't forget to check Rhasspy official [documentation](https://rhasspy.readthedocs.io/en/latest/wake-word/#snowboy) on using snowboy wake word detector!