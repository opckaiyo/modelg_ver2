#coding: utf-8
import numpy as np
import time
import sys
sys.path.append("/kaiyo/my_mod")
from my_get_serial import get_data, send_data
from my_motor import go_back, up_down, spinturn, roll, stop, stop_go_back, stop_up_down, br_xr, go_back_each, up_down_each, spinturn_each, spinturn_meca, pump, stop_pump
from my_gpio import led_red, led_green, led_yellow, led_off, led_blue, led_purple, led_lihtblue


# -----------------------------------------------------------------------------

# 指定した角度に機体を持っていく関数
# def yaw(val):
#     while True:
#         # diving(80)
#         #up_down(60)
#
#         gol_val = val
#         # (0 ~ 100) → (-100 ~ 0 ~ 100)
#         now_val = my_map(get_data("yaw"))
#         # (-100 ~ 0 ~ 100) → (0 ~ 200)
#         now_val2 = map_yaw2(now_val)
#         print "gol_val", gol_val
#         print "now_val", now_val
#         # 偏差を調べる
#         dev_val = now_val2 - gol_val
#         if dev_val >= 101:
#             dev_val = -(200 - dev_val)
#
#         # モータの出力を調整(-100 ~ 0 ~ 100) → (-60 ~ 0 ~ 60)
#         dev_val = map_yaw_adjustment(dev_val)
#         spinturn(-dev_val)
#
#         print "dev_val", -dev_val
#
#         # 目標角度になったら終了
#         # if dev_val <= 1 and dev_val >= -1:
#         if dev_val <= 0 and dev_val >= 0:
#             print "balance OK !!!"
#             stop_go_back()
#             return 0
#
#         print


# 指定した角度に機体を持っていく関数
# 改良版　モータの出力を抑える関数が入っている
def yaw(set_angle, set_diving=True):
    while True:
        if set_diving:
            diving(set_diving)
            #up_down(60)

        gol_val = set_angle
        # (0 ~ 100) → (-100 ~ 0 ~ 100)
        now_val = my_map(get_data("yaw"))
        # (-100 ~ 0 ~ 100) → (0 ~ 200)
        now_val2 = map_yaw2(now_val)
        print "gol_val", gol_val
        print "now_val", now_val
        # 偏差を調べる
        dev_val = now_val2 - gol_val
        if dev_val >= 101:
            dev_val = -(200 - dev_val)

        # 目標角度になったら終了
        if dev_val <= 2 and dev_val >= -2:
        # if dev_val <= 0 and dev_val >= 0:
            print "balance OK !!!"
            stop_go_back()
            return 0


        # モータの出力を調整(-100 ~ 0 ~ 100) → (-60 ~ 0 ~ 60)
        dev_val = map_yaw_adjustment(dev_val)
        spinturn(-dev_val)

        print "dev_val", -dev_val
        print "motor_out", -dev_val
        print

# -----------------------------------------------------------------------------

# 回転数分 旋回する
def yaw_rot(set_rot, set_diving=True):
    set_rot_old = get_data("rot0")
    while True:
        if set_diving:
            diving(set_diving)

        spinturn(-20)

        now_rot0 = get_data("rot0")
        print "rot---------------------------------",now_rot0 - set_rot_old

        if now_rot0 - set_rot_old >= set_rot:
            stop()
            break

# 指定した角度に機体を持っていく関数
# def yaw_test(val, val2):
#     # while True:
#     # diving(80)
#     #up_down(60)
#
#     gol_val = val
#     # (get_data("yae") = 0 ~ 100)
#     # (now_val = -100 ~ 0 ~ 100)
#     # now_val = my_map(get_data("yaw"))
#     now_val = my_map(val2)
#     # (now_val2 = 0 ~ 200)
#     now_val2 = map_yaw2(now_val)
#     print "gol_val", gol_val
#     print "now_val", now_val
#
#     # 偏差を調べる
#     dev_val = now_val2 - gol_val
#     if dev_val >= 101:
#         dev_val = -(200 - dev_val)
#
#     # 機体を回転
#     # spinturn(-dev_val)
#     # (-100 ~ 0 ~ 100) → (-60 ~ 0 ~ 60)
#     dev_val = map_yaw_adjustment(dev_val)
#     print "dev_val", -dev_val
#
#     # # 目標角度になったら終了
#     # # if dev_val <= 1 and dev_val >= -1:
#     # if dev_val <= 0 and dev_val >= 0:
#     #     print "balance OK !!!"
#     #     stop_go_back()
#     #     return 0
#
#     print


