# python thing ????
from sys import argv

script,filename = argv

# the right way to open file
try:
    txt = open(filename)
except:
    print 'fail to open'
    exit(1)
try:
    print "Here's your file %r:" % filename
    print txt.read()
except:
    print 'fail to read'
finally:
    txt.close()

print "Type the filename again:"
file_again = raw_input("> ")

txt_again = open(file_again)

print txt_again.read()

txt_again.close()
