#!/usr/bin/env python
# -*- coding: utf-8 -*-
#
# email.py
# @Author : 吴鹰 (wuying)
# @Link   : 
# @Date   : 8/3/2018, 11:04:33 AM
from threading import Thread
from flask import  current_app
from flask_mail import Message
from app import mail

def send_async_email(app, msg):
    with app.app_context():
        mail.send(msg)

def send_email(subject, sender, recipients, text_body, html_body):
    app = current_app._get_current_object()
    msg = Message(subject, sender=sender, recipients=recipients)
    msg.body = text_body
    msg.html = html_body
    Thread(target=send_async_email, args=(app, msg)).start()