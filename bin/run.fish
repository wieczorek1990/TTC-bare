#!/usr/bin/env fish
# Runs the project.

set project 'ttc'
cd (status dirname)/../src/
python3 -m $project
