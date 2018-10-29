#coding: utf-8
import time
import sys
# sys.path.append("/kaiyo/serial")
sys.path.append("/kaiyo/my_mod")
from my_get_serial import get_data, send_data
# from my_motor import go_back, up_down, spinturn, roll, stop, stop_go_back, stop_up_down, br_xr, go_back_each, up_down_each, spinturn_each, spinturn_meca
from my_teaching_motor import go_back, up_down, spinturn, roll, stop, stop_go_back, stop_up_down, br_xr, go_back_each, up_down_each, spinturn_each, spinturn_meca, pump


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
        print "All joysticks upper right!!"
        if 100 == t10j_map["ly"] and t10j_map["lx"] and t10j_map["ry"] and t10j_map["rx"]:
            while True:
                t10j_map = t10j_map_data()
                print "All joysticks center!!"
                if 0 == t10j_map["ry"]:
                    while True:
                        print "Joysticks OK!!"
                        return 0


def t10j():
    t10j_start_check()
    while True:

        t10j_map = t10j_map_data()

        up_down(t10j_map["ry"])
        if t10j_map["lx"] == 0:
            go_back(t10j_map["ly"])
        else:
            spinturn(t10j_map["lx"])

    return 0


# -------------------------------------------------------------------

def t10j_time(set_time=10):
    t10j_start_check()
    old_time = time.time()
    while True:

        t10j_map = t10j_map_data()

        up_down(t10j_map["ry"])
        if t10j_map["lx"] == 0:
            go_back(t10j_map["ly"])
        else:
            spinturn(t10j_map["lx"])

        ela_time = time.time() - old_time
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
            data =  get_data("all")

            # プロポで操作
            t10j(data)





        stop()

    except KeyboardInterrupt as e:
        stop() #Ctrl + Cを押したときの処理
