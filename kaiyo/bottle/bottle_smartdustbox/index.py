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
from my_voice import jtalk, jtalk_say



@route('/static/:path#.+#', name='static')
def static(path):
    return static_file(path, root='static')


@route('/')
def root():
    return template("index")


global val
# curl -H "Accept: application/json" -H "Content-type: application/json" -X POST -d '{"num":"0", "onoff":true}' http://192.168.1.88:8080/setLed
@route('/setLed', method='POST')
def setLedEntry():
    global val
    val = request.json
    print
    # print "bbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbb",sorted(val.items())
    # print "bbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbb","roll:",val["roll"],"  pitch:",val["pitch"]
    # a = get_data("all")
    print "bbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbb",val
    print

    if val["mode"] == "a":
        jtalk(file_name="sdb1", voice="皆さんこんにちは、これから、「スマートダストボックス」の説明を始めます。　私のなまえは「スマートダストボックス」です。")

    if val["mode"] == "b":
        jtalk(file_name="sdb2", voice="私は大型ショッピングセンターや、リゾートホテルなど、ある程度敷地の広い施設に設置されているごみ箱に")

    if val["mode"] == "c":
        jtalk(file_name="sdb3", voice="a")

    if val["mode"] == "d":
        jtalk_say(file_name="sdb1")
        time.sleep(9)



def main():
    print("Initialize port")
    print('Server Start')
    run(host='172.20.10.8', port=8888, debug=True, eloader=True)


def atExit():
    # stop()
    print("atExit")





if __name__ == '__main__':
    # センサー初期化
    # send_data("reboot")

    atexit.register(atExit)
    main()
