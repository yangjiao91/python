import send_mail
import sys

if __name__ == '__main__':
	mail=send_mail.send_mail()
	mail.send_mail('sub','content');