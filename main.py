from flask import Flask, request, render_template, jsonify
import datetime

import music_token
import apple_music
import firestore

app = Flask(__name__)

@app.route('/')
def hello():
    return 'Hey there! You seem lost.🧐 Check out \'Add To Library\' on the Chrome Webstore.'

# @app.route('/admin/gentoken')
# def generate_token():
# 	if request.headers.get('X-Appengine-Cron') == True:
# 		token = music_token.generate_token(30)
# 		with open("jwt_token", "w") as file:
# 			file.write(token)
# 			return "New token generated successfully"
# 	return "Okay bro, calm down."

@app.route('/auth')
def auth():
	time_now = datetime.datetime.utcnow()
	expire_in = 30

	dev_token = music_token.generate_token(time_now, expire_in)
	firestore.insert_auth_dev_token(dev_token, time_now, expire_in)

	cookie_expire_time = time_now + datetime.timedelta(days=expire_in)
	cookie_expire_time_string = cookie_expire_time.strftime("%a, %d %b %Y %H %M %S") + ' GMT'

	print('cookie_expire_time: ' + cookie_expire_time_string)

	jt = {'jtok': dev_token, 'dev_token_exp': cookie_expire_time_string}
	return render_template('auth.html', jtok=jt, auth='true')

# Unauth user with Apple Music
@app.route('/unauth')
def unauth():
	usertoken = request.headers.get('usertoken')
	storefront = request.headers.get('applestorefront')
	devtoken = request.headers.get('developertoken')

	jt = {"jtok": devtoken}
	return render_template('auth.html', jtok=jt, auth='false')
	

# @app.route('/search', methods=['GET', 'POST'])
# def search():
# 	usertoken = request.headers.get('Music-User-Token')
# 	storefront = request.headers.get('Apple-Storefront')
# 	term = request.form.get('term')
# 	devtoken = music_token.generate_token()
# 	if (usertoken != None and storefront != None and term != None and devtoken != None):
# 		search_res = apple_music.search(term, storefront, devtoken)
# 		return jsonify({'SUCCESS': 'true', 'response': search_res})
# 	else:
# 		return jsonify({'SUCCESS': 'false'})


if __name__ == '__main__':
    app.run(host='127.0.0.1', port=8080, debug=True)
