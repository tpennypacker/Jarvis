from phue import Bridge
import logging

ip = "192.168.1.11"

def turnOff():
	logging.basicConfig()
	b = Bridge(ip)
	b.set_group(1, 'on', False)


def turnOn():
	logging.basicConfig()
	b = Bridge(ip)
	b.set_group(1, 'on', True)


