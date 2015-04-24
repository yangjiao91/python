#!/usr/bin/python

doc = """\
onekey_release.py [-p warfilepath] [-t tomcathome] [-w webhome] [-f replaceScript]
Options:
    -p --
    -t --
    -w --
    -f --

A sample invocation:

onekey_release.py -p warfilepath -t tomcathome -w webhome -f replaceScript
"""

import sys
import getopt

def usage():
    print doc
    sys.exit(1)

def init(self,warFilePath,tomcatHome,webHome,replaceScript):
    self.warFilePath = warFilePath
    self.tomcatHome = tomcatHome
    self.webHome = webHome
    self.replaceScript = replaceScript

def getoptfun(argv=sys.argv):
    if len(sys.argv) != 5:
        print 'An incorrect number of parameters was passed'
        sys.exit(1)

    short_args="hp:t:w:f:"
    long_args=["help","warfilepath=","tomcathome=","webhome=","replaceScript="]
    try:
        opts,args =getopt.getopt(argv[1:],short_args,long_args)
    except:
        usage()

    for opt,value in opts:
        if opt in ('-h','--help'):
            usage()
        if opt in ('-p','--warfilepath'):
            warFilePath = value
        if opt in ('-t','--tomcathome'):
            tomcatHome = value
        if opt in ('-w','--webhome'):
            webHome = value
        if opt in ('-f','--replaceScript'):
            replaceScript = value

     return warFilePath,tomcatHome,webHome,replaceScript

def releasefun():



if __name__ == '__main__':


