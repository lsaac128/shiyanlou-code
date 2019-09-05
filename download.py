#!/usr/bin/env python3
import requests

def download(url):
	try:
		req = requests.get(url)
	except requests.exceptions.MissingSchema:

		print('无效的网址:"{}"'.format(url))
	return
	if req.status_code == 403:
		print('你无权访问此页面！')
		return
	filename = url.split('/')[-1]
	with open(filename, 'w') as fobj:
		fobj.write(req.content.decode('utf-8'))
	print('下载')
if __name__ == '__main__':
	url = input('输入链接：')
	download(url)
