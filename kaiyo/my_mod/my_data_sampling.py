# -*- coding: utf-8 -*-
# sudo pip install pyserial
import serial
import ast
import time
from datetime import datetime
import sys
sys.path.append("/kaiyo/my_mod")
from my_get_serial import get_data
# -----------------------------------------------------------------------------

# ArduinoMEGAとpinで接続
# ser = serial.Serial('/dev/ttyS0', 115200)
# ArduinoMEGAとUSBケーブル接続
ser = serial.Serial('/dev/ttyACM0', 115200)

# logsをテキストに残すか聞くプログラム
file = open('/kaiyo/log/log_'+str(datetime.now().strftime('%y%m%d_%H%M%S'))+'.txt', 'a')

# -----------------------------------------------------------------------------
#
def data_sampling(set_sample_rate=0.2):
    start_time = time.time()
    while True:
        # Arduino から一行取得
        data = ser.readline()
        try:
            # dictに変換
            data = ast.literal_eval(data)
            # print data
            # サンプリングレート以上時間が経過したら書き込み
            ela_time = time.time() - start_time
            if ela_time >= set_sample_rate:
                text_write(data)
                start_time = time.time()

        except SyntaxError:
            # 受信エラー
            print "Reception Error!!"
            pass


# textにlog書き込み
def text_write(data):
    data["datetime"] = str(datetime.now())
    file.writelines(str(data) + "\n")

# -----------------------------------------------------------------------------

if __name__ == '__main__':
    while True:
        try:
            data_sampling(set_sample_rate=0.2)
        except KeyboardInterrupt as e:
            # print "\nFile close!!\n"
            ser.close()
