from pydub import AudioSegment
from pydub.playback import play
import os
from Settings import alarm_settings

from datetime import datetime
from threading import Timer

os.system('clear')


def playAlarm():
	print('Good morning! Playing ' + alarm_settings.song)
	song = AudioSegment.from_mp3(alarm_settings.song)
	play(song)


now = datetime.today()
then = now.replace(hour = alarm_settings.hour, minute = alarm_settings.minute, second = 0, microsecond = 0)

# if setting an alarm the previous day
if (now.hour > alarm_settings.hour):
	then = then.replace(day = now.day + 1)


dt = then - now
secs = dt.seconds + 1

timer = Timer(secs, playAlarm)
timer.start()