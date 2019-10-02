# -*- coding:utf-8 -*-

import os
import json
from flask import Flask, render_template

app = Flask(__name__)
app.config['TEMPLATE_AUTO_RELOAD'] = True

@app.route('/')
def index():
    title_list = []
    files_list = os.listdir('/home/shiyanlou/files/')
    for i in files_list:
        lujin = '/home/shiyanlou/files/' + i
        with open(lujin) as f:
            a = f.read()
            b = json.loads(a)
            title_list.append(b['title'])
    return render_template('index.html', title_list=title_list)

@app.route('/files/<filename>')
def file(filename):
    files_contebt = os.listdir('/home/shiyanlou/files')
    lujin2 = '/home/shiyanlou/files/' + filename + '.json'
    try:
        with open(lujin2) as f:
            a = f.read()
            b = json.loads(a)
            content = b['content']
    except FileNotFoundError:
        return render_template('404.html')

    return render_template('file.html', content=content)

@app.errorhandler(404)
def miss(e):
    return render_template('404.html'), 404
