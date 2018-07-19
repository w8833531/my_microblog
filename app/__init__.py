#!/usr/bin/env python
# -*- coding: utf-8 -*-
#
# __init__.py
# @Author : 吴鹰 (wuying)
# @Link   : 
# @Date   : 7/19/2018, 1:47:04 PM


from flask import Flask

app = Flask(__name__)

from app import routes
