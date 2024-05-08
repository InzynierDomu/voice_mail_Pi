# voice_mail_Pi

![GitHub release (latest SemVer)](https://img.shields.io/github/v/release/InzynierDomu/voice_mail_Pi?style=flat-square)
<a href="https://discord.gg/KmW6mHdg">![Discord](https://img.shields.io/discord/815929748882587688?logo=discord&logoColor=green&style=flat-square)</a>
![GitHub](https://img.shields.io/github/license/InzynierDomu/voice_mail_Pi?style=flat-square)
<a href="https://tipo.live/p/inzynierdomu">![support](https://img.shields.io/badge/support-tipo.live-yellow?style=flat-square)</a>

## Description
The video with the entire project can be watched on this [video](https://youtu.be/qu0FXGwLReU)

The device is used to record voice messages after listening to the greeting. It can be used as a phone for wishes or for taking voice notes.
![[alt text](https://www.inzynierdomu.pl/wp-content/uploads/2019/12/IMG_6791-scaled.jpg)](https://www.inzynierdomu.pl/wp-content/uploads/2019/12/IMG_6791-scaled.jpg)

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

## Scheme
![alt text](https://github.com/InzynierDomu/voice_mail_Pi/blob/main/pi_voice_mail_schem.jpg)
### Part list
- Raspberry Pi
- USB audio card
- limit switch
- LED
- resistor 200 ohm (for LED)
- Power bank
- Switch
- Power supply

![[alt text](https://github.com/InzynierDomu/voice_mail_Pi/blob/main/pi_voice_mail_schem.jpg)](https://www.inzynierdomu.pl/wp-content/uploads/2019/12/IMG_6783-scaled.jpg)

## Configuration & using
Before using check audio device:
- with command 
  ```arecord -l```
check audio card number and subdevice number.
- If it's needed change line 42 "plughw:1,0"
- Default it's card 1 and subdevice 0.
TBD automate finding audio card.

To easily modify greeting files and download recordings, it's recommended to use FTP (File Transfer Protocol).
- Install the FTP server on your Raspberry Pi using the following command:
```sudo apt-get install proftpd```
- Download and install the FTP client such as Filezilla on your computer.
- Connect to your Raspberry Pi using an FTP client. You'll need the IP address of your Raspberry Pi, along with the username and password.

On default timeout for record is 3 min. It's hard coded in line 42 main script -duration. TBD make separate configuration file.

After picking up the handset (limit switch), greeting will be played, then the green LED will light up and recording will start. 
After hanging up the handset (limit switch) or timeout, the recording will be saved using the date and time.
