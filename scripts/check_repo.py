#!/usr/bin/env python

from hallman.session3 import CourseRepo, Repo_dir
import argparse

parser = argparse.ArgumentParser()
parser.add_argument('repo', help='Path to check')
arg = parser.parse_args()
lastname = arg.repo.split('/')[-1]

with Repo_dir(arg.repo):
	path = CourseRepo(lastname)
	if path.check():
		print 'PASS'
	else:
		print 'FAIL'
	
