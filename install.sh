#!/bin/sh

# Installing wireshark
sudo apt install wireshark
chmod +x /usr/bin/dumpcap
sudo dpkg-reconfigure wireshark-common

# Installing BAC0 and bacpypes
pip install -r requirements.txt

# Installing yabe
sudo apt install mono-complete

# Installing project repo
git clone 