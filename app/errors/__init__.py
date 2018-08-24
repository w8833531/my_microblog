#!/usr/bin/env python
# -*- coding: utf-8 -*-
#
# __init__.py
# @Author : 吴鹰 (wuying)
# @Link   : 
# @Date   : 8/20/2018, 3:14:21 PM
from flask import Blueprint

bp = Blueprint('errors', __name__)
from app.errors import handlers