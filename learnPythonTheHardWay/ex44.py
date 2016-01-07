# -*- coding:utf-8 -*-
from resource import other

class Parent(object):
    def implicit(self):
        print "PARENT implicit()"
    def override(self):
        print "PARENT override()"
    def altered(self):
        print "PARENT altered()"

class Child(Parent):
    def override(self):
        print "CHILD override()"
    def altered(self):
    	print "CHILD, BEFORE PARENT altered()"
    	super(Child,self).altered()
    	print "CHILD, AFTER PARENT altered()"

dad = Parent()
son = Child()

dad.implicit()
son.implicit()

dad.override()
son.override()

dad.altered()
son.altered()


class Person(object):
    def __init__(self):
        self.other = other.Other()
    def implicit(self):
        self.other.implicit()
    def override(self):
        print "CHILD override()"
    def altered(self):
        print "CHILD, BEFORE OTHER altered()"
        self.other.altered()
        print "CHILD, AFTER OTHER altered()"

son = Person()

son.implicit()
son.override()
son.altered()
