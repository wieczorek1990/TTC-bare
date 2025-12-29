#!/usr/bin/env fish
# Installs dependencies.

cd (status dirname)/../src/
pip3 install -r requirements.txt --break-system-packages -U
