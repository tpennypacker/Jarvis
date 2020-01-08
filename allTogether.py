from pydub import AudioSegment
from pydub.playback import play
import os
from Settings import alarm_settings

from datetime import datetime
from threading import Timer
import time

import webbrowser
from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager

os.system('clear')


def playAlarm():
	print('Good morning! Playing ' + alarm_settings.song)
	# song = AudioSegment.from_mp3(alarm_settings.song)
	# play(song)
	time.sleep(3)
	playSpotify()


def playSpotify():
	# open to login / redirect page
	url = 'https://accounts.spotify.com/en/login?continue=https:%2F%2Fopen.spotify.com%2Fshow%2F24HhxNTGC8dF4aJ63ofzrT'
	driver = webdriver.Chrome()
	driver.get(url)

	# log in to spotify
	driver.find_element_by_id('login-username').send_keys('trevp@seas.upenn.edu')
	driver.find_element_by_id ('login-password').send_keys('jarvislandry')
	button = driver.find_element_by_xpath('//button[text()="Log In"]')
	button.click()

	time.sleep(1)
	button = driver.find_element_by_xpath('//button[text()="PLAY"]')
	button.click()
	time.sleep(1000)




now = datetime.today()
then = now.replace(hour = alarm_settings.hour, minute = alarm_settings.minute, second = 0, microsecond = 0)

# if setting an alarm the previous day
if (now.hour > alarm_settings.hour):
	then = then.replace(day = now.day + 1)

print ('Setting alarm for ' + str(then))
dt = then - now
secs = dt.seconds + 1

timer = Timer(secs, playAlarm)
timer.start()