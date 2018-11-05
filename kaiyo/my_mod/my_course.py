#coding: utf-8
import time
import sys
# マルチタスク
sys.path.append("/kaiyo/my_mod")
from my_get_serial import get_data, send_data, log
from my_motor import go_back, up_down, spinturn, roll, stop, stop_go_back, stop_up_down, br_xr, go_back_each, up_down_each, spinturn_each, spinturn_meca
from my_balance import yaw, go_yaw_time, go_yaw_rot, diving, diving_while, go_yaw_onoff, go_yaw_onoff_iki, go_yaw_onoff_kaeri, yaw_rot
from my_rc import t10j
from my_check import operation_check, status_check, my_exit
from my_gpio import led_red, led_green, led_yellow, led_off, led_blue, led_purple, led_lihtblue
from my_state_write import state_write

# -----------------------------------------------------------------------------


"""
def test(set_speed, set_time):
def test_rot(set_speed, set_rot):
def test_rot_onoff(set_speed, set_rot):
def course_ver1(set_speed, set_rot):
def course_ver2(set_speed, set_rot):
def course_data_picking(set_speed, set_rot):
"""


def test(set_speed, set_time):
    stop()

    # 浮上
    print "up"
    # diving_while(20)
    up_down(80)
    time.sleep(3)
    yaw(0, set_diving=False)

    # Uターン地点まで行く
    print "go_yaw"
    led_green()
    go_yaw_time(set_speed, 0, set_time, set_diving=80)

    # 慣性で流れるのを停止
    stop()
    led_off()
    time.sleep(0.5)
    go_back(-30)
    time.sleep(1)
    stop()

    # 浮上
    print "up"
    # diving_while(20)
    up_down(60)
    time.sleep(2)

    # Uターン
    print "yaw"
    yaw(100, set_diving=False)

    # スタート地点まで行く
    print "go_yaw"
    led_green()
    go_yaw_time(set_speed-2, 100, set_time, set_diving=80)


    # 浮上
    print "up"
    # diving_while(20)
    up_down(80)
    time.sleep(3)


    # Uターン
    print "yaw"
    yaw(0, set_diving=False)

    led_red()
    stop()


# -----------------------------------------------------------------------------


def test_rot(set_speed, set_rot):
    stop()

    # 浮上
    print "up"
    # diving_while(20)
    up_down(80)
    time.sleep(3)
    yaw(0, set_diving=False)

    # Uターン地点まで行く
    print "go_yaw"
    led_green()
    go_yaw_rot(set_speed, 0, set_rot, set_diving=80)

    # 慣性で流れるのを停止
    stop()
    led_off()
    time.sleep(0.5)
    go_back(-30)
    time.sleep(1)
    stop()

    # 浮上
    print "up"
    # diving_while(20)
    up_down(60)
    time.sleep(4)

    # Uターンの補助
    spinturn(30)
    time.sleep(1.2)
    stop()

    # Uターン
    print "yaw"
    yaw(100, set_diving=False)
    led_red()
    time.sleep(0.5)
    print "yaw"
    yaw(100, set_diving=False)

    # スタート地点まで行く
    print "go_yaw"
    led_green()
    go_yaw_rot(set_speed, 100, set_rot)


    # 慣性で流れるのを停止
    stop()
    led_off()
    time.sleep(0.5)
    go_back(-30)
    time.sleep(1)
    stop()

    # 浮上
    print "up"
    led_off()
    # diving_while(20)
    up_down(80)
    time.sleep(3)

    # Uターンの補助
    spinturn(20)
    time.sleep(1)
    stop()

    # Uターン
    print "yaw"
    led_red()
    yaw(0, set_diving=False)

    stop()



# -----------------------------------------------------------------------------

# 停止の制御をなくして pitch のずれを少なくする
def course_ver4(set_speed, set_rot):
    stop()

    # Uターン地点まで行く(海上)
    go_yaw_onoff(set_speed, 0, 40, set_diving=5)

    # Uターン地点まで行く(潜水)
    go_yaw_onoff(set_speed, 0, 40, set_diving=80)

    # 浮上
    stop()
    up_down(60)
    time.sleep(4)

    # Uターン
    yaw(100, set_diving=False)

    # スタート地点まで行く(潜水)
    go_yaw_onoff(set_speed, 100, 70, set_diving=80)

    # スタート地点まで行く(海上)
    go_yaw_onoff(set_speed, 100, 40, set_diving=5)

    # 浮上
    stop()
    up_down(60)
    time.sleep(2)

    my_exit()

# -----------------------------------------------------------------------------

# go_yaw_onoff_iki と go_yaw_onoff_kaeri と yaw_rotを利用したプログラム
def course_ver5(set_speed, set_rot):
    stop()

    # Uターン地点まで行く(海上)
    led_red()
    go_yaw_onoff_iki(30, 250, set_diving=5)
    led_off()

    # Uターン地点まで行く(潜水)
    led_blue()
    go_yaw_onoff_iki(50, 880, set_diving=60)
    led_off()

    # 浮上
    stop()
    led_green()
    up_down(60)
    time.sleep(5)
    stop()
    led_off()

    # Uターン
    # yaw(100, set_diving=False)
    led_purple()
    yaw_rot(20)
    led_off()

    # 所定の深さまで沈む
    diving_while(30)
    # スタート地点まで行く(潜水)
    led_blue()
    go_yaw_onoff_kaeri(30, 800, set_diving=60)
    led_off()

    # スタート地点まで行く(海上)
    led_red()
    go_yaw_onoff_kaeri(30, 400, set_diving=5)
    led_off()

    # 浮上
    stop()
    led_green()
    up_down(60)
    time.sleep(2)

    my_exit()

# -----------------------------------------------------------------------------
