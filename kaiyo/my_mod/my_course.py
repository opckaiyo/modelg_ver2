#coding: utf-8
import time
import sys
# マルチタスク
sys.path.append("/kaiyo/my_mod")
from my_get_serial import get_data, send_data
from my_motor import go_back, up_down, spinturn, roll, stop, stop_go_back, stop_up_down, br_xr, go_back_each, up_down_each, spinturn_each
from my_balance import yaw, go_yaw_time, go_yaw_rot, diving, diving_while, go_yaw_onoff, go_yaw_onoff_iki, go_yaw_onoff_kaeri, yaw_rot
from my_rc import t10j
from my_check import operation_check, battery_check, my_exit
from my_gpio import led_red, led_green, led_yellow, led_off, led_blue, led_purple, led_lihtblue
from my_text_write import error_log_write
from my_waypoint import waypoint

# -----------------------------------------------------------------------------


# 大会で100点とったパラメータ
def course_convention():
    stop()

    # Uターン地点まで行く(海上)
    led_red()
    go_yaw_onoff_iki(set_speed=30, set_rot=250, set_diving=5)
    led_off()

    # Uターン地点まで行く(潜水)
    led_blue()
    go_yaw_onoff_iki(set_speed=50, set_rot=880, set_diving=60)
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
    yaw_rot(set_rot=20, set_diving=True)
    led_off()

    # 所定の深さまで沈む
    diving_while(30)

    # スタート地点まで行く(潜水)
    led_blue()
    go_yaw_onoff_kaeri(set_speed=30, set_rot=800, set_diving=60)
    led_off()

    # スタート地点まで行く(海上)
    led_red()
    go_yaw_onoff_kaeri(set_speed=30, set_rot=400, set_diving=5)
    led_off()

    # 浮上
    stop()
    led_green()
    up_down(60)
    time.sleep(2)

    my_exit()

# -----------------------------------------------------------------------------



def course_pool():
    stop()

    # Uターン地点まで行く(海上)
    led_red()
    go_yaw_onoff_iki(set_speed=30, set_rot=400, set_diving=80)
    # go_yaw_onoff_iki(set_speed=30, set_rot=200, set_diving=5)
    led_off()

    # Uターン地点まで行く(潜水)
    # led_blue()
    # go_yaw_onoff_iki(set_speed=30, set_rot=200, set_diving=60)
    # led_off()

    # 浮上
    stop()
    led_green()
    up_down(60)
    time.sleep(5)
    stop()
    led_off()

    # 設定地点まで自動で移動
    waypoint_data = {1:{'lat': 26.377735, 'lng': 127.822441667}}
    waypoint(waypoint_data = waypoint_data)
    print "aaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa"

    # # Uターン
    # # yaw(100, set_diving=False)
    # led_purple()
    # yaw_rot(set_rot=30, set_diving=True)
    # led_off()

    # 所定の深さまで沈む
    diving_while(30)

    # スタート地点まで行く(潜水)
    led_blue()
    go_yaw_onoff_kaeri(set_speed=30, set_rot=420, set_diving=80)
    # go_yaw_onoff_kaeri(set_speed=30, set_rot=210, set_diving=80)
    led_off()

    # スタート地点まで行く(海上)
    # led_red()
    # go_yaw_onoff_kaeri(set_speed=30, set_rot=200, set_diving=5)
    # led_off()

    # 浮上
    stop()
    led_green()
    up_down(60)
    time.sleep(2)

    my_exit()

# -----------------------------------------------------------------------------

def auv():

    #パラメーター----------------------------

    #競技スタート位置を入力
    start_lat =
    start_lng =

    #潜水地点を入力
    diving_lat =
    diving_lng =

    #目的の水深
    depth =

    #パラメーター----------------------------


    #競技スタート位置に移動-------------------

    #現在の向き取得
    now_gps_data = get_gps_data()
    now_lat = now_gps_data["ex"]

    #direction:向き, distance:距離, set_rot:距離を元にスラスタ回転数計算
    direction, distance, set_rot = get_direction_distance(start_lat,start_lng)

    #左回り、右回りどちらが早いか計算
    now_lot = now_lot - (int(now_lot / 90) * 90)
    direction = direction - (int(now_lot / 90) * 90)

    if (direction < 0):
        direction = abs(direction) + 180

    #回転
    while
    spinturn(direction)

    #スラスタ回転数を指定し前進
    go_back(set_rot)

    #競技スタート位置に移動-------------------


    #潜水位置へ移動--------------------------

    #現在の向き取得
    now_gps_data = get_gps_data()
    now_lat = now_gps_data["ex"]

    #direction:向き, distance:距離, set_rot:距離を元にスラスタ回転数計算
    direction, distance, set_rot = get_direction_distance(start_lat,start_lng)

    #左回り、右回りどちらが早いか計算
    now_lot = now_lot - (int(now_lot / 90) * 90)
    direction = direction - (int(now_lot / 90) * 90)

    if (direction < 0):
        direction = abs(direction) + 180

    #回転
    spinturn(direction)

    #スラスタ回転数を指定し前進
    go_back(set_rot)

    #潜水位置へ移動--------------------------


    #目的水深まで潜水------------------------

    now_gps_data = get_gps_data()
    depth = now_gps_data["depth"]



    #目的水深まで潜水------------------------

# -----------------------------------------------------------------------------
