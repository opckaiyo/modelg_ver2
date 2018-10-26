# -*- coding: utf-8 -*-
import ast
import time

import sys
sys.path.append("/kaiyo/my_mod")

#------------------------------------------------------------------------------


def get_log():
    vals = {}
    cnt = 0

    # print
    # print "Please file name :",
    # filename = raw_input()
    # file = open('/kaiyo/log/'+filename+'.txt', 'r')
# /kaiyo/log/181005_195052.txt
    # file_name = "/kaiyo/log/181005_202822.txt"
    file_name = "/kaiyo/log/181009_212609.txt"
    file = open(file_name, 'r')
    data = file.readline()
    data = ast.literal_eval(data)

    print
    print "File name :", file_name
    print "vals :",
    for key in data.keys():
        print key,

    print
    print "Please value :",
    val = raw_input()


    while True:
        try:
            data = file.readline()
            data = ast.literal_eval(data)

            vals[str(cnt)] = data[val]
            cnt+=1
            # print data[val]
        except Exception as e:
            print "----------------------------"
            print "Number of data :", cnt
            print "MIN :", min(vals.values())
            print "MAX :", max(vals.values())
            print "----------------------------"
            break


if __name__ == '__main__':
    # get_log("roll")
    get_log()
