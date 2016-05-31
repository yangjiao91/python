#!/usr/bin/env python
#coding: utf-8
import sys
import os
import redis
import random
import subprocess
import multiprocessing
import time
import datetime
import pdb

def set(host="127.0.0.1", key=""):

    pool = redis.ConnectionPool(host=host, port=6379,socket_timeout=1)
    r = redis.Redis(connection_pool=pool)

    success = 0
    fail = 0
    try:
        r.ping()
	print r.get(key)
        if(r.get(key) == None):
	    print "key error,key is not exist"
            return (0,1)
	else:
            return (1,0)
    except Exception as e:
        print "redis connect error"
        pool.disconnect()
        return (0,1)
    pool.disconnect() 

if __name__=="__main__":
    totalsuccess,totalfail = 0,0
    try:
        file=open(sys.argv[2])
        lines = file.readlines()
        for line in lines:
            line = line.strip('\n')
	    (success, fail) = set(sys.argv[1],line)
            totalsuccess += success
            totalfail += fail
    finally:
        file.close()
    print "total:",totalsuccess+totalfail,",success:",totalsuccess,",fail:",totalfail
