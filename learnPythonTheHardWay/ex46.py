# -*- coding:utf-8 -*-
# pip from http://pypi.python.org/pypi/pip
# distribute from http://pypi.python.org/pypi/distribute
# nose from http://pypi.python.org/pypi/nose/
# virtualenv from http://pypi.python.org/pypi/virtualenv

from nose.tools import *

def setup():
    print "function setup"

def TestFunc1():
    print "TestFunc1"
    assert True

def tearDown():
    print "function tearDown"

#忽略这个测试case
@nottest
def TestFunc2():
    print "TestFunc2"
    assert True
