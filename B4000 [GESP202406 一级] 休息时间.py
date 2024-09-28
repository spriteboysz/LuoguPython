#! /usr/bin/env python
# coding=utf-8
"""
Author: Deean
Date: 2024-09-28 15:22
FileName: 
Description:B4000 [GESP202406 一级] 休息时间.py 
"""


def func():
    hh, mm, ss, k = [int(input().strip()) for _ in range(4)]
    seconds = ss + mm * 60 + hh * 3600 + k
    print(seconds // 3600, (seconds % 3600) // 60, seconds % 60)


if __name__ == '__main__':
    func()
