#-*- coding:utf-8 -*-
from sys import argv
script,input_file=argv

def print_all(f):
    print f.read()

def rewind(f):
    f.seek(0) #seek(offset,where):  where=0从起始位置移动，1从当前位置移动，2从结束位置移动。当有换行时，会被换行截断。seek（）无返回值，故值为None。

def print_a_line(f):
    print  f.readline()  #readline(n):当n为空时，默认只读当前行的内容

current_file = open(input_file)

print "First let's print the whole file:\n"
print_all(current_file)

print "Now let's rewind, kind of like a tape."
rewind(current_file)

print "Let's print three lines:"
print_a_line(current_file)

for line in current_file:
        print line,
