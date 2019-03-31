#!/bin/bash/
echo "##############################################################################"
echo "           Monitor mode for Raspberry Pi 3 B/B+,Zero W On Raspbian OS         "
echo "##############################################################################"
echo
# Upadating
sudo apt-get update
sudo apt-get install tar wget -y

# Installing Re4son kernel in Raspbian
sudo su
cd /usr/local/src

# Downloading tar
wget -O re4son-kernel_current.tar.xz https://re4son-kernel.com/download/re4son-kernel-current/

# Extracting
tar -xJf re4son-kernel_current.tar.xz
echo
echo "##############################################################################"
echo "           Now take a cup of tea until complete installation :)               "
echo "##############################################################################"
echo
# Installation
cd re4son-kernel_4*
./install.sh
echo "##############################################################################"
echo "          Succeed! Now start monitor mode by typing 'sudo mon0 up'            "
echo "##############################################################################"
echo
echo "If you found any error in this installation,update & upgrade your system and try again!"
echo
echo "################################################################################"
echo "                          Script By:Deadpool007                                 "
echo "                 Subscribe my YouTube Channel : Deadpool2000                    "
echo "################################################################################" 

