#!/usr/bin/env python

from setuptools import setup, find_packages


setup(
	name='hallman',
	version='0.3',
	author='Jimmie Hallman',
	author_email='johndoe@example.com',
	url='example.com',
	license='GPLv3',
	packages = find_packages(),
	scripts = ['scripts/getting_data.py', 'scripts/check_repo.py'],
	long_description=open('README.txt').read(),
	)
