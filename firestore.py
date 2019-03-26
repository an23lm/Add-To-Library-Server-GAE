from google.cloud import firestore
from google.cloud.firestore_v1beta1 import ArrayUnion
from google.cloud import exceptions

import datetime

from user import User, UserKeys
from dev_token import DevToken, DevTokenKeys

db = firestore.Client()

def register_user(user_token, dev_token, storefront):
	doc_ref = db.collection(u'users')
	time_now = datetime.datetime.utcnow()

	try:
		query = doc_ref.where(UserKeys.user_token, '==', user_token)
		user_doc = [doc for doc in query.get()]
		if (len(user_doc) == 0):
			raise exceptions.NotFound('Query returned 0 documents')

		doc_ref.document(user_doc[0].id).update({
			UserKeys.dev_tokens: ArrayUnion([dev_token]),
			UserKeys.latest_activity_ts: time_now,
			UserKeys.last_token_ts: time_now
		})
	except exceptions.NotFound:
		doc_ref.document().set(User(user_token, [dev_token], time_now, time_now, time_now, storefront).to_json())

	return True

def insert_auth_dev_token(dev_token, issue_on, expire_in):
	doc_ref = db.collection(u'dev_token').document()
	doc_ref.set(DevToken(dev_token, None, issue_on, expire_in).to_json())

	return True

def complete_auth_dev_token(dev_token, user_token):
	doc_ref = db.collection(u'dev_token')
	try:
		query = doc_ref.where(DevTokenKeys.dev_token, '==', dev_token)
		token_doc = [doc for doc in query.get()]
		if (len(token_doc) == 0):
			return False
		doc_ref.document(token_doc[0].id).update({
			DevTokenKeys.user_token: user_token
		})
		return True
	except exceptions.NotFound:
		return False

def auth_user(user_token, dev_token):
	doc_ref = db.collection(u'users')
	try:
		query = doc_ref.where(UserKeys.user_token, '==', user_token)
		user_doc = [doc.to_dict() for doc in query.get()]
		if (len(user_doc) == 0):
			return False
		if ((DevTokenKeys.dev_token in user_doc[0]) and dev_token in user_doc[0][DevTokenKeys.dev_token]):
			return True
		return False
	except exceptions.NotFound:
		return False
	return False