def my_map(val):
    if val <= 50:
        in_min = 0
        in_max = 50
        out_min = 0
        out_max = 100
        val = (val - in_min) * (out_max - out_min) / (in_max - in_min) + out_min
        # 少数切り捨ての為intに変換
        return int(val)
    else:
        in_min = 100
        in_max = 50
        out_min = -0
        out_max = -100
        val = (val - in_min) * (out_max - out_min) / (in_max - in_min) + out_min
        # 少数切り捨ての為intに変換
        return int(val)


def map_yaw2(val):
    if val >= 1:
        in_min = 1
        in_max = 100
        out_min = 1
        out_max = 100
        val = (val - in_min) * (out_max - out_min) / (in_max - in_min) + out_min
        # 少数切り捨ての為intに変換
        return int(val)
    elif val <= -1:
        in_min = -100
        in_max = -1
        out_min = 101
        out_max = 200
        val = (val - in_min) * (out_max - out_min) / (in_max - in_min) + out_min
        # 少数切り捨ての為intに変換
        return int(val)
    else:
        return 0


# モータ出力をお押せる関数
def map_yaw_adjustment(val):
    in_min = 0
    in_max = 100
    out_min = 0
    out_max = 60
    # out_max = 100
    val = (val - in_min) * (out_max - out_min) / (in_max - in_min) + out_min

    if val == 0:
        val = 0
    elif val <= 10 and val >= -10:
        if val >= 0:
            val = 10
        else:
            val = 10
    return int(val)

# -----------------------------------------------------------------------------

# 指定した角度に機体を持っていく関数
# タイマーで制御
def go_yaw_time(set_speed, set_angle, set_time, set_diving=True):
    old_time = time.time()
    while True:
        if set_diving:
            diving(set_diving)
            #up_down(60)

        gol_val = set_angle
        # yawを取得して変換
        now_val = my_map(get_data("yaw"))
        print "gol_val", gol_val
        print "now_val", now_val
        # 偏差を調べる
        dev_val = gol_val - now_val
        if dev_val <= 100:
            print "dev_val",dev_val
        else:
            # 左側を向いていれば、この計算
            dev_val = -1*((100 - (-1*now_val)) + (100 - gol_val))
            print "dev_val2", dev_val

        r = set_speed
        l = set_speed

        if dev_val >= 0:
            # 右に動く（右を弱める）
            r = set_speed - dev_val
        else:
            # 左に動く（左を弱める）
            l = set_speed + dev_val

        go_back_each(l, r)

        print l, r
        print

        ela_time = time.time() - old_time
        print ela_time

        if ela_time >= set_time:
            stop()
            break


# -----------------------------------------------------------------------------

# 指定した角度に機体を持っていく関数(改良版)
def go_yaw_rot(set_speed, set_angle, set_rot, set_diving=True):
    set_rot_old = get_data("rot0")
    while True:
        if set_diving:
            diving(set_diving)
            #up_down(60)

        gol_val = set_angle
        # yawを取得して変換( -100 ~ 0 ~ 100)
        now_val = my_map(get_data("yaw"))

        print "gol_val", gol_val
        print "now_val", now_val
        # 偏差を調べる
        dev_val = gol_val - now_val
        if dev_val <= 100:
            print "dev_val",dev_val
        else:
            # 左側を向いていれば、この計算
            dev_val = -1*((100 - (-1*now_val)) + (100 - gol_val))
            print "dev_val2", dev_val

        r = set_speed
        l = set_speed

        if dev_val >= 0:
            dev_val = map15(dev_val, set_speed)
            # 右に動く（右を弱める）
            r = set_speed - dev_val
            r = map13(r, set_speed)
        else:
            dev_val = map15(dev_val, set_speed)
            # 左に動く（左を弱める）
            l = set_speed + dev_val
            l = map13(l, set_speed)
            # if l <= -100:
            #     l =  (200 + l)

        print l, r

        go_back_each(l, r)

        now_rot0 = get_data("rot0")
        print "rot---------------------------------",now_rot0 - set_rot_old
        print

        if now_rot0 - set_rot_old >= set_rot:
            print "rot stop!!"
            stop()
            break


