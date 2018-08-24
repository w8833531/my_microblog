#!/usr/bin/env python
# -*- coding: utf-8 -*-
#
# __init__.py
# @Author : 吴鹰 (wuying)
# @Link   : 
# @Date   : 8/20/2018, 5:01:04 PM
from flask import Blueprint

bp = Blueprint('main', __name__)

from app.main import routes