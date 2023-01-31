#!/usr/bin/python
# -*- coding: UTF-8 -*-
import requests
import smtplib
from email.mime.text import MIMEText
from email.header import Header
message = MIMEText('plain', 'utf-8')
subject = requests.get("http://6.ipw.cn").text
message['Subject'] = Header(subject, 'utf-8')
try:
    smtpObj = smtplib.SMTP() 
    smtpObj.connect("smtp.qq.com", 25)    # 25 为 SMTP 端口号
    smtpObj.login("sender@sender.com","password")  
    smtpObj.sendmail("sender@qq.com", "receivers@ccedu.top", message.as_string())
    print ("邮件发送成功")
except smtplib.SMTPException:
    print ("Error: 无法发送邮件")