def map15(val, set_speed):
    if val <= 0:
        in_min = 0
        in_max = -100
        out_min = 0
        out_max = -set_speed
        val = (val - in_min) * (out_max - out_min) / (in_max - in_min) + out_min
        # 少数切り捨ての為intに変換
        return int(val)
    else:
        in_min = 0
        in_max = 100
        out_min = 0
        out_max = set_speed
        val = (val - in_min) * (out_max - out_min) / (in_max - in_min) + out_min
        # 少数切り捨ての為intに変換
        return int(val)


def map13(val, set_speed):
    if val >= 0:
        in_min = 0
        in_max = set_speed
        out_min = -100
        out_max = set_speed
        val = (val - in_min) * (out_max - out_min) / (in_max - in_min) + out_min
        # 少数切り捨ての為intに変換
        return int(val)
    else:
        in_min = 0
        in_max = set_speed
        out_min = -100
        out_max = set_speed
        val = (val - in_min) * (out_max - out_min) / (in_max - in_min) + out_min
        # 少数切り捨ての為intに変換
        return int(val)


# -----------------------------------------------------------------------------


# 指定した角度に機体を持っていく関数(onとoff)
def go_yaw_onoff(set_speed, set_angle, set_rot, set_diving=True):
    set_rot_old = get_data("rot0")
    while True:
        if set_diving:
            diving(set_diving)

        gol_val = set_angle

        # yawを取得して変換( -100 ~ 0 ~ 100)
        now_val = my_map(get_data("yaw"))

        print "gol_val", gol_val
        print "now_val", now_val
        # 偏差を調べる
        dev_val = gol_val - now_val
        if dev_val <= 100:
            print "dev_val",dev_val
        else:
            # 左側を向いていれば、この計算
            dev_val = -1*((100 - (-1*now_val)) + (100 - gol_val))
            print "dev_val2", dev_val

        # この範囲の時は直進
        if dev_val >= -1 and dev_val <= 1:
            # print "Move LR"
            r = set_speed
            l = set_speed
        else:
            if dev_val <= 0:
                # 左に動かす
                # print "Move L"
                r = set_speed
                # l = 0
                l = set_speed / 2
            else:
                # 右に動かす
                # print "Move R"
                # r = 0
                r = set_speed / 2
                l = set_speed

        print l, r
        print

        go_back_each(l, r)

        now_rot0 = get_data("rot0")
        print "rot---------------------------------",now_rot0 - set_rot_old
        # print "rot0",now_rot0

        if now_rot0 - set_rot_old >= set_rot:
            print "rot stop!!"
            stop()
            break



# ----------------------------------------------------------------------------

# 潜水
def diving_while(val):
    while True:
        depth = get_data("depth")
        # 変換
        map_depth_val = map_depth(depth)
        print "depth", depth

        now_val = map_depth_val
        gol_val = val
        dev_val = gol_val - now_val

        print "now_val", now_val
        print "gol_val", gol_val
        print "dev_val", dev_val
        dev_val = map_depth2(dev_val)
        print "dev_val_map",dev_val
        print
        up_down(-dev_val)

        if dev_val <= 2 and dev_val >= -2:
            print "depth OK !!!"
            stop_up_down()
            return 0

