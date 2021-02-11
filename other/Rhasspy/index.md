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

### MQTT

```bash
sudo apt install -y mosquitto mosquitto-clients
sudo systemctl enable mosquitto.service
```

For MQTT debugging I would highly recommend portable [MQTT Explorer](http://mqtt-explorer.com/)

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
      --name rhasspy \
      --restart unless-stopped \
      -v "$HOME/.config/rhasspy/profiles:/profiles" \
      -v "/etc/localtime:/etc/localtime:ro" \
      --device /dev/snd:/dev/snd \
      rhasspy/rhasspy \
      --user-profiles /profiles \
      --profile fr
```
- Start an instance: `docker start rhasspy`<br />
- Stop an instance: `docker stop rhasspy`<br />
- Update the container: `docker pull rhasspy/rhasspy:latest`<br />
- Remove current container: `docker rm rhasspy`
- Remove all containers and images: `docker system prune -a`<br />


## Custom tools

- [HermesLedControl](HermesLedControl)
- [Rhasspy-BatchTester](RhasspyBatchTester)
- [Rhasspy-Logger](RhasspyLogger)
- [PyJeedom and intent handling with scenarios](JeedomPyHandling)


