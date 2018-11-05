#!/bin/env python
# coding: utf-8
import json
from bottle import route, run, request, HTTPResponse, template, static_file
# import RPi.GPIO
import atexit
import time
import random

import sys
sys.path.append("/kaiyo/my_mod")
from my_get_serial import get_data, send_data, log
from my_motor import go_back, up_down, spinturn, roll, stop, stop_go_back, stop_up_down, br_xr, go_back_each, up_down_each, spinturn_each, spinturn_meca
# from test2 import go_yaw_simulato

@route('/static/:path#.+#', name='static')
def static(path):
    return static_file(path, root='static')


@route('/')
def root():
    return template("index")


global var
# curl -H "Accept: application/json" -H "Content-type: application/json" -X POST -d '{"num":"0", "onoff":true}' http://192.168.1.88:8080/setLed
@route('/setLed', method='POST')
def setLedEntry():
    global var
    var = request.json
    print
    # print "bbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbb",sorted(var.items())
    print "bbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbb","roll:",var["roll"],"  pitch:",var["pitch"]
    # a = get_data("all")
    # print "bbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbb",a["flw0"],a["flw1"],a["flw2"]
    print


    # if int(var["slider1"]) == 0:
    #     go_back(int(var["slider2"]))
    # else:
    #     spinturn(int(var["slider1"]))
    # up_down(int(var["slider3"]))

    go_back(int(var["pitch"]))



def main():
    print("Initialize port")
    print('Server Start')
    run(host='172.20.10.8', port=8888, debug=True, eloader=True)


def atExit():
    # stop()
    print("atExit")



def f1():
    return random.randrange(100)




def set_kaiyo():
    pass
    # stop()
    # センサー初期化
    # send_data("reboot")
    # time.sleep(1)
    # send_data("yaw_zero off")

    # textにlogを残すか？
    # log()

    # 動作チェックするか？
    # operation_check()





if __name__ == '__main__':
    # センサー初期化
    # send_data("reboot")

    atexit.register(atExit)
    main()
