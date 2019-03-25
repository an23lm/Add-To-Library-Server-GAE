class User(object):
	def __init__(self, activation_ts, dev_tokens, latest_activity_ts, last_token_ts, store_front):
		self.activation_ts = activation_ts
		self.dev_tokens = dev_tokens
		self.latest_activity_ts = latest_activity_ts
		self.last_token_ts = last_token_ts
		self.store_front = store_front

	def to_json(self):
		return {
			UserKeys.activation_ts: self.activation_ts,
			UserKeys.dev_tokens: self.assigned_tokens,
			UserKeys.latest_activity_ts: self.latest_activity_ts,
			UserKeys.last_token_ts: self.last_token_ts,
			UserKeys.store_front: self.store_front
			}

class UserKeys:
	activation_ts = u'activation_ts'
	dev_tokens = u'dev_tokens'
	latest_activity_ts = u'latest_activity_ts'
	last_token_ts = u'last_token_ts'
	store_front = u'store_front'

