#coding: utf-8
from time import sleep
import sys
# 自作関数のインポート
sys.path.append("/kaiyo/my_mod")
from my_get_serial import get_data, send_data
from my_motor import go_back, up_down, spinturn, roll, stop, stop_go_back, stop_up_down, br_xr, go_back_each, up_down_each, spinturn_each, solenoid_on, solenoid_off
from my_balance import yaw, go_yaw, go_yaw_time, go_yaw_rot, diving, diving_while, go_yaw_onoff, go_yaw_onoff_iki, go_yaw_onoff_kaeri, yaw_rot, compass, go_compass_onoff
from my_rc import t10j, t10j_time, t10j_mode_sumo
from my_check import operation_check, battery_check, my_exit, first_action
from my_gpio import led_red, led_green, led_yellow, led_off, led_blue, led_purple, led_lihtblue
from my_course import course_convention, course_pool
from my_text_write import error_log_write
from my_gps import gps_sensor_join_data
from my_waypoint import waypoint, pad_rc_route_data_creation
from my_gamepad import pad_rc

# -----------------------------------------------------------------------------


def my_main():
    # センサーデータ取得
    data = get_data("all")
    # print data
    # print "rot0",data["rot0"]
    # print "rot1",data["rot1"]
    # print "rot2",data["rot2"]
    # print "rot3",data["rot3"]
    # print "flw0", data["flw0"]
    # print "flw1", data["flw1"]
    # print "flw2", data["flw2"]
    # print "flw3", data["flw3"]
    # print

    go_back(80)
    # up_down(20)

    # pad_rc_route_data_creation()
    # compass(set_angle=0, set_diving=False)
    # pad_rc()

    # sleep(5)
    # waypoint_data = {1:{'lat': 26.377735, 'lng': 127.822441667}}
    # waypoint(waypoint_data = waypoint_data)
    # print "aaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa"


    # print data["compass"],
    # print data["yaw"]

    # yaw(set_angle=0, set_diving=False)
    # go_yaw_time(set_speed=50, set_angle=0, set_time=100, set_diving=False)
    # compass(set_angle=0, set_diving=False)
    # go_compass_onoff(set_speed=30, set_angle=0, set_rot=100, set_diving=True)
    # go_yaw(set_speed=30, set_angle=0, set_rot=100, set_time=False, set_diving=True)
    # go_yaw_rot(set_speed=30, set_angle=0, set_rot=10000, set_diving=True)
    # go_yaw_onoff(set_speed=30, set_angle=0, set_rot=100, set_diving=True)


    # course_pool()

    # t10j_mode_sumo()
    # t10j(set_time=10)

    # 本番
    # course_convention()


# -------------------------------------------------------------------


if __name__ == '__main__':
    try:
        # モードなどの設定
        first_action()

        while True:
            # 予期せぬエラーが発生した時の処理
            try:
                # Ctrl-cを押したときの処理
                try:
                    # メインのプログラム
                    # ----------------------------------------
                    my_main()
                    # my_exit()
                    # break
                    # ----------------------------------------
                except KeyboardInterrupt as e:
                    # Ctrl-cを押したときの処理
                    print "\nCtrl-c!!"
                    # プログラムを終了したらデータを作成
                    gps_sensor_join_data()
                    # print e
                    my_exit()
            except Exception as e:
                # 予期せぬエラーが発生した時の処理
                stop()
                # エラーの内容を残す
                error_log_write(e)
                print "\nError =",e
                print "Error!!!!!!!!!!!!!!!!!!!!!!!"
                for i in range(20):
                    led_green()
                    sleep(0.05)
                    led_off()
                    sleep(0.05)
                # my_exit()

    except KeyboardInterrupt as e:
        print "\nCtrl-c!!"
        # プログラムを終了するときの処理
        my_exit()
