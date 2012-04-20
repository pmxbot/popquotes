"""
Popular Quotes Database
"""

from __future__ import absolute_import

import pkg_resources

import pmxbot.quotes as quotes

def open():
	db_file = pkg_resources.resource_filename('popquotes', 'popquotes.sqlite')
	return quotes.SQLiteQuotes.from_URI('sqlite:' + db_file)
