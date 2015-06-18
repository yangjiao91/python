from getopt import *
import sys

def getoptTest(dict):
	try:
		opts,argsTmp=getopt(dict[1:],'s:m:')
		for o,a in opts:
			if o in ("-s"):
				sub = a
				print sub 
			if o in ("-m"):
				msg = a
				print msg

	except getopt.GetoptError:
		print("getopt error")
		sys.exit(1)

if __name__ == '__main__':
	argvTmp = sys.argv
	print argvTmp
	getoptTest(argvTmp)

	