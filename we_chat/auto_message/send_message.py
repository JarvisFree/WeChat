#!/usr/bin/env python
# -*- coding: utf-8 -*-

"""
@Time    ：2021/6/19 14:45
@Author  ：维斯
@File    ：send_message.py
@Version ：1.0
@Function：在当前窗口自动发送消息
"""

import random
import time

import pyperclip
from pymouse import *
from pykeyboard import PyKeyboard


def read_data(file_path):
    data = []
    for line in open(file_path, 'r', encoding='utf-8'):
        if line.endswith('\n'):
            data.append(line[:-1])
        else:
            data.append(line)
    # print('11111111111111111')
    # print(*data, sep='\n')
    # print('11111111111111111')
    return data


def start(data_file, min_time, max_time, first_time=10):
    """
    开始执行
    :param data_file: 数据文件
    :param min_time: 最小发送间隔时间（s）
    :param max_time: 最大发送间隔时间（s）
    :param first_time: 首次运行等待时间（s）
    """
    k = PyKeyboard()

    data_list = read_data(data_file)
    time.sleep(first_time)
    count = 1
    while True:
        data_str = random.choice(data_list)
        pyperclip.copy(data_str)
        time_num = random.randint(min_time, max_time)
        print(f'第{count}条({time_num}s)：{data_str}')
        k.press_key(k.control_key)
        k.tap_key('v')
        k.release_key(k.control_key)
        time.sleep(time_num)
        k.tap_key(k.enter_key)
        count += 1


if __name__ == '__main__':
    start('data/data.txt', 1, 10)
