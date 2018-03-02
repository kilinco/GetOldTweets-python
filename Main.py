import sys
assert sys.version_info[0] < 3
from got import manager
import csv

def main():

	tweet_criteria = manager.TweetCriteria()
	tweet_criteria.setQuerySearch("UnitedAirlines").setMaxTweets(10)
	tweets = manager.TweetManager().getTweets(tweet_criteria)
	print str(tweet_criteria)
	for i in range(len(tweets)):
	    d = {'date':tweets[i].date, 'text':tweets[i].text, 'id':tweets[i].id, 'username':tweets[i].username,'retweets':tweets[i].retweets, 'favorites':tweets[i].favorites, 'mentions':tweets[i].mentions,'hashtags':tweets[i].hashtags, 'geo':tweets[i].geo, 'permalink':tweets[i].permalink}
	    print '##', i+1, '## =', d
	manager.TweetHelper().getCSV(tweets, 'example.csv')

	# tweet_criteria = manager.TweetCriteria().setHashtagSearch("unitedairlines").setSince("2015-09-01").setUntil("2015-09-30").setMaxTweets(100)
	# tweets = manager.TweetManager.getTweets(tweet_criteria)
	# with open('exam.csv', 'w') as csvfile:
	#     fieldnames = ['username', 'text', 'date', 'mentions', 'hashtags', 'geo', 'retweets', 'favorites', 'id', 'permalink']
	#     writer = csv.DictWriter(csvfile, fieldnames=fieldnames, delimiter=',', lineterminator='\n')
	#     writer.writeheader()
	#     print len(tweets)
	#     for i in range(len(tweets)):
	#         d = {'date':tweets[i].date, 'text':tweets[i].text, 'id':tweets[i].id, 'username':tweets[i].username,'retweets':tweets[i].retweets, 'favorites':tweets[i].favorites,  'mentions':tweets[i].mentions,'hashtags':tweets[i].hashtags, 'geo':tweets[i].geo, 'permalink':tweets[i].permalink}
	#         writer.writerow({k:unicode(v).encode('utf-8') for k,v in d.items()})
	#         print '##', i, '## =', d

	# tweet_criteria = manager.TweetCriteria()
	# tweet_criteria.setQuerySearch
	# tweet_gen = manager.TweetGenerator(tweet_criteria, noTweets=5)
 #    while True:
 #        tweets = tweet_gen.next()
 #        print len(tweets)
 #        for i in range(len(tweets)):
 #            d = {'date':tweets[i].date, 'text':tweets[i].text, 'id':tweets[i].id, 'username':tweets[i].username,'retweets':tweets[i].retweets, 'favorites':tweets[i].favorites,  'mentions':tweets[i].mentions,'hashtags':tweets[i].hashtags, 'geo':tweets[i].geo, 'permalink':tweets[i].permalink}
 #            print '##', i, '## =', d

if __name__ == '__main__':
	main()
