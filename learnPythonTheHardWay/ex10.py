#-*- coding:utf-8 -*-
# ESCAPE	WHAT IT DOES.
# \\	Backslash (\)
# \'	Single-quote (')
# \"	Double-quote (")
# \a	ASCII bell (BEL)
# \b	ASCII backspace (BS)
# \f	ASCII formfeed (FF)
# \n	ASCII linefeed (LF)
# \N{name}	Character named name in the Unicode database (Unicode only)
# \r	Carriage Return (CR)
# \r 表示换行，但是没有\n,所以不会到下一行，而是将光标移到了本行最前面，然后继续输出\r后面的字符。
# 例如：
# print "abcd\re" 光标移到最前，会输出e，覆盖掉a，然后继续输出bcd，得到的答案是ebcd
# print "abcd\reeeee" eeeee会吧abcd都覆盖掉，输出eeeee
# \t	Horizontal Tab (TAB)
# \uxxxx	Character with 16-bit hex value xxxx (Unicode only)
# \Uxxxxxxxx	Character with 32-bit hex value xxxxxxxx (Unicode only)
# \v	ASCII vertical tab (VT)
# \ooo	Character with octal value ooo
# \xhh	Character with hex value hh

tabby_cat = "\tI'm tabbed in."
persian_cat = "I'm split\non a line."
backslash_cat = "I'am \\ a \\ cat."

fat_cat = """
I'll do a list:
\t* Cat food
\t* Fishies
\t* Catnip\n\t* Grass
"""
print tabby_cat
print persian_cat
print backslash_cat
print fat_cat

while True:
    for i in ["/","_","|","\\","|"]:
        print "%s\r" %i,
