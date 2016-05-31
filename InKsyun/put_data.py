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

def set(host=None, num=1, key_len=8, value_len=1024):

    pool = redis.ConnectionPool(host=host, port=6379,socket_timeout=10)
    r = redis.Redis(connection_pool=pool)

    keyBuffer = "AaBbCcDdEeFfGgHhIiJjKkLlMmNnOoPpQqRrSsTtUuVvWwXxYyZz0123456789"
    len1 = len(keyBuffer) -1
    valueBuffer = ["testcszf","testin.ing","7447534567"]
    value_len = value_len / 10 + 1

    success = 0
    fail = 0
    try:
        r.ping()
        for i in range(0, num):
            key = ""
            for i in range(0, key_len):
                key += keyBuffer[random.randint(0, len1)]

            value = ""
            for i in range(0,value_len):
                value += valueBuffer[random.randint(0,2)]

            try:
                r.set(key, value)
            except Exception as e:
                fail += 1
                continue
            success += 1
            print "-----key:",key,"----value:",value,"-------."
            return (success, fail)
    except Exception as e:
        print "redis connect error"
        pool.disconnect()
        return (0,1)
    pool.disconnect() 

if __name__=="__main__":
    totalsuccess,totalfail = 0,0
    total = sys.argv[2]
    for i in range(0,int(total)):
        (success, fail) = set(sys.argv[1])
        totalsuccess += success
        totalfail += fail
    print "total:",total,",success:",totalsuccess,",fail:",totalfail
