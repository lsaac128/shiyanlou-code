#!/usr/bin/env python3
print('欢迎使用余额宝收益计算器')
jinge = float(input('请输入本金:'))
lilv = float(input('请输入年化利率:'))
qishu = float(input('请输入天数:'))
benli = 0
xunhuan = 1
while xunhuan <= qishu:
	benli = jinge + jinge * lilv * (qishu/365) 
	print('第{}天, {:.2f}'.format(xunhuan, benli))
	jinge = benli
	xunhuan += 1
