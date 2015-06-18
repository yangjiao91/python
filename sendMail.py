#!/usr/bin/env python
#coding:utf-8
import smtplib,sys,socket
from getopt import *
from email.mime.text import MIMEText

def mail(subject,msgData):
	sender = 'account-service@funshion.com'
	receiver = 'yangjiao@fun.tv'
	smtpserver = 'mail.funshion.com'
	username = 'account-service@funshion.com'
	password = 'q@w#e$r1'

	msg = MIMEText(msgData,'html','utf-8')
	msg['Subject'] = subject
	msg['from'] = sender
	msg['to'] = receiver

	try:
		smtp = smtplib.SMTP(smtpserver)
		code = smtp.ehlo()[0]
		usesesmtp = 1
		if not (200 <= code <=299):
			usesesmtp = 0
			code = smtp.helo()[0]
			raise SMTPHeloError(code,resp)
		if usesesmtp and smtp.has_extn('auth'):
			print "Using Authentication connect."
			try:
				smtp.login(username,password)
			except smtplib.SMTPException, e:
				print "Authentication failed:",e
				sys.exit(1)
		else:
			print "Server does not support Authentication; Using normail connect."
		smtp.sendmail(sender,receiver,msg.as_string())
		smtp.quit()
	except(socket.gaierror,socket.error,socket.herror,smtplib.SMTPException), e:
		print "***Your message may not have been sent!"
      	 	print e
        	sys.exit(1)

def getoptTest(dict):
	try:
		opts,argsTmp=getopt(dict[1:],'s:m:')
		for o,a in opts:
			if o in ("-s"):
				sub = a
			if o in ("-m"):
				msg = a
		return sub,msg
	except getopt.GetoptError:
		print("getopt error")
		sys.exit(1)

if __name__ == '__main__':	
	sub,msg=getoptTest(sys.argv)
	mail(sub,msg)
