#!/usr/bin/env python3
def huiwen(N):
	return N == N[::-1]
if __name__ == '__main__':
	N = input('请输入字符串：')
	if huiwen(N):
		print('这是回文！')
	else:
		print('不，这不是回文！')
