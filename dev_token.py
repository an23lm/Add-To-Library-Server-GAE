class DevToken(object):
	def __init__(self, dev_token, user_token, issue_on, expire_in):
		self.dev_token = dev_token
		self.user_token = user_token
		self.issue_on = issue_on
		self.expire_in = expire_in

	def to_json(self):
		return {
			DevTokenKeys.user_token: self.user_token,
			DevTokenKeys.issue_on: self.issue_on,
			DevTokenKeys.expire_in: self.expire_in
		}

class DevTokenKeys:
	dev_token = u'dev_token'
	user_token = u'user_token'
	issue_on = u'issue_on'
	expire_in = u'expire_in'