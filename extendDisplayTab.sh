sudo xrandr --fb 3200x1080 --output eDP1 --panning 3200x1080+0+0/3200x1080+0+0
sleep 3
sudo xrandr --fb 3200x1080 --output eDP1 --panning 1920x1080+0+0/3200x1080+0+0
sudo x11vnc -clip 1280x800+1920+280 -nocursorshape -nocursorpos -ncache 10 &
