#!/usr/bin/env python
from setuptools import find_packages
setup_params = dict(
	name='popquotes',
	description="Popular Quotes database",
	use_hg_version=True,
	packages=find_packages(),
	zip_safe=False,
	install_requires=[
		'pmxbot>=1100',
	],
	setup_requires=[
		'hgtools',
	],
	entry_points = dict(
		pmxbot_handlers = [
			'popular_quotes = popquotes.pmxbot:install_commands',
		],
	),
)
if __name__ == '__main__':
	from setuptools import setup
	setup(**setup_params)
