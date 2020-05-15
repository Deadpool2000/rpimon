# rpimon
Enable Monitor mode &amp; Packet Injection in Raspberry Pi

![1589557277389~2](https://user-images.githubusercontent.com/32305505/82069325-c5055580-96f0-11ea-96c6-7e2fedd21ec9.jpg)


## Requirements
Python 3.x

## Installation
1) git clone https://github.com/Deadpool2000/rpimon.git
2) cd rpimon
3) sudo su
4) python3 mon.py

## Info
1) This script install **Re4son** Kernel which enables monitor mode & packet injection in Raspberry Pi.
2) This script works on Raspberry Pi 3B/B+,Raspberry Pi Zero W (**Tested on Raspbian OS**)

## Re4son kernel - [Click Here](https://re4son-kernel.com/re4son-pi-kernel/)

## To check Monitor mode is working
1) After successfull installation,Reboot Pi
2) After rebooting,run '**sudo mon0 up**' command.
3) then run **'sudo airodump-ng wlan0mon'**

## To check Packet Injection is working
1) Run **'sudo aireplay-ng --test wlan0mon'**
2) If you get output '**Injection is working!**' then packet injection is working properly.
