import requests
import os

os.system('clear')


# username = "Byvmg6eWg7PVgf3Qb5yptBZYsUI6h1q7Znbp4iIg"
# group_id = "Bedroom"
ip = "192.168.1.11"


# url = 'https://' + ip + '/api/' + username + '/groups/' + group_id + '/action'
# response = requests.put(url, data = {'on':False}, verify=False)
# print(response.text)


from phue import Bridge
import logging

logging.basicConfig()
b = Bridge(ip)

b.set_group(1, 'on', False)