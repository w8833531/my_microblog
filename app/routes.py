#!/usr/bin/env python
# -*- coding: utf-8 -*-
#
# routes.py
# @Author : 吴鹰 (wuying)
# @Link   : 
# @Date   : 7/19/2018, 2:31:18 PM
from app import app


@app.route('/')
@app.route('/index')
def index():
    return "Hello, World"