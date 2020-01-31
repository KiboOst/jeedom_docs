---
title: Rhasspy Assistant Tips n Tricks
description: Some unofficial doc and tools for Rhasspy Assistant.
---

<img align="right" src="images/rhasspyLogoLong.png" width="160" style="top: 15px">

# Rhasspy Assistant

**summary**

[Common commands](#common-commands)<br />
[3rdparty installations](#rdparty-installations)<br />
[Custom tools](#custom-tools)<br />

## Introduction

**Rhasspy** is an open source, fully offline voice assistant toolkit.

After Sonos literally killed Snips, a lot of users switched to Rhasspy, which get actively developed and enhanced into an amazing fully customizable offline assistant.

Once installed and setup, you can define all intents, slots and interact everyday with it, without any Internet connection. All settings and intents/slots definition are available through Rhasspy own on Pi interface. Welcome private life!

The official documentation is rather complete and enough to set it up and running so I won't rewrite it, but focus on tips and add-on tools.

Before going further, you should ever know these:
- [Official documentation](https://rhasspy.readthedocs.io/en/latest/)
- [Official community](https://community.rhasspy.org/)
- [Official repository](https://github.com/rhasspy)

Rhasspy also have its own plugin for **Jeedom** smart-home solution
- [jeeRhasspy documentation](https://kiboost.github.io/jeedom_docs/plugins/jeerhasspy/fr_FR/)
- [jeeRhasspy on the market](https://www.jeedom.com/market/index.php?v=d&p=market&type=plugin&plugin_id=3869)


## Common commands

A few common used ssh commands.

### Startup commands

You can set commands run at Raspberry startup. Just edit /etc/rc.local file and add some commands.
`sudo nano /etc/rc.local`

- Set volume level (*-c 0 is your sound-card identifier*):

```bash
# Set alsa volume
sleep 30
amixer -c 0 set Playback 88%
```

- Turn off wifi power standby on Rpi 0:

```bash
# Turn off wifi standby on pi0
sudo iwconfig wlan0 power off
```

You can debug the execution of rc.local like this: `journalctl -u rc-local`

## 3rdparty installations

Some 3rdparty tools that your Rhasspy setup may need.

### ReSpeaker

If you have a ReSpeaker 2-Mics Pi HAT or such, install its drivers:

- First, disable Raspberry onboard soundcard:

`sudo nano /boot/config.txt`

Turn **dtparam=audio** parameter to off: `dtparam=audio=off`

<details>
<summary>Then install seeed drivers:</summary>

```bash
sudo apt-get install git
git clone https://github.com/respeaker/seeed-voicecard
cd seeed-voicecard
sudo ./install.sh
sudo reboot
```

</details>

> [seed wiki](http://wiki.seeedstudio.com/Raspberry_Pi/)

### PicoTTS

<details>
<summary>Rpi 4 Buster:</summary>

```bash
wget http://ftp.us.debian.org/debian/pool/non-free/s/svox/libttspico0_1.0+git20130326-9_armhf.deb
wget http://ftp.us.debian.org/debian/pool/non-free/s/svox/libttspico-utils_1.0+git20130326-9_armhf.deb
sudo apt-get install -f ./libttspico0_1.0+git20130326-9_armhf.deb ./libttspico-utils_1.0+git20130326-9_armhf.deb
```

</details>

<details>
<summary>Rpi 0 buster:</summary>

```bash
wget http://archive.raspberrypi.org/debian/pool/main/s/svox/libttspico-utils_1.0+git20130326-3+rpi1_armhf.deb
wget http://archive.raspberrypi.org/debian/pool/main/s/svox/libttspico0_1.0+git20130326-3+rpi1_armhf.deb
sudo apt-get install -f ./libttspico0_1.0+git20130326-3+rpi1_armhf.deb ./libttspico-utils_1.0+git20130326-3+rpi1_armhf.deb
```

</details>

<details>
<summary>Testing:</summary>

```bash
pico2wave -l fr-FR -w test.wav "Bonjour Rhasspy"
aplay test.wav
```

</details>

### MQTT

```bash
sudo apt install -y mosquitto mosquitto-clients
sudo systemctl enable mosquitto.service
```

### Kaldi

Kaldi is a lot better at speech recognition than pocketspinx. But it comes by default with an heavy language model which make it slower.<br />
You can install lighter models from here (get the TDNN-250):<br />
Models: [zamia-speech ASR models](https://github.com/gooofy/zamia-speech#asr-models)<br />
French models: [zamia-speech releases](https://github.com/pguyot/zamia-speech/releases/tag/20190930)

Replace these files in `{profile_dir}/kaldi/model/model` folder and retrain Rhasspy!

> cmvn_opts<br />
> den.fst<br />
> final.mdl<br />
> normalization.fst<br />
> tree<br />

### Docker
*rhasspy can run as a Docker container, which is extremely simple to run without setup!*

- Install Docker:
```
curl -sSL https://get.docker.com | sh
sudo usermod -a -G docker $USER
```
- List running instances: `docker ps`<br />
- Start named rhasspy instance:
```bash
docker run -d -p 12101:12101 \
      --name rhasspy-server \
      --restart unless-stopped \
      -v "$HOME/.config/rhasspy/profiles:/profiles" \
      --device /dev/snd:/dev/snd \
      synesthesiam/rhasspy-server:latest \
      --user-profiles /profiles \
      --profile fr
```
- Start an instance: `docker start rhasspy-server`<br />
- Stop an instance: `docker stop rhasspy-server`<br />
- Update the container: `docker pull synesthesiam/rhasspy-server:latest`<br />
- Remove current container: `docker rm rhasspy-server`

### Virtual environement as a service

If you start rhasspy as venv with an ssh command, it won't live forever, which is what we need for an assistant.

So you have to setup the venv as a service, and activate the service at startup. So you can unplug the pi, plug it and had rhasspy running without any manipulation.

Create the systemd service file:

```bash
sudo nano /etc/systemd/system/rhasspy.service

```

Edit this file with your settings, like --profile manguage, --host IP and --user-profiles path. Then paste in `/etc/systemd/system/rhasspy.service` file.

<details>
<summary>rhasspy.service file</summary>

```bash
[Unit]
Description=Rhasspy
After=syslog.target network.target

[Service]
Type=simple
WorkingDirectory=/home/pi/rhasspy
ExecStart=/bin/bash -lc './run-venv.sh --profile fr --host 192.168.0.140 --user-profiles /home/pi/.config/rhasspy/profiles'

RestartSec=1
Restart=on-failure

StandardOutput=syslog
StandardError=syslog

SyslogIdentifier=rhasspy

[Install]
WantedBy=multi-user.target
```

</details>

Then simply run these to set, enable, then start the service:

```bash
sudo systemctl daemon-reload
sudo systemctl enable rhasspy
sudo systemctl start rhasspy

```

If you need to debug it:

```bash
journalctl -u rhasspy.service

```

## Custom tools

- [HermesLedControl](HermesLedControl)
- [Rhasspy-BatchTester](RhasspyBatchTester)
- [Rhasspy-Logger](RhasspyLogger)
- [Snowboy-CustomMaker](SnowboyCustomMaker)
- [PyJeedom and intent handling with scenarios](JeedomPyHandling)


