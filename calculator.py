#!/usr/bin/env python3

import sys
try:
	yjssde = int(sys.argv[1]) - 5000
	if yjssde <= 3000:
		print(format(yjssde * 0.03, '.2f'))
	elif yjssde > 3000 and yjssde <= 12000:
		print(format(yjssde * 0.1 - 210, '.2f'))
	elif yjssde > 12000 and yjssde <= 25000:
		print(format(yjssde * 0.2 - 1410, '.2f'))
	elif yjssde > 25000 and yjssde <= 35000:
		print(format(yjssde * 0.25 - 2660, '.2f'))
	elif yjssde > 35000 and yjssde <= 55000:
		print(format(yjssde * 0.3 -4410, '.2f'))
	elif yjssde > 55000 and yjssde <= 80000:
		print(format(yjssde * 0.35 - 7160, '.2f'))
	elif yjssde > 80000:
		print(format(yjssde * 0.45 - 15160, '.2f'))
except:
	print('Parameter Error')


