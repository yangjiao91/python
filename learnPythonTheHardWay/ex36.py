# -*- coding:utf-8 -*-

usage= """Please input you opt:
1  rock
2  scissors
3  paper
"""

print usage
john_opt = raw_input("> ")

if john_opt in ("1","rock"):
    print "your choice is : ",john_opt
