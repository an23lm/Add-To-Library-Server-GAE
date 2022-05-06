#AUTHOR
#https://github.com/pelauimagineering/apple-music-token-generator

import datetime
import jwt


# generate apple music api keys here https://developer.apple.com/account/resources/authkeys/list
secret = ""
keyId = ""
teamId = ""
alg = 'ES256'

headers = {
	"alg": alg,
	"kid": keyId
}

def generate_token(time_now, time_delta_days):
	time_expired = time_now + datetime.timedelta(days=time_delta_days)
	payload = {
		"iss": teamId,
		"exp": int(time_expired.strftime("%s")),
		"iat": int(time_now.strftime("%s"))
	}
	return jwt.encode(payload, secret, algorithm=alg, headers=headers).decode('utf8')

if __name__ == "__main__":
	token = generate_token()

	print("----TOKEN----")
	print(token)
