# -*- coding:utf-8 -*-

def loop(max,step):
    numbers = []
    i = 0
    while i < max:
        print "At the top i is %d" % i
        numbers.append(i)

        i = i + step
        # i++  error
        print "Numbers now: ",numbers
        print "At the bottom i is %d" % i

    print "The numbers: "

if __name__ == "__main__":
    loop(10,2)
