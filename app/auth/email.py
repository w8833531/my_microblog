#!/usr/bin/env python
# -*- coding: utf-8 -*-
#
# email.py
# @Author : 吴鹰 (wuying)
# @Link   : 
# @Date   : 8/3/2018, 11:04:33 AM
from flask import render_template, current_app
from app.email import send_email
from flask_babel import _


def send_password_reset_email(user):
    token = user.get_reset_password_token()
    send_email(_('[Microblog] Reset Your Password'),
                sender=current_app.config['MAIL_SENDER'],
                recipients=[user.email],
                text_body=render_template('email/reset_password.txt',
                                            user=user,token=token),
                html_body=render_template('email/reset_password.html',
                                            user=user,token=token))