#!/usr/bin/env python
# -*- coding: utf-8 -*-
#
# __init__.py
# @Author : 吴鹰 (wuying)
# @Link   : 
# @Date   : 8/20/2018, 4:29:07 PM
from flask import Blueprint

bp = Blueprint('auth', __name__)
from app.auth import routes