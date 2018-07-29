#!/usr/bin/env python
# -*- coding: utf-8 -*-
#
# microblog.py
# @Author : 吴鹰 (wuying)
# @Link   : 
# @Date   : 7/19/2018, 2:39:58 PM

from app import app, db
from app.models import User, Post

@app.shell_context_processor
def make_shell_context():
    return {'db': db, 'User': User, 'Post': Post}