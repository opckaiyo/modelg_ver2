#coding: utf-8
import time
# import signal
import sys
import subprocess
sys.path.append("/kaiyo/my_mod")
from my_get_serial import get_data, send_data
from my_motor import go_back, up_down, spinturn, roll, stop, stop_go_back, stop_up_down, br_xr, go_back_each, up_down_each, spinturn_each, spinturn_meca
from my_balance import yaw, go_yaw_time
from my_rc import t10j
from my_gpio import led_red, led_green, led_yellow, led_off, led_blue, led_purple, led_lihtblue
from my_voice import jtalk

# -------------------------------------------------------------------

# プログラムを終了する手順
def my_exit():
    led_off()
    stop()
    sys.exit()

# 起動前にマシンの状態をチェック
def battery_check(set_lipoC2=8, set_lipoC3S3=12):
    data = get_data("all")
    print
    print "----------------------------------"
    print "Status checking!!"
    time.sleep(1)


    print "Lipo checking!!"


    if data["lipoC2"] <= set_lipoC2 or data["lipoC3S3"] <= set_lipoC3S3:
        if data["lipoC2"] == 0 or data["lipoC3S3"] == 0:
            if data["lipoC2"] == 0:
                print "lipoC2 : No connection!!"
            if data["lipoC3S3"] == 0:
                print "lipoC3S3 : No connection!!"
        else:
            while True:
                if data["lipoC2"] <= set_lipoC2:
                    print "lipoC2 : "+str(get_data("lipoC2"))+"[V]"
                if data["lipoC3S3"] <= set_lipoC3S3:
                    print "lipoC3S3 : "+str(get_data("lipoC3S3"))+"[V]"

                print "Lipo Low!!"
                led_red()
                time.sleep(0.1)
                led_off()
                time.sleep(0.1)

    print "lipoC2 : "+str(get_data("lipoC2"))+"[V]"
    print "lipoC3S3 : "+str(get_data("lipoC3S3"))+"[V]"
    print "Status okay!!"
    print "----------------------------------"
    print


# 動作確認
def operation_check():
    while True:
        my_time = 0.002
        print "Do you check the operation? [Y/n]",
        key_in = raw_input()

        if key_in == "y" or key_in == "Y":
            for i in range(100):
                go_back_each(i, 0)
                print i
                time.sleep(my_time)
            for i in range(100):
                go_back_each(0, i)
                print i
                time.sleep(my_time)


            stop()


            for i in range(100):
                up_down_each(0, i)
                print i
                time.sleep(my_time)
            for i in range(100):
                up_down_each(i, 0)
                print i
                time.sleep(my_time)


            stop()


            for i in range(0, -100, -1):
                up_down_each(i, 0)
                print i
                time.sleep(my_time)
            for i in range(0, -100, -1):
                up_down_each(0, i)
                print i
                time.sleep(my_time)


            stop()


            for i in range(0, -100, -1):
                go_back_each(0, i)
                print i
                time.sleep(my_time)
            for i in range(0, -100, -1):
                go_back_each(i, 0)
                print i
                time.sleep(my_time)


            stop()


            for i in range(0, -100, -1):
                go_back_each(i, i)
                up_down_each(i, i)
                print i
                time.sleep(my_time)


            stop()


            for i in range(0, 100, 1):
                go_back_each(i, i)
                up_down_each(i, i)
                print i
                time.sleep(my_time)

            stop()
            print "It worked normally!!"
            return 0

        elif key_in == "n" or key_in == "N":
            print "nnn"
            return 0


# 取得した値を読み上げ
def voice_check(val):
    # print get_data("all")
    data = get_data("all")
    print data[val]
    # voice_text = "角度"+str(data[val])
    # print voice_text
    # # jtalk(file_name="a", voice=str(voice_text))
    time.sleep(1)


# 最初の動作
def first_action(set_send_reboot=True, set_battery_check=True, set_log=True, set_operation_check=False, set_start_mgs=True, set_send_pwm=False, set_countdown=True):
    print
    print "----------------------------------"
    print "set_send_reboot :", set_send_reboot
    print "set_battery_check :", set_battery_check
    print "set_log :", set_log
    print "set_operation_check :", set_operation_check
    print "set_start_mgs :", set_operation_check
    print "set_send_pwm :", set_send_pwm
    print "set_countdown :", set_countdown
    print "----------------------------------"

    # 念のためモーターstop
    stop()

    if set_send_reboot:
        # センサー初期化
        send_data("reboot")

    if set_battery_check:
        # マシンの状態をチェック
        battery_check(set_lipoC2=7.0, set_lipoC3S3=11)

    # 待機状態のLEDをセット
    led_purple()


    if set_operation_check:
        # 動作チェックするか？
        operation_check()

    if set_start_mgs:
        # リードスイッチでスタート
        data =  get_data("all")

        # スタート動作なし
        # while data["mgs"] == 1:
        # スタート動作あり
        while data["mgs"] == 0:
            data =  get_data("all")
            print data["mgs"]
            print "Ready !!"

    print "\nPlease wait!!"
    # センサー初期化
    send_data("reboot")
    time.sleep(0.5)
    # send_data("reboot")
    # time.sleep(0.5)
    # send_data("reboot")
    # time.sleep(0.5)

    if set_send_pwm:
        # プロポ受信モード
        send_data("pwm on")

        # センサを安定状態にするため
        for i in range(20):
            data = get_data("all")

    if set_log:
        # textにlogを残すか？
        cmd = "python /kaiyo/my_mod/my_data_sampling.py"
        subprocess.Popen(cmd.split())
        # subprocess.call(cmd.split())


    if set_countdown:
        # カウントダウン
        for cnt in range(set_countdown, 0, -1):
            led_red()
            print cnt
            time.sleep(0.5)
            led_off()
            time.sleep(0.5)

        print "Go !!"




# -------------------------------------------------------------------
if __name__ == '__main__':
    # operation_check()


    while True:
        # send_data("reboot")
        try:
            voice_check("yaw")

            # go_back(50)
            # up_down(20)
            # go_back_each(10,10)
            # dc_u( 100 )
        except KeyboardInterrupt as e:
            stop()
            break
