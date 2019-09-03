#!/usr/bin/env python3
def change():
	global a
	a = 90
	print(a)
a = 9
print('xxxx', a)
print('yyyy', end=' ')
change()
print('iiii', a)
