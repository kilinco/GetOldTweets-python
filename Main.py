import sys
assert sys.version_info[0] < 3
from got import manager
import csv

def main():

	tweet_criteria = manager.TweetCriteria()
	tweet_criteria.setQuerySearch("UnitedAirlines").setMaxTweets(100)
	tweets = manager.TweetManager().getTweets(tweet_criteria)
	print str(tweet_criteria)
	for i in range(len(tweets)):
	    #tweets[i] = TweetHelper.parseTweetText(tweets[i])
	    d = {'date':tweets[i].date, 'text':tweets[i].text, 'id':tweets[i].id, 'username':tweets[i].username,'retweets':tweets[i].retweets, 'favorites':tweets[i].favorites, 'mentions':tweets[i].mentions,'hashtags':tweets[i].hashtags, 'geo':tweets[i].geo, 'permalink':tweets[i].permalink}
	    print '##', i+1, '## =', d
	manager.TweetHelper().getCSV(tweets, 'example.csv')


if __name__ == '__main__':
	main()
