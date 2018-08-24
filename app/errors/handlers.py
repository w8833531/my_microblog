#!/usr/bin/env python
# -*- coding: utf-8 -*-
#
# error.py.py
# @Author : 吴鹰 (wuying)
# @Link   : 
# @Date   : 7/30/2018, 9:12:47 PM
from flask import render_template
from app import db
from app.errors import bp


@bp.app_errorhandler(404)
def not_found_error(error):
    return render_template('errors/404.html'), 404

@bp.app_errorhandler(500)
def internal_error(error):
    db.session.rollback()
    return render_template('errors/500.html'), 500

