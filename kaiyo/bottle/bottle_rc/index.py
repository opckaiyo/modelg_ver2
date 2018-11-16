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
from my_motor import go_back, up_down, spinturn, roll, stop, stop_go_back, stop_up_down, br_xr, go_back_each, up_down_each, spinturn_each, spinturn_meca
from my_motor import br_xr, br_xl, dc_xr, dc_xl, dc_yr, dc_yl, dc_u, pump

@route('/static/:path#.+#', name='static')
def static(path):
    return static_file(path, root='static')


@route('/')
def root():
    return template("index")

@route('/index2')
def root():
    return template("index2")


global var
# curl -H "Accept: application/json" -H "Content-type: application/json" -X POST -d '{"num":"0", "onoff":true}' http://192.168.1.88:8080/setLed
@route('/setLed', method='POST')
def setLedEntry():
    global var
    var = request.json
    # print "bbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbb",var

    mode_b(var)



def mode_b(var):
    ly = int(var["slider1"])
    ry = int(var["slider2"])
    roll = int(-var["roll"])
    print "bbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbb"," ly:",ly," ry:",ry," roll:",roll


    m_xr = 0
    m_xl = 0
    m_yr = 0
    m_yl = 0


    m_xr = ry
    m_xl = ly

    m_yr = roll
    m_yl = roll

    # 出力調整
    m_xr = motor_adjustment(m_xr)
    m_xl = motor_adjustment(m_xl)

    m_yr = motor_adjustment(m_yr)
    m_yl = motor_adjustment(m_yl)

    dc_xr(-m_xr)
    dc_xl(m_xl)

    dc_yr(-m_yr)
    dc_yl(m_yl)


def mode_a(var):
    ly = int(var["pitch"])
    lx = int(var["roll"])
    ry = int(var["slider1"])
    # print "bbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbb"," ly:",ly," lx:",lx," ry:",ry


    m_xr = 0
    m_xl = 0
    m_yr = 0
    m_yl = 0


    # 0 ~ 90
    if ly >= 1 and lx >= 1:
        m_xl = ly
        m_xr = ly - lx

    # 91 ~ 180
    if ly >= 1 and lx <= -1:
        m_xr = ly
        m_xl = ly + lx

    # 180 ~ 270
    if ly <= -1 and lx <= -1:
        m_xr = ly
        m_xl = ly - lx

    # 270 ~ 360
    if ly <= -1 and lx >= 1:
        m_xl = ly
        m_xr = ly + lx

    # go_back
    if ly != 0 and lx == 0:
        m_xl = ly
        m_xr = ly

    # spinturn
    if lx != 0 and ly == 0:
        m_xl = lx
        m_xr = -lx

    # ----------------------------------

    m_yl = ry
    m_yr = ry


    # 出力調整
    m_xr = motor_adjustment(m_xr)
    m_xl = motor_adjustment(m_xl)

    m_yr = motor_adjustment(m_yr)
    m_yl = motor_adjustment(m_yl)

    # dc_xr(-m_xr)
    # dc_xl(m_xl)
    #
    # dc_yr(-m_yr)
    # dc_yl(m_yl)



def motor_adjustment(val):
    in_min = -100
    in_max = 100
    out_min = -50
    out_max = 50
    val = (val - in_min) * (out_max - out_min) / (in_max - in_min) + out_min
    return int(val)

def main():
    print("Initialize port")
    print('Server Start')
    run(host='172.20.10.8', port=8888, debug=True, eloader=True)


def atExit():
    stop()
    print("atExit")




if __name__ == '__main__':
    # センサー初期化
    # send_data("reboot")

    atexit.register(atExit)
    main()
