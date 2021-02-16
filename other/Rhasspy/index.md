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

### ALSA Plugin equal with Docker : The Equalizer

**plugin-equal** is an equalizer plugin for Alsa that allow you to asjust playback tone. Here, it will allow us to adjust TTS voice tone. On portable/bluetooth speakers, fashion is actually on extra bass. This provide a totally unatural sound. Sometimes, the TTS is even hard to understand !

So, here is how to install and set it up to work inside Rhasspy Docker container. I use this solution with a Raspberry Pi4 / Buster / Respeaker 2 mic Pi HAT.

{% include lightbox.html src="../other/Rhasspy/images/rhasspy_equal.jpg" data="interface" title="plugin equal" imgstyle="width:500px;display: block;margin: 0 auto;" %}

Connect to your pi with ssh, and install the plugin:

`sudo apt-get install -y libasound2-plugin-equal`

Checkout your sound cards:

`aplay -l`

You should see your respeaker on card 1. This may differ if you have disabled the default sound card, or if you have another card. Note the card/device number used for output, or its name.

Edit asound.conf:

`sudo nano -c /etc/asound.conf`

And copy, or adapt, the content into. Here I use the name of the card. It could also be hw:1,0

<details>
<summary>asound.conf</summary>

```
pcm.!default {
    type asym
    playback.pcm {
        type plug
        slave.pcm "plugequal"
    }
    capture.pcm {
        type plug
        slave.pcm "hw:seeed2micvoicec"
    }
}

#equalizer:
ctl.equal {
 type equal
}
pcm.plugequal {
 type equal
 slave.pcm "plughw:seeed2micvoicec"
 controls "/home/pi/.alsaequal.bin"
}
pcm.equal {
 type plug
 slave.pcm plugequal
}

```

</details>

Now, reboot the Pi (sudo reboot), and set up the equalizer:

`alsamixer -D equal`

Once you are done, store the settings so they get reloaded at startup:

`sudo alsactl store`

Now, your Pi is ok and will use plugin-equal with your settings ! You can test it with:

`speaker-test -c1 --test=wav -w /usr/share/sounds/alsa/Front_Center.wav`

But, Inside a Docker container, the *system* doesn't have access to all host system files, and here Rhasspy will miss the plugin librairies. So now, we will start Rhasspy Docker container like this:

<details>
<summary>docker run</summary>

```
docker run -d -p 12101:12101 \
	--name rhasspy \
	--restart unless-stopped \
	-v "$HOME/.config/rhasspy/profiles:/profiles" \
	-v "/etc/localtime:/etc/localtime:ro" \
	-v "/etc/asound.conf:/etc/asound.conf" \
	-v "$HOME/.alsaequal.bin:/home/pi/.alsaequal.bin" \
	-v "/usr/lib/arm-linux-gnueabihf/alsa-lib:/usr/lib/arm-linux-gnueabihf/alsa-lib" \
	-v "/usr/lib/ladspa:/usr/lib/ladspa" \
	--device /dev/snd:/dev/snd \
	rhasspy/rhasspy \
	--user-profiles /profiles \
	--profile fr
```

</details>

And if you run it with docker-compose:

<details>
<summary>docker-compose.yml</summary>

```
rhasspy:
    image: "rhasspy/rhasspy"
    container_name: rhasspy
    restart: unless-stopped
    volumes:
        - "$HOME/.config/rhasspy/profiles:/profiles"
        - "/etc/localtime:/etc/localtime:ro"
        - "/etc/asound.conf:/etc/asound.conf:ro"
        - "/usr/lib/arm-linux-gnueabihf/alsa-lib:/usr/lib/arm-linux-gnueabihf/alsa-lib:ro"
        - "/usr/lib/ladspa:/usr/lib/ladspa:ro"
        - type: bind
          source: $HOME/.alsaequal.bin
          target: /home/pi/.alsaequal.bin
          read_only: true
    ports:
        - "12101:12101"
    devices:
        - "/dev/snd:/dev/snd"
    command: --user-profiles /profiles --profile fr
```

</details>

I added four volumes:
- Link to /etc/asound.conf.
- Link to .alsaequal.bin, which is the equalizer settings.
- Links to alsa-lib and ladspa lib used by plugin-equal.

In rhasspy settings, just use aplay with Default Device, and all should work !

### Docker Compose

So now, you may ask how about using Docker-compose ?

Docker-compose allow you to set a docker-compose.yml file with all docker settings into, and just run simple commands.

- Installing:

`sudo pip3 -v install docker-compose`

- Shortcut:

Typing docker-compose cmd everytime can be a bit awkward ... So here you to use dcp instead:

`sudo nano ~/.bashrc`  and add this at the end of the file:
`alias dcp='docker-compose "$@"'`

So now, you can use:

```
dcp build
dcp pull
dcp up -d
dcp down -v
```


## Custom tools

- [HermesLedControl](HermesLedControl)
- [Rhasspy-BatchTester](RhasspyBatchTester)
- [Rhasspy-Logger](RhasspyLogger)
- [PyJeedom and intent handling with scenarios](JeedomPyHandling)


