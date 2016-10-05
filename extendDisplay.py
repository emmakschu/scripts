import sys
import os

try:
    normalDisplay = sys.argv[1]
    secondDisplay = sys.argv[2]
    outputName = sys.argv[3]
    
except Exception:
    normalDisplay = input("Normal display resolution: ")
    secondDisplay = input("Second display resolution: ")
    outputName = input("Monitor EDID: ")

normalResolution = normalDisplay.split('x')
secondResolution = secondDisplay.split('x')

totalResolution = []

totalWidth = int(normalResolution[0]) + int(secondResolution[0])

maxHeight = max( int(normalResolution[1]), int(secondResolution[1]) )
minHeight = min( int(normalResolution[1]), int(secondResolution[1]) )

totalHeight = maxHeight
heightDifference = str(maxHeight - minHeight)


totalResolution.append(str(totalWidth))
totalResolution.append(str(totalHeight))

totalDisplay = totalResolution[0] + 'x' + totalResolution[1]

print(totalDisplay)

os.system("sudo xrandr --fb " + totalDisplay + " --output " + outputName
        + " --panning " + totalDisplay + "+0+0/" + totalDisplay + "+0+0")
os.system("sleep 3")
os.system("sudo xrandr --fb " + totalDisplay + " --output " + outputName
        + " --panning " + normalDisplay + "+0+0/" + totalDisplay + "+0+0")
os.system("sudo x11vnc -clip " + secondDisplay + "+" + normalResolution[0]
        + "+" + heightDifference + " -nocursorshape -nocursorpos -ncache 10 &")
