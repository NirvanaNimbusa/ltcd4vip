# coding=utf-8
'comment'
from flask import render_template

from bootstrap_init import app

__author__ = 'Jiateng Liang'


@app.route('/leetcode/<type>')
def main(type):
    return render_template('index.html')
