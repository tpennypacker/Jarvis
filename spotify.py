import time
from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager


def playNews():
	url = 'https://accounts.spotify.com/en/login?continue=https:%2F%2Fopen.spotify.com%2Fshow%2F24HhxNTGC8dF4aJ63ofzrT'
	driver = webdriver.Chrome()
	driver.get(url)

	# log in to spotify
	driver.find_element_by_id('login-username').send_keys('trevp@seas.upenn.edu')
	driver.find_element_by_id ('login-password').send_keys('jarvislandry1')
	button = driver.find_element_by_xpath('//button[text()="Log In"]')
	button.click()

	time.sleep(1)
	button = driver.find_element_by_xpath('//button[text()="PLAY"]')
	button.click()