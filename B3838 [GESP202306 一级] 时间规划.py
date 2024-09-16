#! /usr/bin/env python
# coding=utf-8
"""
Author: Deean
Date: 2024-09-16 10:49
FileName: 
Description:B3838 [GESP202306 一级] 时间规划.py 
"""


def func():
    data = [int(input().strip()) for _ in range(4)]
    print((data[2] - data[0]) * 60 + data[3] - data[1])


if __name__ == '__main__':
    func()
