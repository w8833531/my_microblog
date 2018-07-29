#!/usr/bin/env python
# -*- coding: utf-8 -*-
#
# config.py
# @Author : 吴鹰 (wuying)
# @Link   : 
# @Date   : 7/24/2018, 10:23:48 AM

import os
from dotenv import load_dotenv


basedir = os.path.abspath(os.path.dirname(__file__))
load_dotenv(os.path.join(basedir,'.env'))
class Config(object):
    SECRET_KEY = os.getenv('SECRET_KEY') or 'MY_VERY_VERY_HARD_SECRET_KEY'
    SQLALCHEMY_DATABASE_URI = os.getenv('SQLALCHEMY_DATABASE_URL')
    SQLALCHEMY_TRACK_MODIFICATIONS = False