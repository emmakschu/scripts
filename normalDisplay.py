"""
normalDisplay.py

Author: Michael K Schumacher
Github: mkschu

Created:  10/05/2016
Modified: 10/05/2016

This script accepts two user inputs -- normal display resolution
and display output name (EDID), then passes these to shell commands
to kill all x11vnc processes, and call the xrandr command to return
the display resolution to normal. Sudo (or other superuser access)
is required. Meant to be paired with my 'extendDisplay.py' script,
which extends display and starts the VNC server.

Arguments can be passed in the command line while calling the script,
but if they are not given, the program will ask for them while running.

"""

import sys
import os

# Pass the command line arguments to variables, if given at call
try:
    normalResolution = sys.argv[1]
    outputName = sys.argv[2]

# If command line args not given, get info from user with input method
except Exception:
    normalResolution = input("Normal resolution (e.g. 1920x1080): ")
    outputName = input("Monitor EDID: ")

# Get PIDs of x11vnc processes, and kill
os.system("ps -ef | grep x11vnc | grep -v grep | awk '{print $2}' | "
        + "sudo xargs kill")

# Return to normal screen resolution with xrandr
os.system("xrandr --fb " + normalResolution + " --output " + outputName
        + " --panning " + normalResolution + "+0+0/" + normalResolution
        + "+0+0")
