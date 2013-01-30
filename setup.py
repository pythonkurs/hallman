#from distutils.core import setup
from setuptools import setup, find_packages
import sys, os

setup(
	name='hallman',
	#version='0.2',
	author='Jimmie Hallman',
	author_email='johndoe@example.com',
	url='example.com',
	license='GPLv3',
	#packages = find_packages(),
	scripts = ['scripts/getting_data.py'],
	#long_description=open('README.txt').read(),
	)
