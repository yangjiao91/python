#-*- coding:utf-8 -*-
# * tells Python to take all the arguments to the function and then put them in args as a list.
def print_two(*args):
    arg1,arg2 = args
    print "arg1: %r, arg2: %r" % (arg1,arg2)

def print_two_again(arg1,arg2):
    print "arg1: %r, arg2: %r" % (arg1,arg2)

def print_one(arg1):
    print "arg1: %r" % arg1

def print_none():
    print "I got nothin'."

print_two("Zed","Shaw")
# argc = {"Zed","Shaw"}
# print_two(*argc)

# print_two_again("Zed","Shaw")
print_one("First!")
print_none()
