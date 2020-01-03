import os
import requests

os.system('clear')

# {
# 	"access_token":"BQBdsO1jqWtw3eDkdfWJMUXKDIM0mRHluIphecDy08G4zGkhP8KBqhod_gPRFOIdM94__8yfBugJ_RefVsVaAyewni3NJSTQilX10HqsfKXEmhTLDMspMxRcpjHfz6TBDKAo_QuIfqsQhZDppZCJdRCnXFs",
# 	"token_type":"Bearer",
# 	"expires_in":3600,
# 	"refresh_token":"AQD2E7kZiB27HiKVFZjz1MMx-EAO9V9lnwHibz2R0MiJZ5rizzfyN53FQR8tuYm_uDupnxnMnLYYWMC9RrRR1FFjktFwXemQgHgExdKHpG8XynJYG5CwN8oVJS7PsQ9ews4",
# 	"scope":""
# }

user = 'trevorpennypacker'
token = 'Bearer BQBdsO1jqWtw3eDkdfWJMUXKDIM0mRHluIphecDy08G4zGkhP8KBqhod_gPRFOIdM94__8yfBugJ_RefVsVaAyewni3NJSTQilX10HqsfKXEmhTLDMspMxRcpjHfz6TBDKAo_QuIfqsQhZDppZCJdRCnXFs'
url = 'https://api.spotify.com/v1/shows/24HhxNTGC8dF4aJ63ofzrT/episodes?limit=1'

headers = {'Authorization':token}
request = requests.get(url, headers=headers)

response = request.text
print(response)







# # erase cache and prompt for user permission
# try:
# 	token = util.prompt_for_user_token(username)
# except:
# 	os.remove(f".cache-{username}")
# 	token = util.prompt_for_user_token(username)

# # create our spotify object
# spotify = spotipy.Spotify(auth=token)

# user = spotify.current_user()
# print(json.dumps(user, sort_keys=True, indent=4))