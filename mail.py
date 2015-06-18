#!/usr/bin/python
#-*- coding: utf-8 -*-

import smtplib,os
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText
from email.header import Header
import sys
reload(sys)
sys.setdefaultencoding('utf8') 

def smail(result,environment):
    sender='qa-pub@funshion.com'
    receiver=['gaoshan@funshion.com','yangss@funshion.com','liangll@funshion.com','yangjiao@funshion.com','niuxy@funshion.com','maojy@funshion.com']
    #receiver=['maojy@funshion.com']
 
    if environment == 'pro':
        title=u'zeus接口公网环境测试'
    if environment == 'alpha':
        title=u'zeus接口alpha环境测试'
    if environment == '212':
        title=u'zeus接口212环境测试'
    #title='zeus公网接口测试'.decode("gbk", 'ignore').encode("utf-8")
    username='qa-pub@funshion.com'
    password='nihao123$'
    msg = MIMEMultipart('alternatvie')
    html = open(result).read()
    html_att = MIMEText(html, 'html','utf-8')
    msg.attach(html_att)
    msg['from'] = sender
    #msg['to'] = 'liangll@funshion.com'
    #msg['to'] = 'maojy@funshion.com'
    #msg['to'] = 'yangjiao@funshion.com'
    #msg['to'] = 'maojy@funshion.com'
    #msg['to'] = 'wubo@funshion.com'
    msg['to'] = 'zeus-scrum@funshion.com'
    msg['subject']=title
    smtp = smtplib.SMTP('mail.funshion.com',25,'qa-pub')
    smtp.login(username, password)
    smtp.sendmail(sender, receiver, msg.as_string())
    smtp.quit()


#smail('/var/ftp/pub/result.html')                                 
