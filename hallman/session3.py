#!/usr/bin/env python

import os

class CourseRepo(object):
	def __init__(self, lastname):
		self._lastname = lastname
		self.set_required()

	@property
	def surname(self):
		return self._lastname
	
	@surname.setter
	def surname(self, lastname):
		self._lastname = lastname
		self.set_required()
	
	def set_required(self):
		self.required = [".git",
						"setup.py",
						"README.md", 
						"scripts/getting_data.py", 
						"scripts/check_repo.py", 
						self._lastname + "/__init__.py", 
						self._lastname + "/session3.py"]

	def check(self):
   		for i in self.required:
   			if not os.path.exists(i):
   				return False
   		return True


class Repo_dir(object):

   	def __init__(self, repo):
   		self.original = os.getcwd()
   		self.new = repo
   	
   	def __enter__(self):
	   	try:
	   		os.chdir(self.new)
	   	except OSError:
		   	print 'OSError: Check that path exists'
   	
   	def __exit__(self, type, value, tb):
   		os.chdir(self.original)	



