# -*- coding:utf-8 -*-
import random

usage= """Please input you opt:
1  rock
2  scissors
3  paper
"""
print usage

results = "*****Your's choice is : %r,\n*****Robot's choice is : %r,\n*****Results is : %r."
opts = ["rock","scissors","paper"]

def getYourOpt():
    your_opt = raw_input("> ")
    if your_opt in ("1","2","3"):
        return opts[int(your_opt)-1]
    elif your_opt in opts:
        return your_opt
    else:
        print "Unknown input,please input again ..."
        return ""

def getRobotOpt():
    return random.choice(opts)

def compare(john,robot):
    if john == robot:
        return "a draw -_-"
    elif john=="rock" and robot=="scissors"  or john=="scissors" and robot=="paper" or john=="paper" and robot=="rock":
        return "You win ^_^"
    else:
        return "robot win *_*"

while True:
    your_opt = getYourOpt()
    if your_opt == "":
        continue
    else :
        robot_opt = getRobotOpt()
        result = compare(your_opt,robot_opt)
        print results %(your_opt,robot_opt,result)
    print "*********Next*********"
