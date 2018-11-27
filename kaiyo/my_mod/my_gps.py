#!/usr/bin/env python
# -*- coding: utf-8 -*-

from datetime import datetime
import gps
import ast
from time import sleep



# textにlog書き込み
def text_write(data):
    data["datetime"] = str(datetime.now())
    file.writelines(str(data) + "\n")


# GPSのデータを取得して還す
def get_gps_data():
    # logsをテキストに残すか聞くプログラム
    file = open('/kaiyo/log/gps_log/gps_log_'+str(datetime.now().strftime('%y%m%d_%H%M%S'))+'.txt', 'a')
    session = gps.gps("localhost", "2947")
    session.stream(gps.WATCH_ENABLE | gps.WATCH_NEWSTYLE)
    lat = ""
    lon = ""
    alt = ""
    while True:
        try:
            report = session.next()
            # print report # To see all report data, uncomment the line below
            if report['class'] == 'TPV':
                if hasattr(report, 'lat'):
                    # lat = str(report.lat)
                    lat = float(report.lat)
                if hasattr(report, 'lon'):
                    # lon = str(report.lon)
                    lon = float(report.lon)
                if hasattr(report, 'alt'):
                    # alt = str(report.alt)
                    alt = float(report.alt)

                if( lat!='' and lon!='' and alt!='' ):
                    gps_data_dict = {"lat":lat, "lng":lon, "alt":alt}
                    print gps_data_dict
                    return gps_data_dict
        except KeyError:
                pass
        except KeyboardInterrupt:
                quit()
        except StopIteration:
                session = None
                print "GPSD has terminated!!"




# gps と sensor を結合
def gps_sensor_join():
    # ファイルのパスを指定
    gps_log_file = "/kaiyo/log/gps_log/gps_log_181126_131959.txt"
    sensor_log_file = "/kaiyo/log/sensor_log/sensor_log_181126_131959.txt"
    join_log_file = '/kaiyo/log/join_log/join_log.txt'

    # ファイルを開く
    gps_log_file = open(gps_log_file, 'r')
    sensor_log_file = open(sensor_log_file, 'r')
    join_log_file = open(join_log_file, 'w')

    try:
        # 1行読み込み
        gps_log_data = gps_log_file.readline()
        # str から dictに変換
        gps_log_data = ast.literal_eval(gps_log_data)
        # str から datetime に変換
        gps_log_data["datetime"] = datetime.strptime(gps_log_data["datetime"], '%Y-%m-%d %H:%M:%S.%f')
        while True:
            # 1行読み込み
            sensor_log_data = sensor_log_file.readline()
            # str から dictに変換
            sensor_log_data = ast.literal_eval(sensor_log_data)
            # str から datetime に変換
            sensor_log_data["datetime"] = datetime.strptime(sensor_log_data["datetime"], '%Y-%m-%d %H:%M:%S.%f')

            # dict 生成
            join_log_data = sensor_log_data

            if gps_log_data["datetime"] > sensor_log_data["datetime"]:
                # dict から str に変換
                join_log_data["datetime"] = str(join_log_data["datetime"])

                # GPS のデータを追加
                join_log_data["lat"] = float(gps_log_data["lat"])
                join_log_data["lng"] = float(gps_log_data["lng"])
                join_log_data["alt"] = float(gps_log_data["alt"])
                # テキストに書き込み
                join_log_file.writelines(str(join_log_data) + "\n")
            else:
                # 1行読み込み
                gps_log_data = gps_log_file.readline()
                # str から dictに変換
                gps_log_data = ast.literal_eval(gps_log_data)
                # str から datetime に変換
                gps_log_data["datetime"] = datetime.strptime(gps_log_data["datetime"], '%Y-%m-%d %H:%M:%S.%f')

                # dict から str に変換
                join_log_data["datetime"] = str(join_log_data["datetime"])

                # GPS のデータを追加
                join_log_data["lat"] = float(gps_log_data["lat"])
                join_log_data["lng"] = float(gps_log_data["lng"])
                join_log_data["alt"] = float(gps_log_data["alt"])
                # テキストに書き込み
                join_log_file.writelines(str(join_log_data) + "\n")

    except Exception as e:
        # ファイルを閉じる
        gps_log_file.close()
        sensor_log_file.close()
        join_log_file.close()
        print "END!!"



if __name__ == '__main__':
    gps_sensor_join()
    # while True:
    #     data = get_gps_data()
    #     data["datetime"] = str(datetime.now())
    #     file.writelines(str(data) + "\n")
