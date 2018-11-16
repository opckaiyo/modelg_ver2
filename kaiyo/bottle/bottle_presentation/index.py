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
from my_voice import jtalk, jtalk_say
from my_gpio import led_red, led_green, led_yellow, led_off, led_blue, led_purple, led_lihtblue



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

    up_down(int(val["slider1"]))
    go_back(int(val["slider1"]))

    if val["mode"] == "a":
        jtalk(file_name="modea", voice="エイチワイの皆さんこんにちは、これから、海洋ロボットの説明を始めます。　私のなまえは「ちぶるまぎーもでるじーです」")
        # jtalk(file_name="modea", voice="皆さんこんにちは、これから、海洋ロボットの説明を始めます。　私のなまえは「ちぶるまぎーもでるじーです」")

    if val["mode"] == "b":
        jtalk(file_name="modedb", voice="私は「海洋ロボットコンペティション、イン、沖縄」に出場するためにかいはつされた、海洋ロボットです。")

    if val["mode"] == "c":
        jtalk(file_name="modedc", voice="私は主に、アルミニウムとアクリルで構成されています。モータには12ボルトのDCモータ、メインコントローラにはラズベリーパイモデルBを使用しています。バッテリは11.1ボルトのしゅ制御用と「制御回路用」の7.4ボルトのリポバッテリを使用しています。センサ類は主に方向検出用の9軸センサ、水深の検出には圧力センサ、また、各スラスターにはモータの回転数を検出するための「ロータリエンコーダ」を搭載しています。")
        # jtalk(file_name="modedc2", voice="潜航深度は最大で5メートル、航行速度は最大で2メートル毎秒です。")
        # jtalk(file_name="modedc3", voice="それでは、実際にスラスタを動かしてみたいと思います。機体から少しだけ離れてください。　このスラスタで潜水や浮上を行います。　　")
        # jtalk(file_name="modedc4", voice="また、こちらのスラスタでは、前進や行進、旋回などを行います。　　")
        # jtalk(file_name="modedc5", voice="また、こちらのLEDは外部からロボットがどのような「動作」をしているかがわかりやすいように7しょくで「現在」の状態を表現しています")
        # jtalk(file_name="modedc6", voice="これで海洋ロボットの説明を終了します。ご清聴、ありがとうございました。")

    if val["mode"] == "d":
        jtalk_say(file_name="modea")
        time.sleep(9)
        jtalk_say(file_name="modedb")
        time.sleep(10)
        jtalk_say(file_name="modedc")
        time.sleep(34)
        jtalk_say(file_name="modedc2")
        time.sleep(8)

        jtalk_say(file_name="modedc3")
        led_blue()
        time.sleep(7)
        up_down(20)
        time.sleep(2)
        up_down(90)
        time.sleep(3)
        stop()
        led_off()

        jtalk_say(file_name="modedc4")
        led_purple()
        time.sleep(3)
        go_back(20)
        time.sleep(2)
        go_back(90)
        time.sleep(3)
        stop()
        led_off()


        jtalk_say(file_name="modedc5")
        led_red()
        time.sleep(1.5)
        led_blue()
        time.sleep(1.5)
        led_green()
        time.sleep(1.5)
        led_purple()
        time.sleep(1.5)
        led_yellow()
        time.sleep(1.5)
        led_lihtblue()
        time.sleep(1.5)
        led_off()
        time.sleep(3)

        jtalk_say(file_name="modedc6")



    # if int(val["slider1"]) == 0:
    #     go_back(int(val["slider2"]))
    # else:
    #     spinturn(int(val["slider1"]))
    # up_down(int(val["slider3"]))

    # go_back(int(val["pitch"]))



def main():
    print("Initialize port")
    print('Server Start')
    run(host='172.20.10.8', port=8888, debug=True, eloader=True)


def atExit():
    # stop()
    print("atExit")



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
