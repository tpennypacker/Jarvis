# Jarvis

SETUP
1. Verify spotify in browser using spotify client id
	https://accounts.spotify.com/authorize?client_id=9d056bf9f7b14a2e9f96b97392e066b7&response_type=code&redirect_uri=http%3A%2F%2Fgoogle.com%2F

2. Copy code from redirect url

3. Encode clientId:clientSecret in base64 (www.base64encode.org)

3. curl -H "Authorization: Basic OWQwNTZiZjlmN2IxNGEyZTlmOTZiOTczOTJlMDY2Yjc6ZDNhM2EyMGRjNmQ0NDUxNzg5YjE4MjU1NzczZGZiNDc=" -d grant_type=authorization_code -d code=AQAT2xRB_dd-l6eOs-ctmZb_42g7g0HWR4bMMQIek8xXhGhdsy2JTMveuPuQT1ChuAhx5q8Zr9-gguCn_FEH_9M7pxClznG3cAdALm_7r5YTnlF0WCqKM0UYf-_9pqfqvHB39iJ615-tBFe89r6QMn9ohDMTFeCGR4Dl3F8SCqc2-PHZqrq7kw -d redirect_uri=http%3A%2F%2Fgoogle.com%2F https://accounts.spotify.com/api/token