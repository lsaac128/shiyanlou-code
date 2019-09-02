#!/usr/bin/env python3
N = 10
he = 0
cishu = 0
print('请输入10个数字')
while cishu < 10:
	number = float(input(''))
	he = he + number
	cishu += 1
pjz = he / N
print('{}个数的和是{}'.format(N, he))
print('{}个数的平均数是{:.2f}'.format(N, pjz))

