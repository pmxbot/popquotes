#!/usr/bin/env python
# Generated by jaraco.develop (https://bitbucket.org/jaraco/jaraco.develop)
from setuptools import find_packages
setup_params = dict(
	name='popquotes',
	use_hg_version=True,
	packages=find_packages(),
	namespace_packages=[''],
	zip_safe=False,
	setup_requires=[
		'hgtools',
	],
)
if __name__ == '__main__':
	from setuptools import setup
	setup(**setup_params)
