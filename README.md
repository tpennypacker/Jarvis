# Jarvis

SETUP
1. Verify spotify in browser using spotify client id
	https://accounts.spotify.com/authorize?client_id=9d056bf9f7b14a2e9f96b97392e066b7&response_type=code&redirect_uri=http%3A%2F%2Fgoogle.com%2F

2. Copy code from redirect url

3. Encode clientId:clientSecret in base64 (www.base64encode.org)

3. curl -H "Authorization: Basic OWQwNTZiZjlmN2IxNGEyZTlmOTZiOTczOTJlMDY2Yjc6ZDNhM2EyMGRjNmQ0NDUxNzg5YjE4MjU1NzczZGZiNDc=" -d grant_type=authorization_code -d code=AQBN6zrapu6RgjLajgM3m0all--o5bQ7_KbZmvOv1Qu4OQXigFCvqkpaq9Zsmis7ZyoAcov73-tDrkfWopBJ0smEy8c499-5s_dMLnUDm739UiUhdB-hdyHmWcpzCM0qyTRUHJb7g6rcOIsB_Lo8m6s7p6yS4ouEqA2-fKiZ4V5WMK0Y1Js9qQ -d redirect_uri=http%3A%2F%2Fgoogle.com%2F https://accounts.spotify.com/api/token

4. Copy access token and include it in any requests. Also save the refresh token.

NOTE: the access token will expire after one hour. After that, a refresh token must be used.
https://developer.spotify.com/documentation/general/guides/authorization-guide/





# refresh token
AQCEhl96zWumqgxBPIP4jVlWmBDIiN4jNDVWA3sF9A5ntjePDAHw9v1BghvkyK3dkjfCgZf9b2cKZxj8hs1bngUtR