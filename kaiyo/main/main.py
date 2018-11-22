#coding: utf-8
from time import sleep
import sys
# 自作関数のインポート
sys.path.append("/kaiyo/my_mod")
from my_get_serial import get_data, send_data
from my_motor import go_back, up_down, spinturn, roll, stop, stop_go_back, stop_up_down, br_xr, go_back_each, up_down_each, spinturn_each, spinturn_meca, pump
from my_balance import yaw, go_yaw_time, go_yaw_rot, diving, diving_while, go_yaw_onoff, go_yaw_onoff_iki, go_yaw_onoff_kaeri, yaw_rot, pitch
from my_rc import t10j, t10j_time, t10j_mode_sumo
from my_check import operation_check, battery_check, my_exit, first_action
from my_gpio import led_red, led_green, led_yellow, led_off, led_blue, led_purple, led_lihtblue
from my_course import course_convention
from my_text_write import error_log_write
from my_teaching import teaching_set, teaching_in, teaching_out


# -----------------------------------------------------------------------------


def my_main():
    # センサーデータ取得
    data = get_data("all")
    print data

    # teaching_in()
    # teaching_out()
    # teaching_set()
    # t10j_mode_sumo()
    # t10j(set_time=10)

    # print "aaa"
    # go_back(50)

    # yaw(set_angle=0, set_diving=0)

    # 本番
    # course_convention()


# -------------------------------------------------------------------

if __name__ == '__main__':
    try:
        # 初期動作設定
        set_send_reboot = True
        set_battery_check = True
        set_log = False
        set_operation_check = False
        set_start_mgs = False
        set_send_pwm = False
        set_countdown = 0
        first_action(set_send_reboot, set_battery_check, set_log, set_operation_check, set_start_mgs, set_send_pwm, set_countdown)
        # t10jを使うとき
        # first_action(set_send_reboot=True, set_battery_check=True, set_log=True, set_operation_check=False, set_start_mgs=False, set_send_pwm=True, set_countdown=0)
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
                stop()
                # エラーの内容を残す
                error_log_write(e)
                # print "\nError =",e
                # print "Error!!!!!!!!!!!!!!!!!!!!!!!"
                # for i in range(20):
                #     led_green()
                #     time.sleep(0.05)
                #     led_off()
                #     time.sleep(0.05)
                # my_exit()

    except KeyboardInterrupt as e:
        print "\nCtrl-c!!"
        # プログラムを終了するときの処理
        my_exit()
