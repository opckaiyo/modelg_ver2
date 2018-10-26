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


def test_rot_onoff(set_speed, set_rot):
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
    # go_yaw_rot(set_speed, 0, set_rot)
    go_yaw_onoff(set_speed, 0, set_rot, set_diving=80)

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
    # go_yaw_rot(set_speed, 100, set_rot)
    go_yaw_onoff(set_speed, 100, set_rot, set_diving=80)


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


    # Uターン
    print "yaw"
    led_red()
    yaw(0, set_diving=False)

    stop()


# -----------------------------------------------------------------------------


def course_ver1(set_speed, set_rot):
    stop()

    # 浮上
    state_write("up")
    print "up"
    # diving_while(20)
    up_down(80)
    time.sleep(3)
    yaw(0, set_diving=False)

    # Uターン地点まで行く
    state_write("go_yaw")
    print "go_yaw"
    led_green()
    go_yaw_rot(set_speed, 0, set_rot, set_diving=60)
    # go_yaw_rot(set_speed, 0, set_rot, set_diving=False)

    # 慣性で流れるのを停止
    state_write("stop U")
    stop()
    led_off()
    time.sleep(0.5)
    go_back(-20)
    time.sleep(1)
    stop()

    # 浮上
    state_write("up")
    print "up"
    # diving_while(20)
    up_down(60)
    time.sleep(4)

    # Uターンの補助
    spinturn(30)
    time.sleep(1)
    stop()

    # Uターン
    state_write("yaw")
    print "yaw"
    yaw(100, set_diving=False)
    led_red()
    time.sleep(0.5)
    print "yaw"
    yaw(100, set_diving=False)

    # スタート地点まで行く
    state_write("go_yaw")
    print "go_yaw"
    led_green()
    go_yaw_rot(set_speed, 100, set_rot, set_diving=60)
    # go_yaw_rot(set_speed, 100, set_rot, set_diving=False)


    # 慣性で流れるのを停止
    stop()
    led_off()
    time.sleep(0.5)
    go_back(-20)
    time.sleep(1)
    stop()

    # 浮上
    state_write("up")
    print "up"
    led_off()
    # diving_while(20)
    up_down(80)
    time.sleep(3)


    state_write("end")
    stop()


# -----------------------------------------------------------------------------

def course_ver2(set_speed, set_rot):
    state_write("\ncourse_ver2 START")
    stop()

    yaw(0, set_diving=False)

    # Uターン地点まで行く(海上)
    print "go_yaw"
    state_write("kaijou")
    led_off()
    led_blue()
    # go_yaw_rot(set_speed, 0, 300, set_diving=5)
    go_yaw_onoff(set_speed, 0, 50, set_diving=5)
    led_off()

    # Uターン地点まで行く(潜水)
    print "go_yaw"
    state_write("sennsui")
    led_green()
    # go_yaw_rot(set_speed, 0, set_rot, set_diving=80)
    go_yaw_onoff(set_speed, 0, 50, set_diving=80)
    led_off()

    # 慣性で流れるのを停止
    stop()
    time.sleep(0.5)
    go_back(-20)
    time.sleep(1)
    stop()

    # 浮上
    print "up"
    state_write("up")
    # diving_while(20)
    led_lihtblue()
    up_down(60)
    time.sleep(4)
    led_off()

    led_yellow()

    # Uターン
    print "yaw"
    state_write("yaw")
    # yaw(100, set_diving=1)
    yaw(100, set_diving=False)

    # スタート地点まで行く(潜水)
    print "go_yaw"
    state_write("sennsui")
    led_green()
    # go_yaw_rot(set_speed, 100, set_rot)
    # go_yaw_rot(set_speed, 100, set_rot, set_diving=80)
    go_yaw_onoff(set_speed, 100, 60, set_diving=80)
    led_off()

    # スタート地点まで行く(海上)
    print "go_yaw"
    state_write("kaiyo")
    led_blue()
    # go_yaw_rot(set_speed, 100, set_rot)
    # go_yaw_rot(set_speed, 100, 300, set_diving=5)
    # 回転数を調整
    go_yaw_onoff(set_speed, 100, 50, set_diving=5)
    led_off()

    # 慣性で流れるのを停止
    stop()
    time.sleep(0.5)
    go_back(-20)
    time.sleep(1)
    stop()

    # 浮上
    print "up"
    state_write("up")
    led_off()
    # diving_while(20)
    up_down(60)
    time.sleep(4)

    led_yellow()

    state_write("END")
    stop()

    my_exit()


