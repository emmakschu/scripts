"""
extendDisplay.py

Author: Michael K Schumacher
Github: mkschu

Created:  10/05/2016
Modified: 10/05/2016

This script accepts three user inputs -- normal display resolution,
secondary display resolution, and display output name (EDID), then
calculates the appropriate extended display size, then pass these
arguments to shell commands to adjust display with xrandr, then
start a VNC server with x11vnc. Sudo (or other superuser access)
is required.

Arguments can be passed in the command line while calling the script,
but if none are given, the program will ask for them while running.

"""

import sys
import os

# Pass command line arguments to variables, if given at call
try:
    normalDisplay = sys.argv[1]
    secondDisplay = sys.argv[2]
    outputName = sys.argv[3]

# If command line args not given, get user info with input method
except Exception:
    normalDisplay = input("Normal display resolution (e.g. 1920x1080): ")
    secondDisplay = input("Second display resolution (e.g. 1280x800): ")
    outputName = input("Monitor EDID: ")

# Create arrays for each display, with arr[0] = width, arr[1] = height
normalResolution = normalDisplay.split('x')
secondResolution = secondDisplay.split('x')

# Declare empty array for total resolution to be used
totalResolution = []

# Total width is just the sum of widths, since I'm extending across
totalWidth = int(normalResolution[0]) + int(secondResolution[0])

# Will need max and min heights, as difference will be needed for VNC
maxHeight = max( int(normalResolution[1]), int(secondResolution[1]) )
minHeight = min( int(normalResolution[1]), int(secondResolution[1]) )


# Total height of display is just the larger of the two
totalHeight = maxHeight

# Will need difference as string to pass into shell command
heightDifference = str(maxHeight - minHeight)

# Fill total resolution array with proper width and height as strings
totalResolution.append(str(totalWidth))
totalResolution.append(str(totalHeight))

# Make a single string in "WIDTHxHEIGHT" form to pass into shell commands
totalDisplay = totalResolution[0] + 'x' + totalResolution[1]

# Call the xrandr and x11vnc commands to fix resolution and start VNC server
os.system("sudo xrandr --fb " + totalDisplay + " --output " + outputName
        + " --panning " + totalDisplay + "+0+0/" + totalDisplay + "+0+0")
os.system("sleep 3")
os.system("sudo xrandr --fb " + totalDisplay + " --output " + outputName
        + " --panning " + normalDisplay + "+0+0/" + totalDisplay + "+0+0")
os.system("sudo x11vnc -clip " + secondDisplay + "+" + normalResolution[0]
        + "+" + heightDifference + " -nocursorshape -nocursorpos -ncache 10 &")
