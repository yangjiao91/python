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
context_filename = 'user-service.xml'

import sys,os
import getopt
import zipfile,time

def usage():
        print doc
        sys.exit(1)

class OnekeyRelease:
    #def __init__(self,warFilePath,tomcatHome,webHome,replaceScript):
    def __init__(self,warFilePath,tomcatHome,webHome):
        self.warFilePath = warFilePath
        self.tomcatHome = tomcatHome
        self.webHome = webHome
        #self.replaceScript = replaceScript


    def getversion(self):
        if not (os.path.isfile(self.warFilePath)):
            print '\033[41m war_filepath:',self.warFilePath,'is not exist or not a war file \033[0m'
            sys.exit(1)

        cmd="cat "+self.tomcatHome+"conf/Catalina/localhost/"+context_filename+"|awk '{print $3}'"
        print "----cmd",cmd
	version = os.popen(cmd).readlines()[0].split('\n')[0]
        print 'current version: \033[33m',version,'\033[0m'

        ver=version.split('.')
        if len(ver) == 3 :
            ver_1 = int(ver[0])
            ver_2 = int(ver[1])
            ver_3 = int(ver[2]) + 1
            if ver_3 == 50:
                ver_3 = 0
                ver_2 = ver_2 + 1
                if ver_2 == 10:
                    ver_2 = 0
                    ver_1 = ver_1 + 1
            new_version = str(ver_1) + '.' + str(ver_2) + '.' + str(ver_3)
            print 'new_version: \033[33m',new_version,'\033[0m'
            return version,new_version

        else:
             print '\033[41m the form of version is incorrect \033[0m'
             sys.exit(1)

    # def shutdown():
    #     cmd = tomcatHome+"bin/shutdown.sh"
    #     os.system(cmd)
    #     pid=process()
    #     while pid != []:
    #         time.sleep(1)
    #         pid=process()
    #     print "[INFO] \033[33m tomcat is stopped \033[0m"

    # def startup():
    #     cmd = tomcatHome+'bin/startup.sh'
    #     os.system(cmd)
    #     pid=process()
    #     while pid == []:
    #         time.sleep(1)
    #         pid=process()
    #     print "[INFO] \033[33m",warFilePath,"is deployed,pid:",pid,"\033[0m"

    # def process():
    #     try:
    #         pid_cmd = "ps -ef|grep '" + tomcatHome + "'|grep java|grep -v grep|head -n 1|awk '{print $2}'"
    #         pid = os.popen(pid_cmd).readlines()
    #         return pid
    #     except os.error,e:
    #         sys.exit(1)

    def releasefun(self):

        version,new_version=self.getversion()

        version_home = self.webHome + new_version + '/'
        print "------version_home:",version_home
        web_root_home = version_home+'web/'

        print "------web_root_home:",web_root_home
        try:
            os.makedirs(version_home)
        except os.error,e:
            print '\033[41m [ERROR] mkdir',version_home,'failed! \033[0m'
            sys.exit(1)
        try:
            os.makedirs(web_root_home)
        except os.error,e:
            print '\033[41m [ERROR] mkdir',web_root_home,'failed! \033[0m'
            sys.exit(1)
        print '[INFO] \033[33m mkdir new version web directory:',web_root_home,'success \033[0m'

        f = zipfile.ZipFile(self.warFilePath, 'r')
        f.extractall(web_root_home)
        f.close()
        print '[INFO] \033[33m unzip',self.warFilePath,'-d ',web_root_home,'success \033[0m'

        try:
            replace_cmd = replaceScript+' '+web_root_home
            os.system(replace_cmd)
            print '[INFO] \033[33m replace_conf success \033[0m'
        except os.error,e:
            print '\033[41m [ERROR] replace_conf failed! \033[0m'
            sys.exit(1)

        shutdown()
        replace_version_cmd="sed -i 's/"+version+"/"+new_version"/g'"+tomcat_home+"conf/Catalina/localhost/" + context_filename
        startup()


# def main(argv = sys.argv):
#     if len(sys.argv) != 5:
#         print 'An incorrect number of parameters was passed'
#         sys.exit(1)

#     short_args = "hp:t:w:f:"
#     long_args = ["help","warfilepath=","tomcathome=","webhome=","replaceScript="]
#     try:
#         opts,args = getopt.getopt(argv[1:],short_args,long_args)
#     except:
#         usage()
#     for opt,value in opts:
#         if opt in ('-h','--help'):
#             usage()
#         if opt in ('-p','--warfilepath'):
#             warFilePath = value
#         if opt in ('-t','--tomcathome'):
#             tomcatHome = value
#         if opt in ('-w','--webhome'):
#             webHome = value
#         if opt in ('-f','--replaceScript'):
#             replaceScript = value
#     prog = OnekeyRelease(warFilePath,tomcatHome,webHome,replaceScript)
            
if __name__ == '__main__':
    #getoptfun()
    warFilePath = "/usr/local/apache-tomcat-7.0.14/webapps/user-service.war"
    tomcatHome = "/usr/local/apache-tomcat-7.0.14/"
    webHome = "/home/yangjiao/version"
    proc = OnekeyRelease(warFilePath,tomcatHome,webHome)
    proc.releasefun()

