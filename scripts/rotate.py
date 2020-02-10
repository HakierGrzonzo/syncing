#!/usr/bin/env python

import subprocess, time

# Get wacom devices ids
command = subprocess.run('xsetwacom --list devices'.split(' '), capture_output=True).stdout.decode('utf-8')
wacomIds = list()
for line in command.strip().split('\n'):
    wacomIds.append(line.strip().split('\t')[1][4:])
assert len(wacomIds) > 0

# get screen and rotation
command = subprocess.run('xrandr -q'.split(' '), capture_output=True).stdout.decode('utf-8')
display = dict()
for line in command.strip().split('\n'):
    line = line.split(' ')
    if 'connected' in line and 'primary' in line:
        display['name'] = line[0]
        rotation = line[4]
        if rotation == 'right':
            display['rotation'] = 'inverted'
            display['wacom'] = 'half'
        elif rotation == 'inverted':
            display['rotation'] = 'left'
            display['wacom'] = 'ccw'
        elif rotation == 'left':
            display['rotation'] = 'normal'
            display['wacom'] = 'none'
        else:
            display['rotation'] = 'right'
            display['wacom'] = 'cw'
        break
assert display != dict()

# rotate the screen 90 degrees
subprocess.run(('xrandr --output ' + display['name'] + ' --rotate ' + display['rotation']).split(' '))
# rotate wacom devices, wait for some other programs to do their stuff
time.sleep(1)
for device in wacomIds:
    subprocess.run(('xsetwacom set ' + device + ' Rotate ' + display['wacom']).split(' '))
