#!/usr/local/bin/python
#coding:utf-8
import smtplib
import sys
from email.mime.text import MIMEText
class send_mail():
	def send_mail(subject,msgData):
		sender = 'account-service@funshion.com'
		receiver = 'chencheng@funshion.com'
		smtpserver = 'mail.funshion.com'
		username = 'account-service@funshion.com'
		password = 'q@w#e$r1'

		msg = MIMEText(msgData,'html','utf-8')
		msg['Subject'] = subject
		msg['from'] = sender
		msg['to'] = receiver

		smtp = smtplib.SMTP()
		smtp.connect(smtpserver)
		smtp.login(username,password)
		smtp.sendmail(sender,receiver,msg.as_string())
		smtp.quit()
