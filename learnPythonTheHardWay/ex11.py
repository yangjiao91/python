#-*- coding:utf-8 -*-
# input() 相当于调用完 raw_input() 之后再调用 eval() 函数，
# raw_input()  将所有输入作为字符串看待，返回字符串类型
# eval() eval('3+4') 将字符串str当成有效Python表达式来求值，并返回计算结果。
print "How old are you?",
age = raw_input()
print "How tall are you?",
height = raw_input()
print "How much do you weigh?",
weight = raw_input("weight:")

print "So, you're %r old, %r tall and %r heavy." % (age, height, weight)

# How old are you? 38
# How tall are you? 6'2"
# How much do you weigh? 180lbs
# So, you're '38' old, '6\'2"' tall and '180lbs' heavy.
