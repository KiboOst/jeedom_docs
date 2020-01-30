---
title: Rhasspy Assistant Tips n Tricks
description: RhasspyBatchTester for Rhasspy Assistant.
---

<img align="right" src="../images/rhasspyLogoLong.png" width="160" style="top: 15px">

# Rhasspy-BatchTester

[← Main page](../index.md)

Rhasspy-BatchTester is a python script that provide a way to mass test intents.

You can test one or several sentences to intent recognition, or define a json with several sentences, intent that should be detected, and test it in one go with a report of matched / unmatched intents and there slots.

So, once you define new intents and re-train your rhasspy, just run the test to be sure it doesn't break other intents!

## Installation

*Coming soon ...*

## Common usage

You can use Rhasspy-BatchTester in two ways: test one single sentence, or feed a json file with sentences and test this json file.

Here is the structure of such json file:

```json
{
	"allume la lumière de la cuisine": "lightsTurnOnJeedom",
	"allume la lumière du canapé": "lightsTurnOnJeedom"
}
```

On the other hand, you can use this tool as a command line tool, or edit runTest.py file and start it.


## Command line usage

You can simply call the tool from command line, with some arguments.

Example with one single sentence to test:

```bash
cd Rhasspy-BatchTester
pyRhasspyBatcher --addr 192.168.0.140 --sentence "Turn light on in the kitchen" --intent "turnLightOn"

```

Available arguments are:

- --addr : http://IP adress of Rhasspy.
- --port' : Port of Rhasspy' (default='12101').
- --json' : json file path to test.
- --sentence' : A sentence to test.
- --intent' : The intent Name that should match --sentence.
- --debug' : debug level (default=0).

## Python script usage

in Rhasspy-BatchTester folder you will find a python script example to test:

`sudo nano /Rhasspy-BatchTester/runTest.py`

In this script, you can set your own arguments for later re-use, and what to do in `if rhasspy.connected condition`.

- `rhasspy.testSentence("allume la lumière de la cuisine", "lightsTurnOnJeedom")`
- `rhasspy.testJsonFile("mySentences.json")`


## Output example

Here is an example of what Rhasspy-BatchTester will output when testing:

```
[ MATCHED] lightsTurnOnJeedom | query: allume la lumière de la cuisine | confidence:1.0 | Slots: house_room : cuisine
[ MATCHED] turnOnJeedom | query: balance de la pop | confidence:1.0 | Slots: device_name : musique | music_genre : pop

matched: 2 | unmatched: 0 | total: 2
```

Of course, *unmatched: 0* is what to achieve ;-)