"""
# 宜野湾漁港でうまく動いたパラメータ
def course_ver2(set_speed, set_rot):
    state_write("\ncourse_ver2 START")
    stop()

    # 浮上
    print "up"
    state_write("up")
    # diving_while(20)
    # yaw(0, set_diving=1)
    up_down(80)
    time.sleep(3)
    stop()
    yaw(0, set_diving=False)

    # Uターン地点まで行く(海上)
    print "go_yaw"
    state_write("kaijou")
    led_red()
    # go_yaw_rot(set_speed, 0, 300, set_diving=5)
    go_yaw_onoff(set_speed, 0, 300, set_diving=5)
    led_off()

    # Uターン地点まで行く(潜水)
    print "go_yaw"
    state_write("sennsui")
    led_green()
    # go_yaw_rot(set_speed, 0, set_rot, set_diving=80)
    go_yaw_onoff(set_speed, 0, set_rot, set_diving=80)
    led_off()

    # 慣性で流れるのを停止
    stop()
    time.sleep(0.5)
    go_back(-20)
    time.sleep(1)
    stop()

    # 浮上
    print "up"
    state_write("up")
    # diving_while(20)
    up_down(60)
    time.sleep(4)

    # Uターン
    print "yaw"
    state_write("yaw")
    # yaw(100, set_diving=1)
    yaw(100, set_diving=False)

    # スタート地点まで行く(潜水)
    print "go_yaw"
    state_write("sennsui")
    led_green()
    # go_yaw_rot(set_speed, 100, set_rot)
    # go_yaw_rot(set_speed, 100, set_rot, set_diving=80)
    go_yaw_onoff(set_speed, 100, 850, set_diving=80)
    led_off()

    # スタート地点まで行く(海上)
    print "go_yaw"
    state_write("go_yaw")
    led_red()
    # go_yaw_rot(set_speed, 100, set_rot)
    # go_yaw_rot(set_speed, 100, 300, set_diving=5)
    # 回転数を調整
    go_yaw_onoff(set_speed, 100, 400, set_diving=5)
    led_off()

    # 慣性で流れるのを停止
    stop()
    time.sleep(0.5)
    go_back(-20)
    time.sleep(1)
    stop()

    # 浮上
    print "up"
    state_write("up")
    led_off()
    # diving_while(20)
    up_down(60)
    time.sleep(4)

    state_write("END")
    stop()

    my_exit()
"""

# -----------------------------------------------------------------------------


def course_ver3(set_speed, set_rot):
    state_write("\ncourse_ver3 START")
    stop()

    # 浮上
    diving_while(10)
    yaw(0, set_diving=10)

    # 海上航行
    led_red()
    go_yaw_rot(set_speed, 0, 100, set_diving=10)
    led_off()

    stop()
    diving_while(40)

    # Uターン地点まで行く
    led_green()
    go_yaw_rot(set_speed, 0, 200, set_diving=60)
    led_off()

    # 慣性で流れるのを停止
    stop()
    time.sleep(0.5)
    go_back(-20)
    time.sleep(1)
    stop()

    # 浮上してUターン
    diving_while(10)
    yaw(100, set_diving=20)

    # スタート地点まで行く
    led_green()
    go_yaw_rot(set_speed, 100, 100, set_diving=60)
    led_off()

    stop()
    diving_while(10)

    # 海上航行
    led_red()
    go_yaw_rot(set_speed, 100, 200, set_diving=10)
    led_off()

    # 慣性で流れるのを停止
    stop()
    time.sleep(0.5)
    go_back(-20)
    time.sleep(1)
    stop()

    # 浮上
    diving_while(10)

    stop()

    my_exit()

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

def course_data_picking(set_speed, set_rot):
    stop()

    # 浮上
    print "up"
    # diving_while(20)
    # yaw(0, set_diving=1)
    up_down(60)
    time.sleep(3)
    # yaw(0, set_diving=False)

    # Uターン地点まで行く
    print "go_yaw"
    led_green()
    go_yaw_rot(set_speed, 0, set_rot, set_diving=5)
    led_off()

    stop_go_back()

    # 慣性で流れるのを停止
    stop()
    time.sleep(0.5)
    go_back(-20)
    time.sleep(1)
    stop()

    yaw(0, set_diving=False)


    print "go_yaw"
    led_green()
    go_yaw_rot(set_speed, 100, set_rot, set_diving=5)
    led_off()

    stop()

    my_exit()
