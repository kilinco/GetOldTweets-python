import os
from setuptools import setup

setup(
	name = "GetOldTweets",
	version = "1.0.0",
	author = "Osman Cihan Kilinc",
	author_email = "okilinc@ucsd.edu",
	description = ("Forked from the original https://github.com/Jefferson-Henrique/GetOldTweets-python, GetOldTweets help "
						"to get data from Twitter."),
	license = "MIT",
	keywords = "twitter",
	url = "https://github.com/kilinco/GetOldTweets-python",
	packages = ['got', 'got3'],
	classifiers=[
		"Development status :: 3 - Alpha",
		"Topic :: Utilities",
		"license :: MIT"
	],
	install_requires =["lxml", "pyquery"],
)


