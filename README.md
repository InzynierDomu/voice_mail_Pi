# voice_mail_Pi

![GitHub release (latest SemVer)](https://img.shields.io/github/v/release/InzynierDomu/voice_mail_Pi?style=flat-square)
<a href="https://discord.gg/KmW6mHdg">![Discord](https://img.shields.io/discord/815929748882587688?logo=discord&logoColor=green&style=flat-square)</a>
![GitHub](https://img.shields.io/github/license/InzynierDomu/voice_mail_Pi?style=flat-square)
<a href="https://tipo.live/p/inzynierdomu">![support](https://img.shields.io/badge/support-tipo.live-yellow?style=flat-square)</a>

## Description
The device is used to record voice messages after listening to the greeting. It can be used as a phone for wishes or for taking voice notes.

## Installation
On Raspberry Pi, there'll need an SD with Raspbian. 
It's best to update it.
```
sudo apt-get update
```
An FTP server must be installed.
```
sudo apt-get install proftpd
```
There'll need the pygame library to run the script.
```
pip3 install pygame
```

## Scheme
### Part list
- Raspberry Pi
- USB audio card
- limit switch
- LED
- resistor 200 ohm
- Power bank
- Switch
- Power supply