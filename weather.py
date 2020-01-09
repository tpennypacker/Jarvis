from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager


def show():
	weather_url = 'https://weather.com/weather/hourbyhour/l/cb8a728d69957a4661df556cddd49c392d66b4bfcb582be3a0fe0dde86af089a'
	driver = webdriver.Chrome()
	driver.get(weather_url)