#!/usr/bin/env python
from setuptools import find_packages
setup_params = dict(
	name='popquotes',
	url="https://bitbucket.org/yougov/popquotes",
	author="YouGov, plc.",
	author_email="you",
	description="Popular Quotes database",
	use_hg_version=True,
	packages=find_packages(),
	include_package_data=True,
	zip_safe=False,
	install_requires=[
		'pmxbot>=1101.3dev',
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
