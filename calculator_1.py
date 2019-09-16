#!/usr/bin/env python3

import sys
age_1 = []
for i in sys.argv[1:]:
	age_1.append(i.split(':'))
dict_1 = dict(age_1)
for x,y in dict_1.items():
	yjssde = int(y) - 0.165*int(y) - 5000
	if yjssde <= 0:
		gongzi = format(int(y) - 0.165*int(y), '.2f')
		print('{}:{}'.format(x,gongzi))
	elif yjssde > 0 and yjssde <= 3000:
		gongzi = format(int(y) - 0.165*int(y) - yjssde * 0.03, '.2f')
		print('{}:{}'.format(x,gongzi))
	elif yjssde > 3000 and yjssde <= 12000:
		gongzi = format(int(y) - 0.165*int(y) - (yjssde * 0.1 - 210), '.2f')
		print('{}:{}'.format(x,gongzi))
	elif yjssde > 12000 and yjssde <= 25000:
		gongzi = format(int(y) - 0.165*int(y) - (yjssde * 0.2 - 1410), '.2f')
		print('{}:{}'.format(x,gongzi))
	elif yjssde > 25000 and yjssde <= 35000:
		gongzi = format(int(y) - 0.165*int(y) - (yjssde * 0.25 - 2660), '.2f')
		print('{}:{}'.format(x,gongzi))
	elif yjssde > 35000 and yjssde <= 55000:
		gongzi = format(int(y) - 0.165*int(y) - (yjssde * 0.3 - 4410), '.2f')
		print('{}:{}'.format(x,gongzi))
	elif yjssde > 55000 and yjssde <= 80000:
		gongzi = format(int(y) - 0.165*int(y) - (yjssde * 0.35 - 7160), '.2f')
		print('{}:{}'.format(x,gongzi))
	elif yjssde > 80000:
		gongzi = format(int(y) - 0.165*int(y) - (yjssde * 0.45 - 15160), '.2f')
		print('{}:{}'.format(x,gongzi))
