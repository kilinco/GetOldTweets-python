import json,sys,cookielib
from pyquery import PyQuery
from .. import models
from . import TweetCriteria
from . import TweetHelper


class TweetGenerator(object):
    def __init__(self, noTweets = sys.maxint, tweetCriteria = TweetCriteria()):
    	assert isinstance(tweetCriteria, dict)
      	self.noTweets = noTweets
     	self.tweetCriteria = tweetCriteria
     	self.tweetIter = getTweetsGen(self.tweetCriteria, self.noTweets)
    def __iter__(self):
    	return self.tweetIter
    def __next__(self):
    	return self.tweetIter.next()
    @staticmethod
    def getTweets(tweetCriteria, noTweets, receiveBuffer=None, bufferLength=100, proxy=None):
		'''
		param tweetCriteria: input
		type tweetCriteria: TweetCriteria
		param noTweets: input
		type noTweets: int

		yields tweets that satisfy the criteria	
		'''
		assert isinstance(noTweets, int)
		assert isinstance(tweetCriteria, TweetCriteria)

		refreshCursor = ''
		
		results = []
		resultsAux = []
		cookieJar = cookielib.CookieJar()
		
		if hasattr(tweetCriteria, 'username') and (tweetCriteria.username.startswith("\'") or tweetCriteria.username.startswith("\"")) and (tweetCriteria.username.endswith("\'") or tweetCriteria.username.endswith("\"")):
			tweetCriteria.username = tweetCriteria.username[1:-1]

		active = True

		while active:
			json = TweetHelper.getJsonResponse(tweetCriteria, refreshCursor, cookieJar, proxy)
			if len(json['items_html'].strip()) == 0:
				break

			refreshCursor = json['min_position']
			scrapedTweets = PyQuery(json['items_html'])
			# Remove incomplete tweets withheld by Twitter Guidelines
			scrapedTweets.remove('div.withheld-tweet')
			tweets = scrapedTweets('div.js-stream-tweet')
			
			if len(tweets) == 0:
				break

			while len(results) >= noTweets:
				tmp = results[:noTweets]
				results = results[noTweets:]
				tweetCriteria.maxTweets = tweetCriteria.maxTweets - noTweets
				yield tmp
			
			for tweetHTML in tweets:

				tweet = TweetHelper().parseTweet(tweetHTML)
				
				results.append(tweet)
				resultsAux.append(tweet)
				
				if receiveBuffer and len(resultsAux) >= bufferLength:
					receiveBuffer(resultsAux)
					resultsAux = []
				
				if tweetCriteria.maxTweets > 0 and len(results) >= tweetCriteria.maxTweets:
					active = False
					break
					
		
		if receiveBuffer and len(resultsAux) > 0:
			receiveBuffer(resultsAux)
		
		while len(results) >= noTweets:
			tmp = results[:noTweets]
			results = results[noTweets:]
			tweetCriteria.maxTweets = tweetCriteria.maxTweets - noTweets
			yield tmp
