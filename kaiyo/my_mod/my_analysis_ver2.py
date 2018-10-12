# -*- coding: utf-8 -*-
import ast
import time

import sys
sys.path.append("/kaiyo/my_mod")

#------------------------------------------------------------------------------


def get_log():
    vals_min = {}
    vals_max = {}
    vals = {}
    cnt = 0

    file_name = "/kaiyo/log/181010_013247.txt"
    file = open(file_name, 'r')
    data = file.readline()
    data = ast.literal_eval(data)

    print "\n----------------------------"
    print "File name :", file_name
    print "keys :",
    for key in data.keys():
        print key,
        vals_min[key] = 0
        vals_max[key] = 0
    print "\n----------------------------\n"
    file.close()

    for key, val in vals_min.items():
        file = open(file_name, 'r')
        while True:
            try:
                data = file.readline()
                data = ast.literal_eval(data)

                vals[str(cnt)] = data[key]
                cnt+=1
            except Exception as e:
                print key
                print "----------------------------"
                print "MIN :", min(vals.values())
                print "MAX :", max(vals.values())
                print "----------------------------\n"

                vals_min[key] = min(vals.values())
                vals_max[key] = max(vals.values())
                cnt = 0
                file.close()
                break

    print "ALL"
    print "----------------------------"
    print "Number of data :", cnt
    print "MIN :", vals_min
    print "MAX :", vals_max
    print "----------------------------\n"


if __name__ == '__main__':
    # get_log("roll")
    get_log()
