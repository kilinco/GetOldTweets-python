import urllib,urllib2,json,re,datetime,csv
from pyquery import PyQuery
from .. import models
from . import TweetCriteria

class TweetHelper:

	def __init__(self):
		pass

	@staticmethod
	def parseTweet(tweetHTML):
		'''
		param tweetHTML: input
		type: string

		parses the tweet's HTML to tweet model
		'''

		tweetPQ = PyQuery(tweetHTML)
		tweet = models.Tweet()

		usernameTweet = tweetPQ("span:first.username.u-dir b").text()
		txt = re.sub(r"\s+", " ", tweetPQ("p.js-tweet-text").text().replace('# ', '#').replace('@ ', '@'))
		retweets = int(tweetPQ("span.ProfileTweet-action--retweet span.ProfileTweet-actionCount").attr("data-tweet-stat-count").replace(",", ""))
		favorites = int(tweetPQ("span.ProfileTweet-action--favorite span.ProfileTweet-actionCount").attr("data-tweet-stat-count").replace(",", ""))
		dateSec = int(tweetPQ("small.time span.js-short-timestamp").attr("data-time"))
		id = tweetPQ.attr("data-tweet-id")
		permalink = tweetPQ.attr("data-permalink-path")

		geo = ''
		geoSpan = tweetPQ('span.Tweet-geo')
		if len(geoSpan) > 0:
			geo = geoSpan.attr('title')

		tweet.id = id
		tweet.permalink = 'https://twitter.com' + permalink
		tweet.username = usernameTweet
		tweet.text = txt
		tweet.date = datetime.datetime.fromtimestamp(dateSec)
		tweet.retweets = retweets
		tweet.favorites = favorites
		tweet.mentions = " ".join(re.compile('(@\\w*)').findall(tweet.text))
		tweet.hashtags = " ".join(re.compile('(#\\w*)').findall(tweet.text))
		tweet.geo = geo

		return tweet

	@staticmethod
	def getJsonResponse(tweetCriteria, refreshCursor, cookieJar, proxy):
		'''
		param tweetCriteria: input
		type tweetCrtieria: TweetCriteria
		param refreshCursor: positions the cursor
		
		returns JSON response with data from Twitter
		'''
		assert isinstance(tweetCriteria, TweetCriteria) 


		url = "https://twitter.com/i/search/timeline?f=tweets&q=%s&src=typd&max_position=%s"
		
		urlGetData = ''
		
		if hasattr(tweetCriteria, 'username'):
			urlGetData += ' from:' + tweetCriteria.username

		if hasattr(tweetCriteria, 'hashtagSearch'):
			urlGetData += ' ' + tweetCriteria.hashtagSearch
		
		if hasattr(tweetCriteria, 'querySearch'):
			urlGetData += ' ' + tweetCriteria.querySearch
		
		if hasattr(tweetCriteria, 'near'):
			urlGetData += "&near:" + tweetCriteria.near + " within:" + tweetCriteria.within
		
		if hasattr(tweetCriteria, 'since'):
			urlGetData += ' since:' + tweetCriteria.since
			
		if hasattr(tweetCriteria, 'until'):
			urlGetData += ' until:' + tweetCriteria.until
		

		if hasattr(tweetCriteria, 'topTweets'):
			if tweetCriteria.topTweets:
				url = "https://twitter.com/i/search/timeline?q=%s&src=typd&max_position=%s"
			
		
		url = url % (urllib.quote(urlGetData), refreshCursor)

		headers = [
			('Host', "twitter.com"),
			('User-Agent', "Mozilla/5.0 (Windows NT 6.1; Win64; x64)"),
			('Accept', "application/json, text/javascript, */*; q=0.01"),
			('Accept-Language', "de,en-US;q=0.7,en;q=0.3"),
			('X-Requested-With', "XMLHttpRequest"),
			('Referer', url),
			('Connection', "keep-alive")
		]

		if proxy:
			opener = urllib2.build_opener(urllib2.ProxyHandler({'http': proxy, 'https': proxy}), urllib2.HTTPCookieProcessor(cookieJar))
		else:
			opener = urllib2.build_opener(urllib2.HTTPCookieProcessor(cookieJar))
		opener.addheaders = headers

		try:
			response = opener.open(url)
			jsonResponse = response.read()
		except:
			print "Twitter weird response. Try to see on browser: https://twitter.com/search?q=%s&src=typd" % urllib.quote(urlGetData)
			sys.exit()
			return
		
		dataJson = json.loads(jsonResponse)
		
		return dataJson

	# TODO - Will be simplified
	@staticmethod
	def getCSV(tweets, filename):
		'''
		param tweets: input
		type tweets: list of tweets
		param filename: input
		type filename: string
		
		creates a CSV file of tweets
		'''
		assert isinstance(tweets, list)
		assert isinstance(filename, str)
		with open(filename, 'w') as csvfile:
		    fieldnames = ['username', 'text', 'date', 'mentions', 'hashtags', 'geo', 'retweets', 'favorites', 'id', 'permalink']
		    writer = csv.DictWriter(csvfile, fieldnames=fieldnames, delimiter=',', lineterminator='\n')
		    writer.writeheader()
		    print len(tweets)
		    for i in range(len(tweets)):
		        d = {'date':tweets[i].date, 'text':tweets[i].text, 'id':tweets[i].id, 'username':tweets[i].username,'retweets':tweets[i].retweets, 'favorites':tweets[i].favorites,  'mentions':tweets[i].mentions,'hashtags':tweets[i].hashtags, 'geo':tweets[i].geo, 'permalink':tweets[i].permalink}
		        writer.writerow({k:unicode(v).encode('utf-8') for k,v in d.items()})
		        # print '##', i, '## =', d
	
	# TODO - Fixes a tweet object given the raw version
	@staticmethod
	def parseTweets(tweet):
		'''
		param tweet: input
		type tweet: tweet object
		
		returns a tweet object
		'''

		