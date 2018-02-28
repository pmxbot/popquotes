import re
import operator

import pmxbot.core

import popquotes.pmxbot


def setup_module(request):
	popquotes.pmxbot.install_commands()


def test_bender():
	quote_pattern = re.compile('\(\d+/\d+\): .+')
	res = popquotes.pmxbot.bartletts('bender', 'somenick', '')
	assert res is not None
	assert quote_pattern.match(res)


def test_registered():
	handlers = pmxbot.core.Handler._registry
	all_names = map(operator.attrgetter('name'), handlers)
	assert 'bender' in all_names
