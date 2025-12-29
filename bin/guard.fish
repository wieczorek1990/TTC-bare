#!/usr/bin/env fish
# Runs checks.

cd (status dirname)/../src/
echo 'Guard!' &&
 black ttc/ &&
 echo 'Done.'
