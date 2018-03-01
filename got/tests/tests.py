# from collections import Iterator, Generator
# import unittest
# from unittest.mock import MagicMock
import csv

# import unittest

# # Here's our "unit".
# def IsOdd(n):
#     return n % 2 == 1

# # Here's our "unit tests".
# class IsOddTests(unittest.TestCase):

#     def testOne(self):
#         self.failUnless(IsOdd(1))

#     def testTwo(self):
#         self.failIf(IsOdd(2))

# def main():
#     unittest.main()

# if __name__ == '__main__':
#     main()


tweet_criteria = manager.TweetCriteria()
tweet_criteria.setQuerySearch("UnitedAirlines").setMaxTweets(5)
print tweet_criteria.querySearch
tweets = manager.TweetManager().getTweets(tweet_criteria)
for i in range(len(tweets)):
    #tweets[i] = TweetHelper.parseTweetText(tweets[i])
    d = {'date':tweets[i].date, 'text':tweets[i].text, 'id':tweets[i].id, 'username':tweets[i].username,'retweets':tweets[i].retweets, 'favorites':tweets[i].favorites, 'mentions':tweets[i].mentions,'hashtags':tweets[i].hashtags, 'geo':tweets[i].geo, 'permalink':tweets[i].permalink}
    print '##', i, '## =', d



# with open('exam.csv', 'w') as csvfile:
#     fieldnames = ['username', 'text', 'date', 'mentions', 'hashtags', 'geo', 'retweets', 'favorites', 'id', 'permalink']
#     writer = csv.DictWriter(csvfile, fieldnames=fieldnames, delimiter=',', lineterminator='\n')
#     writer.writeheader()
#     print len(tweets)
#     for i in range(len(tweets)):
#         d = {'date':tweets[i].date, 'text':tweets[i].text, 'id':tweets[i].id, 'username':tweets[i].username,'retweets':tweets[i].retweets, 'favorites':tweets[i].favorites,  'mentions':tweets[i].mentions,'hashtags':tweets[i].hashtags, 'geo':tweets[i].geo, 'permalink':tweets[i].permalink}
#         writer.writerow({k:unicode(v).encode('utf-8') for k,v in d.items()})
#         print '##', i, '## =', d

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

# tweet_gen = got.manager.TweetGenerator(tweet_criteria, noTweets=5)
# with open('exam.csv', 'w') as csvfile:
#     fieldnames = ['username', 'text', 'date', 'mentions', 'hashtags', 'geo', 'retweets', 'favorites', 'id', 'permalink']
#     writer = csv.DictWriter(csvfile, fieldnames=fieldnames, delimiter=',', lineterminator='\n')
#     writer.writeheader()
#     while True:
#         tweets = tweet_gen.next()
#         print len(tweets)
#         for i in range(len(tweets)):
#             d = {'date':tweets[i].date, 'text':tweets[i].text, 'id':tweets[i].id, 'username':tweets[i].username,'retweets':tweets[i].retweets, 'favorites':tweets[i].favorites,  'mentions':tweets[i].mentions,'hashtags':tweets[i].hashtags, 'geo':tweets[i].geo, 'permalink':tweets[i].permalink}
#             writer.writerow({k:unicode(v).encode('utf-8') for k,v in d.items()})
#             print '##', i, '## =', d

# class Test(unittest.TestCase):
#     def test_tweetGenerator(self):
#         f = tweetGenerator(10, )
#         self.assertEqual(next(f), 0)
#         self.assertEqual(next(f), 1)
#         self.assertEqual(next(f), 1)
#         self.assertEqual(next(f), 2) #etc...
#     def test_tweetGenerator_is_iterator(self):
#         f = tweetGenerator()
#         self.assertIsInstance(f, Iterator)
#     def test_tweetGenerator_is_generator(self):
#         f = tweetGenerator()
#         self.assertIsInstance(f, Generator)