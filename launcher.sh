#!/bin/sh
# launcher.sh
# navigate to home directory, then to this directory, then execute python script, then back home


cd /
cd  home/pi/mqtt_epics_python_bridge
sudo python mqtt_epics.py
cd /
