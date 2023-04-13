# Sustainable Data Documentation

# Initial Setup

The file `[install.sh](http://install.sh)` is a shell script used to install software and packages for the project.

Run the following command to install Wireshark, YABE, python packages, and other dependencies. The command shell shortcut by default is `CTRL + ALT + T` .

`$ sudo install.sh`

# Connecting to Wifi

If you require internet access via Temple’s `tusecurewireless` network, follow these steps:

1. `$ sudo cp {PROJECT_LOCATION}/config/wpa_supplicant.conf /etc/wpa_supplicant/wpa_supplicant.conf`
2. `$ sudo nano /etc/wpa_supplicant/wpa_supplicant.conf`
3. Add your Temple username and password in both the`identity` and `password` field of the `network` section.
4. `$ sudo reboot`

Once the Raspberry Pi is rebooted, it should connect to Temple’s `tusecurewirless` network.

# What is BACpypes?

To read the full documentation, visit this link [https://bacpypes.readthedocs.io/en/latest/](https://bacpypes.readthedocs.io/en/latest/)

BACpypes is a python library that implements the BACnet protocol. It is an extensive library that is capable of creating BACnet applications.

# What is BAC0?

To read the full documentation, visit this link [https://bac0.readthedocs.io/en/latest/](https://bac0.readthedocs.io/en/latest/)

BAC0 is essentially a python scripting application wrapper for BACpypes. BAC0 simplifies desired functionalities of BACnet by providing some basic utility right out of the gate. Everything that BAC0 provides can be done through BACpypes, however BAC0 already provides many simple scripting applications and much more.

sudo apt install libcblas-dev
export APPDATA=
sudo apt install libxkbcommon-dev
sudo apt-get install '^libxcb.*-dev' libx11-xcb-dev libglu1-mesa-dev libxrender-dev libxi-dev libxkbcommon-dev libxkbcommon-x11-dev
