class User(object):
	def __init__(self, user_token, dev_tokens, activation_ts, latest_activity_ts, last_token_ts, store_front):
		self.user_token = user_token
		self.activation_ts = activation_ts
		self.dev_tokens = dev_tokens
		self.latest_activity_ts = latest_activity_ts
		self.last_token_ts = last_token_ts
		self.store_front = store_front

	def to_json(self):
		return {
			UserKeys.user_token: self.user_token,
			UserKeys.activation_ts: self.activation_ts,
			UserKeys.dev_tokens: self.dev_tokens,
			UserKeys.latest_activity_ts: self.latest_activity_ts,
			UserKeys.last_token_ts: self.last_token_ts,
			UserKeys.store_front: self.store_front
			}

class UserKeys:
	user_token = u'user_token'
	activation_ts = u'activation_ts'
	dev_tokens = u'dev_tokens'
	latest_activity_ts = u'latest_activity_ts'
	last_token_ts = u'last_token_ts'
	store_front = u'store_front'

