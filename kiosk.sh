#!/bin/bash

#xset s noblank	# screen won't blank
#xset s off	#screansaver disabled
xset -dpms	# disables power management

#blanks mouse faster
unclutter -root &

#removes an warnings.
sed -i 's/"exited_cleanly":false/"exited_cleanly":true/' /home/pi/.config/chromium/Default/Preferences
sed -i 's/"exit_type":"Crashed"/"exit_type":"Normal"/' /home/pi/.config/chromium/Default/Preferences

/usr/bin/chromium-browser --noerrdialogs --disable-infobars --kiosk http://cricket.local &



