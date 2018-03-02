import datetime

class Tweet(object):
	'''
	Tweet object has all the properties Twitter displays.
	param id: id
	type id: str
	param permalink: link to tweet
	type permalink: str
	param username: username account that wrote the tweet
	type username: str
	param text: text written on the tweet
	type text: str
	param date: date the tweet was published
	type date: datetime
	param retweets: the number of total retweets
	type retweets: int
	param favorites: the number of total favorites
	type favorites: int
	param mentions: mentioned usernames on the tweet
	type mentions: a list of strings
	param hashtags: hashtags on the tweet
	type hashtag: a list of strings
	'''
	
	def __init__(self):
		self.id = ''
		self.permalink = 'https://twitter.com' + ''
		self.username = ''
		self.text = ''
		self.date = datetime.datetime.fromtimestamp(0)
		self.retweets = 0
		self.favorites = 0
		self.mentions = []
		self.hashtags = []


