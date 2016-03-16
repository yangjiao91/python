# # -*- coding:utf-8 -*-
#Keywords
# and	Logical and.	True and False == False
# as	Part of the with-as statement.	with X as Y: pass
with open("ex20.txt") as f:
	print f.read()

# assert	Assert (ensure) that something is true.	assert False, "Error!"
assert True/False

# break	Stop this loop right now.	while True: break
# continue	Don't process more of the loop, do it again.	while True: continue

# class	Define a class.	class Person(object)
class myClass():
	def __init__(self,a):
		self.a = a
	def returnA(self):
		return self.a
x = myClass("hello")
print x.returnA()

# def	Define a function.	def X(): pass
# del	Delete from dictionary.	del X[Y]
a = ['a','b','c','d']
print a
del a[0]   #删除第0个元素
print a
del a[1:2]
print a
del a[:]  #清空a的内容
print a
del a
print a

# elif	Else if condition.	if: X; elif: Y; else: J
# else	Else condition.	if: X; elif: Y; else: J
# except	If an exception happens, do this.	except ValueError, e: print e  ,except(RuntimeError, TypeError, NameError)
try:
	x=int(raw_input())
except ValueError:
	print "Ops!"

# exec	Run a string as Python.	exec 'print "hello"'

# finally	Exceptions or not, finally do this no matter what.	finally: pass
# for	Loop over a collection of things.	for X in Y: pass
# from	Importing specific parts of a module.	import X from Y
# global	Declare that you want a global variable.	global X
a = 2
def b():
	global a    #函数内改变外部的变量
	a = 0
	a += 1
	print a
b()
print a

# if	If condition.	if: X; elif: Y; else: J
# import	Import a module into this one to use.	import os
# in	Part of for-loops. Also a test of X in Y.	for X in Y: pass also 1 in [1] == True
# is	Like == to test equality.	1 is 1 == True
            Python中的对象包含三要素：id、type、value
            其中id用来唯一标识一个对象，type标识对象的类型，value是对象的值
            is判断的是a对象是否就是b对象，是通过id来判断的
            ==判断的是a对象的值是否和b对象的值相等，是通过value来判断的
id(a) #取得a的id

# lambda	Create a short anonymous function.	s = lambda y: y ** y; s(3)
lambda只是一个表达式
b = lambda x:x+2
print b(3)

b = lambda x:lambda y:x+y
a=b(3)
a(2)


# not	Logical not.	not True == False
# or	Logical or.	True or False == True
# pass	This block is empty.	def empty(): pass
# print	Print this string.	print 'this string'
# raise	Raise an exception when things go wrong.	raise ValueError("No")
try:
	with open("ex23.txt") as f:
		pass
except:
	raise IOError("open file error")

# return	Exit the function with a return value.	def X(): return Y
# try	Try this block, and if exception, go to except.	try: pass
# while	While loop.	while X: pass
# with	With an expression as a variable do.	with X as Y: pass
# yield	Pause here and return to caller.	def X(): yield Y; X().next()
            yield 的作用就是把一个函数变成一个 generator，
            带有 yield 的函数不再是一个普通函数，Python 解释器会将其视为一个 generator，
            调用 fab(5) 不会执行 fab 函数，而是返回一个 iterable 对象！
            在 for 循环执行时，每次循环都会执行 fab 函数内部的代码，
            执行到 yield b 时，fab 函数就返回一个迭代值，下次迭代时，代码从 yield b 的下一条语句继续执行，
            而函数的本地变量看起来和上次中断执行前是完全一样的，于是函数继续执行，直到再次遇到 yield
            generator function 中，如果没有 return，则默认执行至函数完毕，如果在执行过程中 return，则直接抛出 StopIteration 终止迭代。
            raise StopIteration()
# -*- coding:utf-8 -*-
from inspect import isgeneratorfunction
def fab(max):
	n,a,b = 0,0,1
	while n < max:
		yield b
		a, b = b, a+b
		n = n + 1

# 如何判断一个函数是否是一个特殊的 generator 函数？可以利用 isgeneratorfunction 判断
# print isgeneratorfunction(fab)
t = fab(5)
print t.next()
print t.next()

def fread_file(fpath):
	BLOCK_SIZE = 1024
	with open(fpath,'rb') as f:
		while True:
			block = f.read(BLOCK_SIZE)
			if block :
				yield block
			else:
				return

print fread_file("../ex1.py").next()




