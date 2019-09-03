#!/usr/bin/env python3
n = int(input('输入学生数量：'))
data = {}
Subjects = ('Physics', 'Maths', 'History')
for i in range(0, n):
	name = input('输入学生的名字 {}'.format(i + 1))
	marks = []
	for x in Subjects:
		marks.append(int(input('分数：'.format(x))))
	data[name] = marks
for x, y in data.items():
	total = sum(y)
	print('{},你的总分为{}'.format(x, total))
	if total < 120:
		print(x, ':(')
	else:
		print(x,':)')
