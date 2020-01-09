import os
import requests
import json
import webbrowser
import time
from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager

os.system('clear')

# {
# 	"access_token":"BQBdsO1jqWtw3eDkdfWJMUXKDIM0mRHluIphecDy08G4zGkhP8KBqhod_gPRFOIdM94__8yfBugJ_RefVsVaAyewni3NJSTQilX10HqsfKXEmhTLDMspMxRcpjHfz6TBDKAo_QuIfqsQhZDppZCJdRCnXFs",
# 	"token_type":"Bearer",
# 	"expires_in":3600,
# 	"refresh_token":"AQD2E7kZiB27HiKVFZjz1MMx-EAO9V9lnwHibz2R0MiJZ5rizzfyN53FQR8tuYm_uDupnxnMnLYYWMC9RrRR1FFjktFwXemQgHgExdKHpG8XynJYG5CwN8oVJS7PsQ9ews4",
# 	"scope":""
# }

# user = 'trevorpennypacker'
# token = 'Bearer BQAMSkgc4Mt5exdlIMmDhF-q3FeIHPqvJUjZKD9as0djkE4KcRBQQNJbmDDuc5sWuTzkraztJXWr9YVMeCPMEp_Aa-F4vaOv7wyrcEZW1e_dP_DajjBJUBsYwWBW7Lda8h4JBqDGYskGrYtee4SQy3HkE4A'
# url = 'https://api.spotify.com/v1/shows/24HhxNTGC8dF4aJ63ofzrT/episodes?limit=1'

# headers = {'Authorization':token}
# request = requests.get(url, headers=headers)

# response = request.text
# json = json.loads(response)
# items = json['items'][0]

# print('Description: ' + items['description'] + '\n')
# print('Audio preview url: ' + items['audio_preview_url'] + '\n')
# print('Duration (ms): ' + str(items['duration_ms']) + '\n')
# print('Release date: ' + items['release_date'] + '\n')
# print("Episode URL: " + items['external_urls']['spotify'] + '\n')


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





















