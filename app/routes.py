#!/usr/bin/env python
# -*- coding: utf-8 -*-
#
# routes.py
# @Author : 吴鹰 (wuying)
# @Link   : 
# @Date   : 7/19/2018, 2:31:18 PM
from flask import render_template
from app import app


@app.route('/')
@app.route('/index')
def index():
    user = {'username': 'LarryWu'}
    posts = [
        {
            'author': {'username': 'John'},
            'body': 'Beautiful day in Portland!'
        },
        {
            'author': {'username': 'Susan'},
            'body': 'The Avengers movie was so cool!'
        }
    ]
    return render_template('index.html', user=user, posts=posts)