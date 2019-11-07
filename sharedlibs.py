# This file should live in the site-packages folder
# example use of this module:
#
# import sharedlibs
# sharedlibs.add_path_for('myLib')
# from myLib import *

import os
import sys


def get_app_root():
	end = 'Pythonista3/Documents'
	cwd = os.getcwd()
	return cwd.split(end)[0] + end
	
def add_path_for(*modules):
	_libs = _load_libs_dict()
	for module in modules:
		if module in _libs:
			sys.path.append(get_app_root() + _libs[module])
		else:
			raise Exception('No such shared module: .%s' % module)		
		
# Prints a list of accessible libraries
def list():
	_libs = _load_libs_dict()
	print('Available Shared Libraries:')
	for key in _libs:
		print('  %s: %s' % (key, _libs[key]))
		
def _load_libs_dict():
	d = {}
	print(__file__)
	libs_path = '%s/sharedlibs_list.txt' % '/'.join(__file__.split('/')[:-1])
	
	with open(libs_path) as f:
		lines = [l.strip() for l in f.readlines()]
		for line in lines:
			if line != '' and not line.startswith('#'):
				k,v = line.split('=')
				d[k] = v
	return d

				
if __name__ == '__main__':
	list()
