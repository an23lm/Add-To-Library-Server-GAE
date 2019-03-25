import requests

def search(term, storefront, devtoken):
	endpoint = 'https://api.music.apple.com/v1/catalog/{storefront}/search'.format(storefront=storefront);
	print(endpoint);
	headers = {"Authorization": "Bearer {0}".format(devtoken)}
	payload = {'term': term, 'types': 'songs'}
	req = requests.get(endpoint, params=payload, headers=headers);
	return req.json()

if __name__=="__main__":
	console.log("running apple_music.py main")
