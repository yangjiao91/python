#-*- coding:utf-8 -*-
ten_things = "Apples Oranges Crows Telephone Light Sugar"

stuff = ten_things.split(' ')
more_stuff = ["Day", "Night", "Song", "Frisbee", "Corn", "Banana", "Girl", "Boy"]

print "stuff: ",stuff
print "more_stuff: ",more_stuff
while len(stuff) != 10:
    next_one = more_stuff.pop()
    print "Adding: ", next_one
    stuff.append(next_one)
    print "There are %d items now." %len(stuff)

print "After adding, the stuff is:",stuff

print "stuff[1]:",stuff[1]
print "stuff[-1]:",stuff[-1]
print "stuff.pop():",stuff.pop()
print "connect with \' \' :",' '.join(stuff)
print "connect with # :",'#'.join(stuff[3:5])  # '3#4'



# Python 表达式	结果	描述
# len([1, 2, 3])	3	长度
# [1, 2, 3] + [4, 5, 6]	[1, 2, 3, 4, 5, 6]	组合
# ['Hi!'] * 4	['Hi!', 'Hi!', 'Hi!', 'Hi!']	重复
# 3 in [1, 2, 3]	True	元素是否存在于列表中
# for x in [1, 2, 3]: print x,	1 2 3	迭代

L = [1,2,3,4,5]
L1 = L       #L1为L的别名，用C来说就是指针地址相同，对L1操作即对L操作。函数参数就是这样传递的
L2 = L[:]    #L1为L的克隆，即另一个拷贝
L1.append('6')
L2.append('7')
print "L: ",L
print "L1: ",L1
print "L2: ",L2

for v in L:
    print v

L.reverse()
for i in range(0,len(L)):
    print L[i]

# 列表操作包含以下函数:
# 1、cmp(list1, list2)：比较两个列表的元素
# 2、len(list)：列表元素个数
# 3、max(list)：返回列表元素最大值
# 4、min(list)：返回列表元素最小值
# 5、list(seq)：将元组转换为列表
# 列表操作包含以下方法:
# 1、list.append(obj)：在列表末尾添加新的对象
# 2、list.count(obj)：统计某个元素在列表中出现的次数
# 3、list.extend(seq)：在列表末尾一次性追加另一个序列中的多个值（用新列表扩展原来的列表）
# 4、list.index(obj)：从列表中找出某个值第一个匹配项的索引位置
# 5、list.insert(index, obj)：将对象插入列表
# 6、list.pop(obj=list[-1])：移除列表中的一个元素（默认最后一个元素），并且返回该元素的值
# 7、list.remove(obj)：移除列表中某个值的第一个匹配项
# 8、list.reverse()：反向列表中元素
# 9、list.sort([func])：对原列表进行排序
