#!/usr/bin/env python
# -*- coding: utf-8 -*-
#
# error.py.py
# @Author : 吴鹰 (wuying)
# @Link   : 
# @Date   : 7/30/2018, 9:12:47 PM
import os, logging
from flask import render_template
from logging.handlers import RotatingFileHandler
from app import app, db

@app.errorhandler(404)
def not_found_error(error):
    return render_template('404.html'), 404

@app.errorhandler(500)
def internal_error(error):
    db.session.rollback()
    return render_template('500.html'), 500

if not app.debug:
    if not os.path.exists('logs'):
        os.mkdir('logs')
    file_handler = RotatingFileHandler(
        'logs/microbolog.log', maxBytes=10240, backupCount=10,
    )
    file_handler.setFormatter(logging.Formatter(
        '%(asctime)s %(levelname)s: %(message)s [in %(pathname)s:%(lineno)d]'
    ))
    file_handler.setLevel(logging.INFO)
    app.logger.addHandler(file_handler)
    app.logger.setLevel(logging.INFO)
    app.logger.info('Microblog startup')