import re

import pmxbot.botbase

import popquotes.pmxbot

def setup_module(request):
	popquotes.pmxbot.install_commands()

def test_bender():
	quote_pattern = re.compile('\(\d+/\d+\): .+')
	res = popquotes.pmxbot.bartletts('bender', 'somenick', '')
	assert res is not None
	assert quote_pattern.match(res)

def test_registered():
	handlers = pmxbot.botbase._handler_registry
	all_names = [handler[1] for handler in handlers]
	assert 'bender' in all_names