# 潜水
def diving(val):
    # print "depth!!"
    # 圧力センサの値を取得
    depth = get_data("depth")
    # (圧力センサの値) → (0 ~ 100)
    map_depth_val = map_depth(depth)
    # print "depth", depth

    now_val = map_depth_val
    gol_val = val
    dev_val = gol_val - now_val

    # print "now_val", now_val
    # print "gol_val", gol_val
    # print "dev_val", dev_val
    dev_val = map_depth2(dev_val)
    # print "motor_out",dev_val
    print
    up_down(-dev_val)


# 圧力センサーの値を(0 ~ 100)に変換
def map_depth(val):
    # 海での値(波の上)
    # in_min = 0.6
    # in_max = 10
    # 宜野湾
    # in_min = 0.6
    # in_max = 7.6
    # 小学校プール
    in_min = 1.5
    in_max = 6

    # プールでの値
    # in_min = 2
    # in_max = 7

    if val <= in_min: val = in_min
    if val >= in_max: val = in_max

    in_min = in_min
    in_max = in_max
    out_min = 0
    out_max = 100
    val = (val - in_min) * (out_max - out_min) / (in_max - in_min) + out_min
    return int(val)


# モータの出力を調整
def map_depth2(val):
    # 出力範囲の設定
    set_range = 5
    # 偏差が小さければモータ出力は0
    if val <= set_range and val >= -set_range:
        val = 0
        return int(val)
    else:
        if val >= 0:
            in_min = 0
            in_max = 100
            # out_min = set_range
            out_min = 40
            out_max = 90
            val = (val - in_min) * (out_max - out_min) / (in_max - in_min) + out_min
            return int(val)
        else:
            in_min = 0
            in_max = -100
            # out_min = -set_range
            out_min = -40
            out_max = -90
            val = (val - in_min) * (out_max - out_min) / (in_max - in_min) + out_min
            return int(val)

# ----------------------------------------------------------------------------

# Uターン地点に行くまでのプログラム
def go_yaw_onoff_iki(set_speed, set_rot, set_diving=True):
    set_rot_old = get_data("rot0")
    while True:
        # pitch()
        if set_diving:
            diving(set_diving)

        # yawを取得( 180 ~ 0 ~ -180)
        now_val = get_data("yaw2")

        # この範囲の時は直進
        if now_val >= -1 and now_val <= 1:
            r = set_speed
            l = set_speed
        else:
            if now_val <= 0:
                # 左に動かす
                r = set_speed
                l = int(set_speed / 1.5)
            else:
                # 右に動かす
                r = int(set_speed / 1.5)
                l = set_speed

        go_back_each(l, r)

        print l, r

        now_rot0 = get_data("rot0")
        print "rot---------------------------------",now_rot0 - set_rot_old
        print

        if now_rot0 - set_rot_old >= set_rot:
            stop()
            break

# -----------------------------------------------------------------------------

# Uターン地点に行くまでのプログラム
def go_yaw_onoff_kaeri(set_speed, set_rot, set_diving=True):
    set_rot_old = get_data("rot0")
    while True:
        pitch()
        if set_diving:
            diving(set_diving)

        # yawを取得( 180 ~ 0 ~ -180)
        now_val = get_data("yaw2")
        print now_val

        # この範囲の時は直進
        if now_val >= 179 or now_val <= -179:
            r = set_speed
            l = set_speed
        else:
            if now_val <= 0:
                # 右に動かす
                r = int(set_speed / 1.5)
                l = set_speed
            else:
                # 左に動かす
                r = set_speed
                l =int(set_speed / 1.5)

        go_back_each(l, r)

        print l, r

        now_rot0 = get_data("rot0")
        print "rot---------------------------------",now_rot0 - set_rot_old
        print

        if now_rot0 - set_rot_old >= set_rot:
            stop()
            break

def pitch():
    now_val = get_data("roll")
    print now_val

    if now_val >= 0:
        pump(100)
        led_blue()
    else:
        stop_pump()
        led_off()


if __name__ == '__main__':
    while True:
        pitch()
    # print "-------------------------------------------------------------"
    # # diving_test(70, 3)
    # # print map_depth(3.2)
    #
    # for i in np.arange(0.01, 3.2, 0.1):
    #     # print "i =", i
    #     diving_test(80, i)
    #     # print map_depth(i)
