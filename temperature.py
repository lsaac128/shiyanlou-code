#!/usr/bin/env python3
qishi = 0
print('华氏转摄氏')
while qishi <= 250:
	jieguo = (qishi - 32) / 1.8
	print('{:5d} {:7.2f}'.format(qishi, jieguo))
	qishi += 25

