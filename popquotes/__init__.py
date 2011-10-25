"""
Popular Quotes Database
"""

import pkg_resources

from pmxbot.util import SQLiteQuotes

def open():
	db_file = pkg_resources.resource_filename('popquotes', 'popquotes.sqlite')
	return SQLiteQuotes.from_URI('sqlite:' + db_file)
