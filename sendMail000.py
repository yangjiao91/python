#!/usr/local/bin/python
#coding:utf-8
import smtplib
import sys
from email.mime.text import MIMEText

def mail(subject,msgData):
	sender = 'account-service@funshion.com'
	receiver = 'yangjiao@funshion.com'
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

if __name__ == '__main__':	

	sub = sys.argv[1]
	msg = sys.argv[2]
	mail(sub,msg)