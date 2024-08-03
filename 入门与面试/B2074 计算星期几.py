#! /usr/bin/env python
# coding=utf-8
"""
Author: Deean
Date: 2024-08-03 18:39
FileName: 入门与面试
Description:B2074 计算星期几.py 
"""


def func():
    a, b = map(int, input().strip().split())
    weekdays = ['Sunday', 'Monday', 'Tuesday', 'Wednesday', 'Thursday', 'Friday', 'Saturday']
    print(weekdays[(a ** b) % 7])


if __name__ == '__main__':
    func()
