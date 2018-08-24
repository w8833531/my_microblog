#!/usr/bin/env python
# -*- coding: utf-8 -*-
#
# microblog.py
# @Author : 吴鹰 (wuying)
# @Link   : 
# @Date   : 7/19/2018, 2:39:58 PM

from app import create_app, db, cli
from app.models import User, Post

app = create_app()
cli.register(app)

@app.shell_context_processor
def make_shell_context():
    return {'db': db, 'User': User, 'Post': Post}