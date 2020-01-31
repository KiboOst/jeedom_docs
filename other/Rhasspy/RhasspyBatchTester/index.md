---
title: Rhasspy Assistant Tips n Tricks
description: Rhasspy-BatchTester for Rhasspy Assistant.
---

<img align="right" src="../images/rhasspyLogoLong.png" width="160" style="top: 15px">

# Rhasspy-BatchTester

[← Main page](../index.md)

Rhasspy-BatchTester is a python script that provide a way to mass test intents.

You can test one or several sentences to Rhasspy intent recognition, or define a json file with several sentences and intent name that should match, and test it in one go.

So, once you define new intents and re-train your rhasspy, just run the test to be sure it doesn't break other intents!

## Installation

Nothing fancy here, just a python file ...
Download it on a PC or use wget to download it on your Rpi:

```bash
wget -P /home/pi/Rhasspy-BatchTester https://raw.githubusercontent.com/KiboOst/jeedom_docs/master/other/Rhasspy/RhasspyBatchTester/pyRhasspyBatcher.py
```

[pyRhasspyBatcher.py](https://github.com/KiboOst/jeedom_docs/tree/master/other/Rhasspy/RhasspyBatchTester/pyRhasspyBatcher.py)


## Common usage

You can use Rhasspy-BatchTester in two ways: test one single sentence, or feed a json file with sentences and test this json file.

Here is the structure of such json file:

```json
{
	"allume le champi d'axel pendant dix minutes": "TimeTurnOnJeedom",
	"allume la lumière du canapé": "lightsTurnOnJeedom"
}
```

On the other hand, you can use this tool as a command line tool, or edit runTest.py file and start it.


## Command line usage

You can simply call the tool from command line, with some arguments.

Example with one single sentence to test:

```bash
cd Rhasspy-BatchTester
python3 pyRhasspyBatcher.py --addr http://192.168.0.140 --sentence "Turn light on in the kitchen" --intent "turnLightOn"

```

Available arguments are:

- --addr : http://IP adress of Rhasspy.
- --port' : Port of Rhasspy' (default='12101').
- --json' : json file path to test.
- --sentence' : A sentence to test.
- --intent' : The intent Name that should match --sentence.
- --debug' : debug level (default=0).

## Python script usage

You can write your own python script and import rhasspyBatcher as a python module. This allow you to set your own default settings and run the script whenever you need.

<details>
<summary>Here is an example of script:</summary>

```python
#!/usr/bin/env python3
#-*- coding: UTF-8 -*-

from argparse import Namespace
from pyRhasspyBatcher import rhasspyBatcher

if __name__ == "__main__":
	args = Namespace(
					addr="http://192.168.0.140",
					port="12101",
					json='',
					sentence='',
					intent='',
					debug=0
					)

	rhasspy = rhasspyBatcher(args)

	if rhasspy.connected:
		rhasspy.testSentence("allume la lumière de la cuisine", "lightsTurnOnJeedom")
		#rhasspy.testJsonFile("mySentences.json")
	else:
		print('Could not connect to Rhasspy')
```

</details>

## Output example

Here is an example of what Rhasspy-BatchTester will output when testing:

```
[     MATCHED] ShutterOpenJeedom | query: ouvre un peu le volet du salon | confidence:1.0 | Slots:  | house_room : salon | window_devices : volet | window_state : peu
[     MATCHED] VolumeDownJeedom | query: baisse un peu le son | confidence:1.0 | Slots:  | ratio : peu
[     MATCHED] TurnOnJeedom | query: lance la musique | confidence:1.0 | Slots:  | device_name : musique
[     MATCHED] TurnOnJeedom | query: mets du jazz | confidence:1.0 | Slots:  | music_genre : Jazz
[     MATCHED] TurnOffJeedom | query: éteins le chauffage dans la salle | confidence:1.0 | Slots:  | device_name : chauffage | house_room : salle
[     MATCHED] ModeJeedom | query: passe les volets en manuel | confidence:1.0 | Slots:  | mode_name : volets | mode_type : manuel
[     MATCHED] departJeedom | query: on y va | confidence:1.0 | Slots:  | depart : depart
[     MATCHED] EntityStateValueJeedom | query: combien fait il dans la chambre d'axel | confidence:1.0 | Slots:  | device_name : temperature | house_room : axel
[     MATCHED] EntityStateValueJeedom | query: C'est quoi cette chanson ? | confidence:1.0 | Slots:  | device_name : musique
[     MATCHED] EntityStateValueJeedom | query: est ce que le volet de la chambre des parents est ouvert | confidence:1.0 | Slots:  | device_name : volet | house_room : parent
[     MATCHED] EntityStateValueJeedom | query: combien fait il dehors | confidence:1.0 | Slots:  | device_name : temperature | house_room : dehors
[     MATCHED] getWeather | query: quel temps il va faire demain | confidence:1.0 | Slots:  | when : forecast1
[     MATCHED] TimeTurnOnJeedom | query: allume le champi d'axel pendant dix minutes | confidence:1.0 | Slots:  | device_name : champi_Axel | duration_mins : 10
[     MATCHED] TimeTurnOffJeedom | query: laisse la cuisine éteinte pendant 25 minutes | confidence:1.0 | Slots:  | duration_mins : 25 | house_room : cuisine
[     MATCHED] searchPreviousDate | query: c'était quand les dernières vacances | confidence:1.0 | Slots:  | annual_event : vacances
matched: 22 | unmatched: 0 | total: 22
```

Of course, *unmatched: 0* is what to achieve ;-)



