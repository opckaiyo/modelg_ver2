#!/usr/bin/env python
# -*- coding: utf-8 -*-

from datetime import datetime
import gps


# logsをテキストに残すか聞くプログラム
file = open('/kaiyo/log/gps_log/gps_log_'+str(datetime.now().strftime('%y%m%d_%H%M%S'))+'.txt', 'a')

# textにlog書き込み
def text_write(data):
    data["datetime"] = str(datetime.now())
    file.writelines(str(data) + "\n")

# GPSのデータを取得して還す
def get_gps_data():
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
                print "GPSD has terminated"


if __name__ == '__main__':
    while True:
        text_write(get_gps_data())
