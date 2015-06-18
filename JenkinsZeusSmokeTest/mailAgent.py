#!/usr/local/bin/python

import smtplib,codecs
from email.mime.multipart import MIMEMultipart
from email.mime.base import MIMEBase
from email.mime.text import MIMEText
from email.utils import COMMASPACE,formatdate
from email import encoders
import os


class mailAgent():  
    def __init__(self,server, fro, to, cc, subject, text, files=[]):
        self.server = server
        self.fro = fro
        self.to = to
        self.cc = cc
        self.subject = subject 
        self.text = text
        self.files = files                                   

    def send_mail(self): 
        assert type(self.server) == dict 
        assert type(self.to) == list 
        assert type(self.cc) == list 
        assert type(self.files) == list 

        msg = MIMEMultipart('alternative') 
        msg['From'] = self.fro 
        msg['Subject'] = self.subject 
        msg['To'] = COMMASPACE.join(self.to)  
        msg['Cc'] =COMMASPACE.join(self.cc)
        msg['Date'] = formatdate(localtime=True) 
        self.text = self.text+codecs.open(self.files[0],'r').read()
        msg.attach(MIMEText(self.text,'html','gb2312'))

        for perfile in self.files: 
            part = MIMEBase('application', 'octet-stream') 
            part.set_payload(open(perfile,'rb').read())
            encoders.encode_base64(part) 
            part.add_header('Content-Disposition', 'attachment; filename="%s"' % os.path.basename(perfile)) 
            msg.attach(part) 

        import smtplib 
        smtp = smtplib.SMTP(self.server['name']) 
        smtp.login(self.server['user'], self.server['passwd']) 
        smtp.sendmail(self.fro, self.to,msg.as_string()) 

        for ccmail in self.cc:
            if ccmail in self.to:
                continue
            smtp.sendmail(self.fro,ccmail, msg.as_string()) 

        smtp.close()
        print "Mail sent to %s,%s, please sign in to your email account to check." %(self.to,self.cc)
