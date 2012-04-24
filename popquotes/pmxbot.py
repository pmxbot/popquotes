from __future__ import absolute_import

import itertools

from pmxbot.botbase import command

import popquotes

def bartletts(lib, nick, qsearch):
	qs = popquotes.open()
	qs.lib = lib
	qsearch = qsearch.strip()
	if nick == 'pmxbot':
		qt, i, n = qs.quoteLookup()
		if not qt: return
		if qt.find(':', 0, 15) > -1:
			qt = qt.split(':', 1)[1].strip()
	else:
		qt, i, n = qs.quoteLookupWNum(qsearch)
		if not qt: return
		qt = u'(%s/%s): %s' % (i, n, qt)
	return qt

# declare all of the popquotes commands
quote_libs = (
	# name, aliases, doc, lib
	('bender', ('bend',), 'Quote Bender, a la http://en.wikiquote.org/wiki/Futurama', 'bender'),
	('zoidberg', ('zoid',), 'Quote Zoidberg, a la http://en.wikiquote.org/wiki/Futurama', 'zoid'),
	('simpsons', ('simp',), 'Quote the Simpsons, a la http://snpp.com/', 'simpsons'),
	('hal', ('2001',), 'HAL 9000', 'hal'),
	('grail', (), 'I questing baby', 'grail'),
	('anchorman', (), 'Quote Anchorman.', 'anchorman'),
	('hangover', (), 'Quote hangover.', 'hangover'),
	('R', ('r',), 'Quote the R mailing list', 'R'),
)

# create the popquotes commands per the declarations above
def make_command(name, aliases, doc, lib):
	# create a command function with the pmxbot command signature
	cmd_func = lambda client, event, channel, nick, rest: bartletts(lib, nick, rest)
	# register the new func as a command
	pmxbot_cmd = command(name, aliases=aliases, doc=doc)(cmd_func)
	# add the command to the global namespace so it can be tested
	globals()[name] = pmxbot_cmd

def install_commands():
	list(itertools.starmap(make_command, quote_libs))
