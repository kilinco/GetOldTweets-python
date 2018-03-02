class TweetCriteria(object):
	'''
	Construct the search query.
	param maxTweets: maximum number of Tweets to be returned
	type maxTweets: int
	param within: search radius using geolocation
	type within: str
	param username: username to be queried
	type username: str
	param since: to query all tweets starting from given date
	type since: str
	param until: to query all tweets until given date
	type until: str
	param querySearch: to query a specific text
	type querySearch: str
	param HashtagSearch: to query a specific hashtag
	type hashtagSearch: str
	param topTweets: to query the last sent tweet
	type topTweets: str
	param near: to set the geolocation of search
	type near: str
	'''
	
	def __init__(self):
		self.maxTweets = 0
		self.within = "15mi"

	def __str__(self):
		strTwitCrit = "Search Query: "
		return  strTwitCrit + str(self.__dict__)
		
	def setUsername(self, username):
		assert isinstance(username, str)
		self.username = username
		return self
		
	def setSince(self, since):
		self.since = since
		return self
	
	def setUntil(self, until):
		self.until = until
		return self
		
	def setQuerySearch(self, querySearch):
		assert isinstance(querySearch, str)
		self.querySearch = querySearch
		return self
	
	def setHashtagSearch(self, hashtagSearch):
		assert isinstance(hashtagSearch, str)
		self.hashtagSearch = hashtagSearch
		return self
		
	def setMaxTweets(self, maxTweets):
		assert isinstance(maxTweets, int)
		self.maxTweets = maxTweets
		return self

	def setTopTweets(self, topTweets):
		self.topTweets = topTweets
		return self
	
	def setNear(self, near):
		assert isinstance(near, str)
		self.near = near
		return self

	def setWithin(self, within):
		assert isinstance(within, str)
		self.within = within
		return self
