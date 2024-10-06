#! /usr/bin/env python
# coding=utf-8
"""
Author: Deean
Date: 2024-10-06 10:54
FileName: 
Description:P8823 [传智杯 #3 初赛] 期末考试成绩.py 
"""


def func():
    s = int(input().strip())
    if s >= 90:
        gpa = 4
    elif s >= 60:
        gpa = 4.0 - (90 - s) * 0.1
    else:
        gpa = (s ** 0.5) * 10 // 1
        if gpa >= 60:
            gpa = 4.0 - (90 - gpa) * 0.1
        else:
            gpa = 0
    print(f'{gpa:.1f}')


if __name__ == '__main__':
    func()
