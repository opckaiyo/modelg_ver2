# coding:utf8
from datetime import datetime


def state_write(state):
    file = open('/kaiyo/log/state_log.txt', 'a')
    file.writelines(str(state) + " : " + str(datetime.now()) + "\n")
    file.close()


def motor_write_reset():
    file = open('/kaiyo/log/motor_log.txt', 'w')
    file.writelines("{'interval':0.1}\n")
    file.close()

#
# def motor_write_open(val):
#     file = open('/kaiyo/log/motor_log.txt', 'a')
#     file.writelines("{'interval':0.1}\n")
#
#
# def motor_write(val):
#     file.writelines(str(val) + "\n")
#
#
# def motor_write_close():
#     file.close()



if __name__ == '__main__':
    state_write("浮上")
