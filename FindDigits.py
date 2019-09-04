#!/usr/bin/env python3
with open('/tmp/String.txt') as fobj:
	a = []
	for i in fobj.read():
		if i.isdigit():
			a.append(i)
	print(''.join(a))

