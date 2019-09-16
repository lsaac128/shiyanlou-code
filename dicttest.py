#!/usr/bin/env python3

import sys

output_dict = {}

def handle_date(arg):
	a = arg.split(':')
	output_dict[a[0]] = a[1]

def print_date(a, b):
	print('ID:{} Name:{}'.format(a, b))

if __name__ == '__main__':
	
	for arg in sys.argv[1:]:
		handle_date(arg)

	for key in output_dict:
		print_date(key, output_dict[key])