# Data Types
# True	True boolean value.	True or False == True
# False	False boolean value.	False and True == False
# None	Represents "nothing" or "no value".	x = None，它只有一个值None，None  type
type(None)  #<type 'NoneType'>

# strings	Stores textual information.	x = "hello"
# numbers	Stores integers.	i = 100
# floats	Stores decimals.	i = 10.389
# lists	Stores a list of things.	j = [1,2,3,4]
Tuple 是不可变的 list
# dicts	Stores a key=value mapping of things.	e = {'x': 1, 'y': 2}
import copy
d=dict()
d={}
d = {'name':"Jane","age":12,"weight":45}
d2 = copy.deepcopy(d)
d3 = copy.copy(d)
print "d2=",d2,",d3=",d3
print d.keys()
print d.items()
d["height"] = 160
print d.pop("name")
del(d["age"])

print sorted(d.items(),key=lambda d:d[0])
print sorted(d)

for key in d.keys():
	print d[key]
for key,value in d.items():
	print "dict[%s]="%key,value
d.clear()
print d

L = ["1","2","tel"]
print L.pop()
print L


# Escape Sequences
# \\	Backslash
# \'	Single-quote
# \"	Double-quote
# \a	Bell
# \b	Backspace
# \f	Formfeed
# \n	Newline
# \r	Carriage
# \t	Tab
# \v	Vertical tab

# String Formats
# %d	Decimal integers (not floating point).	"%d" % 45 == '45'
# %i	Same as %d.	"%i" % 45 == '45'
# %o	Octal number.	"%o" % 1000 == '1750'
# %u	Unsigned decimal.	"%u" % -1000 == '-1000'
# %x	Hexadecimal lowercase.	"%x" % 1000 == '3e8'
# %X	Hexadecimal uppercase.	"%X" % 1000 == '3E8'
# %e	Exponential notation, lowercase 'e'.	"%e" % 1000 == '1.000000e+03'
# %E	Exponential notation, uppercase 'E'.	"%E" % 1000 == '1.000000E+03'
# %f	Floating point real number.	"%f" % 10.34 == '10.340000'
# %F	Same as %f.	"%F" % 10.34 == '10.340000'
# %g	Either %f or %e, whichever is shorter.	"%g" % 10.34 == '10.34'
# %G	Same as %g but uppercase.	"%G" % 10.34 == '10.34'
# %c	Character format.	"%c" % 34 == '"'
# %r	Repr format (debugging format).	"%r" % int == "<type 'int'>"
# %s	String format.	"%s there" % 'hi' == 'hi there'
# %%	A percent sign.	"%g%%" % 10.34 == '10.34%'

# Operators
# +	Addition	2 + 4 == 6
# -	Subtraction	2 - 4 == -2
# *	Multiplication	2 * 4 == 8
# **	Power of	2 ** 4 == 16
# /	Division	2 / 4.0 == 0.5
# //	Floor division	2 // 4.0 == 0.0
# %	String interpolate or modulus	2 % 4 == 2
# <	Less than	4 < 4 == False
# >	Greater than	4 > 4 == False
# <=	Less than equal	4 <= 4 == True
# >=	Greater than equal	4 >= 4 == True
# ==	Equal	4 == 5 == False
# !=	Not equal	4 != 5 == True
# <>	Not equal	4 <> 5 == True
# ( )	Parenthesis	len('hi') == 2
# [ ]	List brackets	[1,3,4]
# { }	Dict curly braces	{'x': 5, 'y': 10}
# @	At (decorators)	@classmethod
# -*- coding:utf-8 -*-
def f1(arg):
    print "f1"
    rl = arg()
    print rl
    return rl + "f1"

@f1
# 类似于f2=f1(f2())
def f2(arg = ""):
    print "f2"
    return arg + "f2r"

print "start"
print f2

result:
f1
f2
f2r
start
f2rf1

# ,	Comma	range(0, 10)
# :	Colon	def X():
# .	Dot	self.x = 10
# =	Assign equal	x = 10
# ;	semi-colon	print "hi"; print "there"    :换行，equal \n
# +=	Add and assign	x = 1; x += 2
# -=	Subtract and assign	x = 1; x -= 2
# *=	Multiply and assign	x = 1; x *= 2
# /=	Divide and assign	x = 1; x /= 2
# //=	Floor divide and assign	x = 1; x //= 2
# %=	Modulus assign	x = 1; x %= 2
# **=	Power assign	x = 1; x **= 2
