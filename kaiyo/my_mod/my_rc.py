#coding: utf-8
import time
import sys
# sys.path.append("/kaiyo/serial")
sys.path.append("/kaiyo/my_mod")
from my_get_serial import get_data, send_data
from my_motor_teaching import go_back, up_down, spinturn, roll, stop, stop_go_back, stop_up_down, br_xr, go_back_each, up_down_each, spinturn_each, spinturn_meca, pump
from my_motor import br_xr, br_xl, dc_xr, dc_xl, dc_yr, dc_yl, dc_u, pump
# from my_motor import go_back, up_down, spinturn, roll, stop, stop_go_back, stop_up_down, br_xr, go_back_each, up_down_each, spinturn_each, spinturn_meca
# from my_motor_teaching import go_back, up_down, spinturn, roll, stop, stop_go_back, stop_up_down, br_xr, go_back_each, up_down_each, spinturn_each, spinturn_meca, pump


def t10j_map_data():
    data =  get_data("all")
    # print "LY  LX  RY  RX"
    t10j_data = [data["duty2"], data["duty0"], data["duty1"], data["duty3"]]
    # print t10j_data

    t10j_map = []
    for val in t10j_data:
        in_min = 1104
        in_max = 1918
        out_min = -100
        out_max = 100
        val = (val - in_min) * (out_max - out_min) / (in_max - in_min) + out_min
        if val < -100: val = -100
        if val > 100: val = 100
        if val <= 10 and val >= -10: val = 0
        t10j_map.append(val)

    t10j_map = {"ly":t10j_map[0],"lx":t10j_map[1],"ry":t10j_map[2],"rx":t10j_map[3]}
    # print t10j_map
    return t10j_map


def t10j_start_check():
    while True:
        t10j_map = t10j_map_data()
        print "RY joystick upper!!"
        # if 100 == t10j_map["ly"] and t10j_map["lx"] and t10j_map["ry"] and t10j_map["rx"]:
        if 100 == t10j_map["ry"]:
            while True:
                t10j_map = t10j_map_data()
                print "RY joystick center!!"
                if 0 == t10j_map["ry"]:
                    while True:
                        print "Joysticks OK!!"
                        return 0


def t10j():
    t10j_start_check()
    while True:

        t10j_map = t10j_map_data()
        print t10j_map

        up_down(t10j_map["ry"])

        xr = t10j_map["ly"]
        xl = t10j_map["ly"]

        dc_xr(xr)
        dc_xl(xl)
        dc_yr = 0
        dc_yl = 0

    return 0


# -------------------------------------------------------------------

def t10j_time(set_time=10):
    # ジョイスティックの位置を正す
    t10j_start_check()
    # カウントダウン
    for cnt in range(3, 0, -1):
        # led_red()
        print cnt
        time.sleep(0.5)
        # led_off()
        time.sleep(0.5)

    start_time = time.time()
    while True:

        t10j_map = t10j_map_data()

        up_down(t10j_map["ry"])
        if t10j_map["lx"] == 0:
            go_back(t10j_map["ly"])
        else:
            spinturn(t10j_map["lx"])

        ela_time = time.time() - start_time
        print ela_time
        if ela_time >= set_time:
            stop()
            break


# -------------------------------------------------------------------

if __name__ == '__main__':
    try:
        ini_val = get_data("yaw")
        # センサー初期化
        send_data("reboot")
        while True:
            # data =  get_data("all")

            # プロポで操作
            t10j()





        stop()

    except KeyboardInterrupt as e:
        stop() #Ctrl + Cを押したときの処理
