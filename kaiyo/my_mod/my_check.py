#coding: utf-8
import time
import sys
sys.path.append("/kaiyo/my_mod")
from my_get_serial import get_data, send_data
from my_motor import go_back, up_down, spinturn, roll, stop, stop_go_back, stop_up_down, br_xr, go_back_each, up_down_each, spinturn_each, spinturn_meca
from my_balance import yaw, go_yaw_time
from my_rc import t10j
from my_gpio import led_red, led_green, led_yellow, led_off

# -------------------------------------------------------------------

# プログラムを終了する手順
def my_exit():
    led_off()
    stop()
    sys.exit()

# 起動前にマシンの状態をチェック
def status_check(set_lipoC2=8, set_lipoC3S3=12):
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



def operation_check():
    while True:
        my_time = 0.002
        print "Do you check the operation? [Y/n]",
        key_in = raw_input()

        if key_in == "y" or key_in == "Y":
            for i in range(100):
                go_back_each(i, 0, 0)
                print i
                time.sleep(my_time)
            for i in range(100):
                go_back_each(0, i, 0)
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
                go_back_each(0, i, 0)
                print i
                time.sleep(my_time)
            for i in range(0, -100, -1):
                go_back_each(i, 0, 0)
                print i
                time.sleep(my_time)

            stop()

            for i in range(0, -100, -1):
                go_back_each(i, i, i)
                up_down_each(i, i)
                print i
                time.sleep(my_time)

            stop()
            print "It worked normally!!"
            return 0

        elif key_in == "n" or key_in == "N":
            print "nnn"
            return 0


# -------------------------------------------------------------------
if __name__ == '__main__':
    operation_check()
