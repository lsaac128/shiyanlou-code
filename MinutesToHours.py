#!/usr/bin/env python3

import sys



def Hours(a):
	if a < 0:
		raise ValueError('抛出异常')
	else:
		print('{} H, {}M'.format(a // 60, a % 60))

try:
	Hours(int(sys.argv[1]))
except:
	print('Parameter Error')
