from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager
import time
import os

os.system('clear')

# # open to login / redirect page
# url = 'https://accounts.spotify.com/en/login?continue=https:%2F%2Fopen.spotify.com%2Fshow%2F24HhxNTGC8dF4aJ63ofzrT'
# driver = webdriver.Chrome()
# driver.get(url)

# # log in to spotify
# driver.find_element_by_id('login-username').send_keys('trevp@seas.upenn.edu')
# driver.find_element_by_id ('login-password').send_keys('jarvislandry')
# button = driver.find_element_by_xpath('//button[text()="Log In"]')
# button.click()

# time.sleep(1)
# button = driver.find_element_by_xpath('//button[text()="PLAY"]')
# button.click()



# weather_url = 'https://weather.com/weather/hourbyhour/l/cb8a728d69957a4661df556cddd49c392d66b4bfcb582be3a0fe0dde86af089a'
# driver = webdriver.Chrome()
# driver.get(weather_url)

calendar_url = 'https://calendar.google.com'
driver = webdriver.Chrome()
driver.get(calendar_url)

time.sleep(1)

driver.find_element_by_id('identifierId').send_keys('trevor.pennypacker@gmail.com')
button = driver.find_element_by_xpath('//*[@id="identifierNext"]/span/span')
button.click()

time.sleep(1)

driver.find_element_by_name('password').send_keys('tmoose11')
button = driver.find_element_by_xpath('//*[@id="passwordNext"]/span/span')
button.click()

