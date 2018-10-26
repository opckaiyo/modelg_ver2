#coding: utf-8
import time
import sys
# sys.path.append("/kaiyo/serial")
sys.path.append("/kaiyo/my_mod")
from my_get_serial import get_data, send_data
from my_motor import go_back, up_down, spinturn, roll, stop, stop_go_back, stop_up_down, br_xr, go_back_each, up_down_each, spinturn_each, spinturn_meca


def t10j(data):
    while True:
        data =  get_data("all")
        print "LY  LX  RY  RX"
        t10j_data = [data["duty0"], data["duty1"], data["duty2"], data["duty3"]]
        print t10j_data
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

        print t10j_map

        # up_down(t10j_map[3])
        if t10j_map[1] == 0:
            # pass
            go_back(t10j_map[0])
        else:
            # pass
            spinturn(t10j_map[1])

    return 0


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
