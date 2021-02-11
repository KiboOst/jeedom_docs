---
title: Rhasspy Assistant Tips n Tricks
description: HermesLedControl for Rhasspy Assistant.
---

<img align="right" src="../images/rhasspyLogoLong.png" width="160" style="top: 15px">

# HermesLedControl

[← Main page](../index.md)

[Official repository](https://github.com/project-alice-assistant/HermesLedControl)

## HLC setup for Rhasspy

Installation of HLC is rather simple and documented [here](https://github.com/project-alice-assistant/HermesLedControl/wiki/Installation-&-update)


### Installation

```bash
wget https://gist.githubusercontent.com/Psychokiller1888/a9826f92c5a3c5d03f34d182fda1ce4c/raw/cbb53252dd55dc4e9f5f6064a493f0981cf133fb/hlc_download.sh
sudo chmod +x hlc_download.sh
sudo ./hlc_download.sh
```

Before starting it, we will have to configure service file for Rhasspy.

The important command line parameters are:
> --engine<br />
> --pathToConfig

Edit the service file and change **ExecStart** line as follow:

*Adapt HLC version number, your profile path (en instead of fr ?) and your hardware if needed*


```bash
sudo nano /etc/systemd/system/hermesledcontrol.service
```

```bash
ExecStart=/home/pi/hermesLedControl_v2.0.3/venv/bin/python3 main.py --engine=rhasspy --pathToConfig=/home/pi/.config/rhasspy/profiles/fr/profile.json --hardware=respeaker2 --pattern=kiboost
```
Then reload daemon and sart it:

```bash
sudo systemctl daemon-reload
sudo systemctl start hermesledcontrol
```

### ReSpeaker button

HLC allow to map some function on button pressed. For this, edit your pattern file in `hermesLedControl_v2.0.x/ledPatterns/yourPattern.py`

<details>
<summary>Example toggling rhasspy wakeword:</summary>

```python
from subprocess import call

	def __init__(self, controller):
		super(KiboostLedPattern, self).__init__(controller)
		self.host = '192.168.0.140'
		self.muted = False

	def idle(self, *args): #continuous blue breathing
		self.off()
		self._animation.set()
		middleLed = int(self._numLeds/2)
		if self.muted:
			self._controller.setLed(middleLed, 85, 0, 0, 75)
		else:
			self._controller.setLed(middleLed, 0, 85, 0, 75)
		self._controller.show()

	def onButton1(self, *args):
		#mute hotword detection:
		self._animation.clear()
		self.off()
		if self.muted:
			self.muted = False
			topic = "hermes/hotword/toggleOn"
		else:
			self.muted = True
			topic = "hermes/hotword/toggleOff"

		payload = '{"siteId": "'+self._controller._mainClass._me+'", "reason": ""}'
		self._controller._mainClass._mqttClient.publish(topic, payload)

		self.off()
		self._controller.idle()
```

</details>

Pressing the button will toggle wakeword service, and set *self.muted* variable accordingly so idle LEDS will show middle led green or middle led red if muted.

### Turn LEDs on/off

HLC have topics to turn LEDs on and off. Just run this command on the master Rhasspy:

```bash
mosquitto_pub -p 1883 -t 'hermes/leds/toggleOn' -m '{"siteId" : "salle"}'
mosquitto_pub -p 1883 -t 'hermes/leds/toggleOff' -m '{"siteId" : "salle"}'
```

> Tips
>
> If you install several Rhasspy with a master and satellites, keep in mind that each device should have its MQTT host setting to the master IP.

### debug

Start the service: `sudo systemctl start hermesledcontrol`<br />
Stop the service: `sudo systemctl stop hermesledcontrol`<br />
Restart the service: `sudo systemctl restart hermesledcontrol`<br />
Show service log: `journalctl -u hermesledcontrol.service`<br />


