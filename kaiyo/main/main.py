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
from my_course import test, test_rot, test_rot_onoff, course_ver1, course_ver2, course_ver3, course_data_picking, course_ver4, course_ver5
from my_state_write import state_write


# -----------------------------------------------------------------------------


def mode_set():
    # 念のためモーターstop
    stop()
    # センサー初期化
    send_data("reboot")
    # マシンの状態をチェック
    status_check(set_lipoC2=7.0, set_lipoC3S3=11.5)
    # 待機状態のLEDをセット
    led_purple()
    # led_blue()

    # textにlogを残すか？
    log()

    # 動作チェックするか？
    # operation_check()

    # リードスイッチでスタート
    data =  get_data("all")
    # print data
    # スタート動作なし
    # while data["mgs"] == 1:
    # スタート動作あり
    while data["mgs"] == 0:
        data =  get_data("all")
        print data["mgs"]
        print "Ready !!"

    # センサー初期化
    send_data("reboot")
    time.sleep(0.5)
    send_data("reboot")
    time.sleep(0.5)
    send_data("reboot")
    time.sleep(0.5)

    # カウントダウン
    # for cnt in range(3, 0, -1):
    #     led_red()
    #     print cnt
    #     time.sleep(0.5)
    #     led_off()
    #     time.sleep(0.5)

    # センサ初期化で起こるずれを
    # for i in range(20):
    #     data = get_data("all")

    print "Go !!"
    # led_yellow()




def my_main():
    # センサーデータ取得
    data = get_data("all")
    # print get_data("yaw2")
    # print data
    # print data["rot0"]
    # print data["rot1"]
    # print data["rot2"]
    # print data["rot3"]
    # print
    # print data
    # print data["depth"]
    # print data["yaw"]
    # test(30, 9)
    # test_rot(30, 90)
    # test_rot_onoff(30, 90)

    # 波の上
    # course_ver1(30, 900)
    # course_ver1(30, 90)

    # course_ver2(40, 1050)
    # course_ver2(30, 1050)
    # course_data_picking(30, 150)
    # course_ver4(30, 100)
    course_ver5(30, 100)


    # コースに沿ったプログラム
    # course_ver3(30, 200)

    # go_yaw_time(30, 0, 200, set_diving=60)
    # go_yaw_rot(30, 100, 100, set_diving=False)
    # go_yaw_onoff(30, 0, 200, set_diving=False)
    # go_yaw_onoff_iki(30, 200, set_diving=False)
    # go_yaw_onoff_kaeri(30, 200, set_diving=False)
    # go_yaw_onoff_kaeri(10, 50, set_diving=5)
    # yaw_rot(30, set_diving=False)
    # time.sleep(1)


    # yaw(0, set_diving=False)
    # up_down_each(80,0)
    # go_back(20)
    # up_down(20)
    # diving_while(20)
    # diving(90)
    # yaw(0, set_diving=0)


# -------------------------------------------------------------------
if __name__ == '__main__':
    try:
        # 初期設定 and チェック
        # send_data("reboot")
        mode_set()
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
                    my_exit()
            except Exception as e:
                # 予期せぬエラーが発生した時の処理
                # stop()
                # エラーの内容を残す
                state_write(e)
                print "\nError =",e
                print "Error!!!!!!!!!!!!!!!!!!!!!!!"
                for i in range(20):
                    led_green()
                    time.sleep(0.05)
                    led_off()
                    time.sleep(0.05)
                my_exit()

    except KeyboardInterrupt as e:
        print "\nCtrl-c!!"
        # プログラムを終了するときの処理
        my_exit()
