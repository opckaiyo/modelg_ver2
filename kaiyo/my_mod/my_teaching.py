# -*- coding: utf-8 -*-
import ast
import time

import sys
sys.path.append("/kaiyo/my_mod")
# from my_teaching_motor import go_back, up_down, spinturn, roll, stop, stop_go_back, stop_up_down, br_xr, go_back_each, up_down_each, spinturn_each, spinturn_meca, pump
from my_motor import br_xr, br_xl, dc_xr, dc_xl, dc_yr, dc_yl, dc_u, pump
from my_rc import t10j, t10j_time
from my_gpio import led_red, led_green, led_yellow, led_off, led_blue, led_purple, led_lihtblue
from my_check import operation_check, status_check, my_exit
from my_state_write import state_write, motor_write, motor_write_close


#------------------------------------------------------------------------------


def get_log():
    print "\nHow many seconds do you teaching? :",
    key_in = raw_input()
    t10j_time(set_time=int(key_in))
    motor_write_close()

    # 動作させますか?
    print "\nDoes it work? [Y/n] :",
    key_in = raw_input()
    while True:
        if key_in == "y" or key_in == "Y":
            # カウントダウン
            for cnt in range(3, 0, -1):
                led_red()
                print cnt
                time.sleep(0.5)
                led_off()
                time.sleep(0.5)

            break
        elif key_in == "n" or key_in == "N":
            my_exit()




def teaching_in():
    print "\nHow many seconds do you teaching? :",
    key_in = raw_input()
    t10j_time(set_time=int(key_in))
    motor_write_close()


def teaching_out():
    # 動作開始
    file_name = "/kaiyo/log/motor_log.txt"
    file = open(file_name, 'r')
    data = file.readline()

    # インターバルを取得
    interval = ast.literal_eval(data)
    interval = interval["interval"]

    while data:
        data = file.readline()
        # データがあれば辞書型に変換
        if data:
            data = ast.literal_eval(data)
            print data

            dc_xr(data["dc_xr"])
            dc_xl(data["dc_xl"])
            dc_yr(data["dc_yr"])
            dc_yl(data["dc_yl"])

        # 実行インターバル
        time.sleep(interval)

    my_exit()

if __name__ == '__main__':
    # get_log()
    teaching_in()
    # teaching_out()
