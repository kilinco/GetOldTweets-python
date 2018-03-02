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