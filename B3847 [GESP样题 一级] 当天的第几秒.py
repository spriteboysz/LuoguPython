#! /usr/bin/env python
# coding=utf-8
"""
Author: Deean
Date: 2024-09-16 11:38
FileName: 
Description:B3847 [GESP样题 一级] 当天的第几秒.py 
"""


def func():
    hh, mm, ss, flag = input().strip().split()
    if flag == 'P':
        hh = int(hh) + 12
    print(int(hh) * 3600 + int(mm) * 60 + int(ss))


if __name__ == '__main__':
    func()
