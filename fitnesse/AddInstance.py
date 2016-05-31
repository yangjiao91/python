#-*- coding: utf-8 -*-
from fit.ColumnFixture import ColumnFixture
import urllib2
import urllib
import json

class AddInstance(ColumnFixture):
    _typeDict = {
    "url":"String",
    "name":"String",
    "size":"Int",
    "responseInstance":"String"
    }

    def _init_(self):
        ColumnFixture.__init__(self)
        self.url = ""
        self.name = ""
        self.size = 0
    def responseInstance(self):
        #url = 'http://10.33.0.7:8779/v1.0/49e049ab04f846a48e5f0fd152a729fc/memdb-resources'
        data = '{"type":"redis","mode":"singledatanode","resource":{"name":"%s","ha":true,"size":%d}}'%(self.name,self.size)
        headers = {"Content-Type":"application/json","X-Auth-Token":"191532849a034f2cb555d8d8fa08027a:49e049ab04f846a48e5f0fd152a729fc"}

        request = urllib2.Request(
            url = self.url,
            headers = headers,
            data = data,
        )
        opener = urllib2.build_opener()
        request.get_method = lambda: 'POST'
        try: 
	    ret = opener.open(request)
        except urllib2.URLError, e:
	    return e.code
    
        retJson = json.loads(ret.read())
        return retJson['resource']['id']


