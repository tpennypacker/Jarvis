from Settings import alarm_settings
import platform

def play():

	if (platform.system() == 'Darwin'):
		print('Good morning! Pretending to play ' + alarm_settings.song)

	elif (platform.system() == 'Linux'):
		from pydub import AudioSegment
		from pydub.playback import play
		song = AudioSegment.from_mp3('Audio\ Files/' + alarm_settings.song)
		play(song)