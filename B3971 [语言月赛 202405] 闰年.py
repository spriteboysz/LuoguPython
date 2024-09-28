#! /usr/bin/env python
# coding=utf-8
"""
Author: Deean
Date: 2024-09-28 09:16
FileName: 
Description:B3971 [语言月赛 202405] 闰年.py 
"""


def func():
    y = int(input().strip())
    if y % 172800 == 0:
        print('Yes')
    elif y % 3200 == 0:
        print('No')
    elif y % 400 == 0:
        print('Yes')
    elif y % 100 == 0:
        print('No')
    elif y % 4 == 0:
        print('Yes')
    else:
        print('No')


if __name__ == '__main__':
    func()
