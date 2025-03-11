# voice_mail_Pi

![GitHub release (latest SemVer)](https://img.shields.io/github/v/release/InzynierDomu/voice_mail_Pi?style=flat-square)
<a href="https://discord.gg/KmW6mHdg">![Discord](https://img.shields.io/discord/815929748882587688?logo=discord&logoColor=green&style=flat-square)</a>
![GitHub](https://img.shields.io/github/license/InzynierDomu/voice_mail_Pi?style=flat-square)
<a href="https://tipo.live/p/inzynierdomu">![support](https://img.shields.io/badge/support-tipo.live-yellow?style=flat-square)</a>

## Description
📖 <a href="https://www.inzynierdomu.pl/gadzet-weselny-z-raspberry-pi/">note about project (PL)</a>
📽️ <a href="https://youtu.be/qu0FXGwLReU">short video with project (PL)</a>

The device is used to record voice messages after listening to the greeting. It can be used as a phone for wishes or for taking voice notes.
![[alt text](https://www.inzynierdomu.pl/wp-content/uploads/2019/12/IMG_6791-scaled.jpg)](https://www.inzynierdomu.pl/wp-content/uploads/2019/12/IMG_6791-scaled.jpg)

<div align="center">
<h2>Support</h2>

<p>If any of my projects have helped you in your work, studies, or simply made your day better, you can buy me a coffee. <a href="https://buycoffee.to/inzynier-domu" target="_blank"><img src="https://buycoffee.to/img/share-button-primary.png" style="width: 195px; height: 51px" alt="Postaw mi kawę na buycoffee.to"></a></p>
</div>

## Installation
On Raspberry Pi, there'll need an SD with Raspbian. 
It's best to update it.
```
sudo apt-get update
```
There'll need the pygame library to run the script.
```
pip3 install pygame
```
### Adding to Autostart
To automatically start the project upon boot, follow these steps:
- Edit the autostart file by running the following command:
```
sudo nano /etc/xdg/lxsession/LXDE-pi/autostart
```
- Add the following line to the end of the file, replacing <path to main.py script> with the actual path to your main.py script:
```
@/usr/bin/python <path to main.py script>
```
For example:
```
@/usr/bin/python /home/pi/voice_mail_Pi/main.py
```
- Save the file and reboot, the script will start automatically upon booting up the Raspberry Pi

## Scheme
### Part list
- Raspberry Pi
- USB audio card
- limit switch
- LED
- resistor 200 ohm (for LED)
- Power bank
- Switch
- Power supply
![alt text](https://github.com/InzynierDomu/voice_mail_Pi/blob/main/pi_voice_mail_schem.jpg)
Connect the sound card with a microphone and speaker to USB. Power the Raspberry from a power bank via an additional switch.
![[alt text](https://github.com/InzynierDomu/voice_mail_Pi/blob/main/pi_voice_mail_schem.jpg)](https://www.inzynierdomu.pl/wp-content/uploads/2019/12/IMG_6783-scaled.jpg)

## Configuration & using
Before using check audio device:
- with command 
  ```arecord -l```

To easily modify greeting files and download recordings, it's recommended to use FTP (File Transfer Protocol).
- Install the FTP server on your Raspberry Pi using the following command:
```sudo apt-get install proftpd```
- Download and install the FTP client such as Filezilla on your computer.
- Connect to your Raspberry Pi using an FTP client. You'll need the IP address of your Raspberry Pi, along with the username and password.

After picking up the handset (limit switch), greeting will be played, then the green LED will light up and recording will start. 
After hanging up the handset (limit switch) or timeout, the recording will be saved using the date and time.
