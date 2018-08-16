#!/usr/bin/env python
# -*- coding: utf-8 -*-
#
# translate.py
# @Author : 吴鹰 (wuying)
# @Link   : 
# @Date   : 8/16/2018, 1:56:02 PM
import hashlib, json, requests, random
from flask_babel import _
from app import app



def translate(text, source_language='', dest_language=''):
    if not app.config['YOUDAO_APPKEY'] or \
            not app.config['YOUDAO_SECRET_KEY']:
        return _('Error: the translation service is not configured.')
    salt = random.randint(1, 65536)
    sign_text = app.config['YOUDAO_APPKEY']+text+str(salt)+app.config['YOUDAO_SECRET_KEY']
    sign = hashlib.md5(sign_text.encode()).hexdigest()
    myurl = 'https://openapi.youdao.com/api?appKey={}&q={}&from={}&to={}&salt={}&sign={}'.format(
        app.config['YOUDAO_APPKEY'], text, source_language, dest_language, salt, sign)
    r = requests.get(myurl)
    if r.status_code != 200:
        return _('Error: the translation service failed.')
    return json.loads(r.content)['translation'][0]