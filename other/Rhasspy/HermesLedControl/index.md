---
title: Rhasspy Assistant Tips n Tricks
description: HermesLedControl for Rhasspy Assistant.
---

<img align="right" src="../images/rhasspyLogoLong.png" width="160" style="top: 15px">

# HermesLedControl

[Official repository](https://github.com/project-alice-assistant/HermesLedControl)

## HLC setup for Rhasspy

Installation of HLC is rather simple and documented [here](https://github.com/project-alice-assistant/HermesLedControl/wiki/Installation-&-update)

> Important
>
> Actually it doesn't work like advertised with Rhasspy, as Rhasspy doesn't publish all standard Hermes topics over MQTT. This should come soon with next big Rhasspy update!

### Installation

```bash
wget https://gist.githubusercontent.com/Psychokiller1888/a9826f92c5a3c5d03f34d182fda1ce4c/raw/cbb53252dd55dc4e9f5f6064a493f0981cf133fb/hlc_download.sh
sudo chmod +x hlc_download.sh
sudo ./hlc_download.sh
```

Before starting it, we will have to configure service file for Rhasspy.

The important command line parameters are:
> --engine=rhasspy<br />
> --pathToConfig=/home/pi/.config/rhasspy/profiles/fr/profile.json

Edit the service file and change **ExecStart** line as follow:

Adapt HLC version number, your profile path (en instead of fr ?) and your hardware if needed:


```bash
sudo nano /etc/systemd/system/hermesledcontrol.service
```

```bash
ExecStart=/home/pi/hermesLedControl_v2.0.1/venv/bin/python3 main.py --engine=rhasspy --pathToConfig=/home/pi/.config/rhasspy/profiles/fr/profile.json --hardware=respeaker2 --pattern=kiboost
```

Then reload daemon and sart it:

```bash
sudo systemctl daemon-reload
sudo systemctl start hermesledcontrol
```

### ReSpeaker button

HLC allow to map some function on button pressed.

Actually, Rhasspy doesn't allow to stop/start wakeword service, but this should come later.

Here is an example toggling snips wakeword service:

```python
def idle(self, *args):
	self.off()
	self._animation.set()
	if self.muted:
		middleLed = int(self._numLeds/2)
		while self._animation.isSet():
			self.breathLeds(1.35, [0, 0, 75], [middleLed])
	else:
		while self._animation.isSet():
			self.breathLeds(1.35, [0, 0, 75])

def onButton1(self, *args):
	#mute hotword detection:
	self._animation.clear()
	self.off()
	if self.muted:
		self.muted = False
		call('sudo systemctl start snips-hotword.service', shell=True)
	else:
		self.muted = True
		call('sudo systemctl stop snips-hotword.service', shell=True)
	self._controller.idle()
```

Pressing the button will toggle wakeword service, and set *self.muted* variable accordingly so idle LEDS will show three leds breathing or only the middle one if muted.

### debug

Start the service: `sudo systemctl start hermesledcontrol`<br />
Stop the service: `sudo systemctl stop hermesledcontrol`<br />
Restart the service: `sudo systemctl restart hermesledcontrol`<br />
Show service log: `journalctl -u hermesledcontrol.service`<br />


