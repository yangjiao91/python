#-*- coding: utf-8 -*-
from fit.ColumnFixture import ColumnFixture
import urllib2
import urllib
import json

class DeteleInstance(ColumnFixture):
    _typeDict = {
    "url":"String",
    "instanceId":"String",
    "responseInstance":"Int",
    }

    def _init_(self):
        ColumnFixture.__init__(self)
        self.url = ""
        self.instanceId = ""
    
    def responseInstance(self):
        #url = 'http://10.33.0.7:8779/v1.0/49e049ab04f846a48e5f0fd152a729fc/memdb-resources'
        url = self.url + '/' + self.instanceId
        headers = {"Content-Type":"application/json","X-Auth-Token":"191532849a034f2cb555d8d8fa08027a:49e049ab04f846a48e5f0fd152a729fc"}
        request = urllib2.Request(
            url = url,
            headers = headers,
        )
        opener = urllib2.build_opener()
        request.get_method = lambda: 'DELETE'
        try:
	    ret = opener.open(request)
        except urllib2.URLError, e:
	    return e.code
        return ret.getcode()
