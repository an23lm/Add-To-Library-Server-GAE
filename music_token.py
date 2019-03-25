#AUTHOR
#https://github.com/pelauimagineering/apple-music-token-generator

import datetime
import jwt


secret = """-----BEGIN PRIVATE KEY-----
MIGTAgEAMBMGByqGSM49AgEGCCqGSM49AwEHBHkwdwIBAQQgAjZejuImELFRDFjX
RVp9PfeqWMY5NILZKV2KI6uwWRGgCgYIKoZIzj0DAQehRANCAATvXlIFaLG5WrIc
P4i7s878QBNnBIiItDPOzk1TW0KpSXYJf7zgIcZFi2G5D2r69+z9x2bvsK+aZsDB
Y8mJadSP
-----END PRIVATE KEY-----"""
keyId = "HK8AWCPH65"
teamId = "F698675JBS"
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