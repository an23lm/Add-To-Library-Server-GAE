from google.cloud import firestore
import datetime

from user import User, UserKeys
from dev_token import DevToken, DevTokenKeys

db = firestore.Client()

def register_user(user_token, dev_token, store_front):
	doc_ref = db.collection(u'users').document(user_token)
	is_user_exist = doc_ref.get().exists()
	time_now = datetime.datetime.utcnow()

	if (is_user_exist == False):
		doc_ref.set(User(time_now, [dev_token], time_now, time_now, store_front).to_json())
	else:
		doc_ref.update({
			UserKeys.dev_tokens: ArrayUnion([dev_token]),
			UserKeys.latest_activity_ts: time_now,
			UserKeys.last_token_ts: time_now
		})

	return True

def insert_auth_dev_token(dev_token, issue_on, expire_in):
	doc_ref = db.collection(u'dev_token').document(dev_token)
	doc_ref.set(DevToken(dev_token, None, issue_on, expire_in).to_json())

	return True

def complete_auth_dev_token(dev_token, user_token):
	doc_ref = db.collection(u'dev_token').document(dev_token)
	if (doc_ref.get().exists()):
		doc_ref.update({DevTokenKeys.user_token: user_token})
		return True
	else:
		return False

def auth_user(user_token, dev_token):
	doc_ref = db.collection(u'users').document(user_token)
	user_doc = doc.ref.get()
	if (doc.ref.get().exists() and DevTokenKeys.user_token in user_doc and user_doc[DevTokenKeys.user_token] == user_token):
		return True
	return False
