import os

from datetime import datetime
from threading import Timer
import time

import spotify
import lights
import alarm
import weather

os.system('clear')


def startRoutine():
	alarm.play()
	spotify.playNews()
	lights.turnOn()
	weather.show()





# now = datetime.today()
# then = now.replace(hour = alarm_settings.hour, minute = alarm_settings.minute, second = 0, microsecond = 0)

# # if setting an alarm the previous day
# if (now.hour > alarm_settings.hour):
# 	then = then.replace(day = now.day + 1)

# print ('Setting alarm for ' + str(then))
# dt = then - now
# secs = dt.seconds + 1

# timer = Timer(secs, startRoutine)
# timer.start()

startRoutine()
time.sleep(5)
lights.turnOff()