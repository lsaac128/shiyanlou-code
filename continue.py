#!/usr/bin/env python3
while True:
	n = int(input('shuru:'))
	if n < 0:
		continue
	elif n == 0:
		break
	print('pingfang:', n ** 2)
print('Goodbye!')
