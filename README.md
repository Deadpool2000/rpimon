# rpimon
Enable Monitor mode &amp; Packet Injection in Raspberry Pi.

## Requirements
Python 3.x

## Installation
1) git clone https://github.com/Deadpool2000/rpimon.git
2) cd rpimon0
3) sudo su
4) python3 mon.py

## Info
1) This script install Re4son Kernel in raspbian os.
2) This script works on Raspberry Pi 3B/B+,Raspberry Pi Zero W (Tested on Raspbian OS)

## To check Monitor mode is working
1) After successfull installation (without any error) run 'sudo mon0 up' command.
2) then run 'sudo airodump-ng wlan0mon'

## To check Packet Injection is working
1) Run 'sudo aireplay-ng --test wlan0mon'
if you get output 'Injection is working!' then packet injection is working properly.
