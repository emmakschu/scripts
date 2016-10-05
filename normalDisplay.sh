#
# This script finds any PIDs associated with x11vnc (except the grep
# search itself), and kills them. Then it sets the output on eDP1 to
# 1920x1080 resolution
#

ps -ef | grep x11vnc | grep -v grep | awk '{print $2}' | sudo xargs kill
xrandr --fb 1920x1080 --output eDP1 --panning 1920x1080+0+0/1920x1080+0+0