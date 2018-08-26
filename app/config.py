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
    POSTS_PER_PAGE = os.getenv('POSTS_PER_PAGE') or 3
    MAIL_DEBUG = os.getenv('MAIL_DEBUG')
    MAIL_SERVER = os.getenv('MAIL_SERVER') or 'localhost'
    MAIL_PORT = os.getenv('MAIL_PORT') or 25
    MAIL_USE_SSL = os.getenv('MAIL_USE_SSL').lower() == 'true'
    MAIL_USE_TSL = os.getenv('MAIL_USE_TSL').lower() == 'true'
    MAIL_USERNAME = os.getenv('MAIL_USERNAME')
    MAIL_PASSWORD = os.getenv('MAIL_PASSWORD')
    MAIL_SENDER = os.getenv('MAIL_SENDER')
    LANGUAGES = ['zh', 'en']

    # YOUDAO translation setting
    YOUDAO_APPKEY = os.getenv('YOUDAO_APPKEY')
    YOUDAO_SECRET_KEY = os.getenv('YOUDAO_SECRET_KEY')

    # elasticsearch setting
    ELASTICSEARCH_URL = os.environ.get('ELASTICSEARCH_URL')