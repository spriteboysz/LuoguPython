#! /usr/bin/env python
# coding=utf-8
"""
Author: Deean
Date: 2024-10-04 11:10
FileName: 
Description:P8722 [蓝桥杯 2020 省 AB3] 日期识别.py 
"""


def func():
    date = input().strip()
    months = ['Jan', 'Feb', 'Mar', 'Apr', 'May', 'Jun', 'Jul', 'Aug', 'Sep', 'Oct', 'Nov', 'Dec']
    print(months.index(date[:3]) + 1, int(date[3:]))


if __name__ == '__main__':
    func()
