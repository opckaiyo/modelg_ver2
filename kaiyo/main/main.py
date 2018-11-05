#coding: utf-8
import time
import sys
# 自作関数のインポート
sys.path.append("/kaiyo/my_mod")
from my_get_serial import get_data, send_data, log
from my_motor import go_back, up_down, spinturn, roll, stop, stop_go_back, stop_up_down, br_xr, go_back_each, up_down_each, spinturn_each, spinturn_meca, pump
from my_balance import yaw, go_yaw_time, go_yaw_rot, diving, diving_while, go_yaw_onoff, go_yaw_onoff_iki, go_yaw_onoff_kaeri, yaw_rot, pitch
from my_rc import t10j, t10j_time
from my_check import operation_check, battery_check, my_exit, first_action
from my_gpio import led_red, led_green, led_yellow, led_off, led_blue, led_purple, led_lihtblue
from my_course import course_convention
from my_state_write import state_write
from my_teaching import teaching_set, teaching_in, teaching_out


# -----------------------------------------------------------------------------


def my_main():
    # センサーデータ取得
    data = get_data("all")
    print data["rot0"],data["rot1"],data["rot2"],data["rot3"]
    go_back_each(r=30,l=0)
    up_down_each(r=30,l=0)

    # teaching_in()
    # teaching_out()
    # teaching_set()
    # t10j()

    # 本番
    # course_convention()


# -------------------------------------------------------------------


if __name__ == '__main__':
    try:
        # 初期設定 and チェック
        # send_data("reboot")
        # mode_set()
        first_action(set_send_reboot=True, set_battery_check=True, set_log=False, set_operation_check=True, set_start_mgs=False, set_send_pwm=False, set_countdown=0)
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
