#!/bin/env python
# coding: utf-8
import json
from bottle import route, run, request, HTTPResponse, template, static_file
# import RPi.GPIO
import atexit
import time
import random


@route('/static/:path#.+#', name='static')
def static(path):
    return static_file(path, root='static')


@route('/')
def root():
    return template("index")


global var
@route('/setLed', method='POST')
def setLedEntry():
    global var
    var = request.json
    print
    print "bbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbb","roll:",var["roll"],"  pitch:",var["pitch"], "yaw:",var["yaw"]
    print


def main():
    print("Initialize port")
    print('Server Start')
    run(host='172.20.10.6', port=8888, debug=True, eloader=True)


def atExit():
    print("atExit")


if __name__ == '__main__':
    atexit.register(atExit)
    main()
