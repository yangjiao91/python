#-*- coding: utf-8 -*-

from fit.ColumnFixture import ColumnFixture
import httplib
import compareDict
import simplejson

class ZeusTest(ColumnFixture):
    _typeDict = {
        "getorpost": "String",
        "expectedresult": "String",
        "description":"String",
        "specialid":"String",
        "parameter":"String",
        "url":"String",

        }

    def __init__ (self):
        ColumnFixture.__init__(self)
        self.getorpost=""
        self.url=""
        self.src=""
        self.cli=""
        self.ver=""
        self.ta=""
        self.jk=""
        self.expectedresult=""
        self.description=""
        self.specialid=""
        self.parameter=""

    _typeDict["compareresult"] = "String"


    def compareresult(self):


        #http request
        conn = httplib.HTTPConnection('jsonfe.funshion.com')
        if self.getorpost == 'get':
            completeurl = self.url +"?"+ self.parameter
            conn.request('GET',completeurl)
        else:
            conn.request("POST",self.url,self.parameter)
            completeurl = "url: "+self.url +"\nparameter: "+ self.parameter
        res = conn.getresponse().read()
        conn.close()

        #如果发生系统错误重试一次
        if res.find('\"retCode\":\"500\"')>0:
            print 'error 500'
            conn = httplib.HTTPConnection('jsonfe.funshion.com')
            if self.getorpost == 'get':
                completeurl = self.url +"?"+ self.parameter
                conn.request('GET',completeurl)
            else:
                conn.request("POST",self.url,self.parameter)
                completeurl = "url: "+self.url +"\nparameter: "+ self.parameter
            res = conn.getresponse().read()
            conn.close()

        expectedresult = self.expectedresult.replace('^','|')
        #expectedresult = self.expectedresult.replace(' ','')
        res = res.replace('  ',' ')
     
        #compare result
       
        #print 'expectedresult: ',expectedresult
        #print 'res: ',res
        res.decode("utf-8")
        try:
            res_dict = simplejson.loads(res)
        except Exception,ex:
            return "actual result return Error message, Json resolution fail"
        try:
            expectedres_dict = simplejson.loads(expectedresult)
        except Exception,ex:
            return "expected result Json resolution fail"

        if res==expectedresult or res_dict==expectedres_dict:
            return 'same'
        else :
            return compareDict.compareDict(res,expectedresult,'/',completeurl,'new')
