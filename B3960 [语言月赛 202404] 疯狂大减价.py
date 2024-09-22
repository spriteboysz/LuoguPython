#! /usr/bin/env python
# coding=utf-8
"""
Author: Deean
Date: 2024-09-22 21:22
FileName: 
Description:B3960 [语言月赛 202404] 疯狂大减价.py 
"""


def func():
    num = int(input())
    if num <= 99:
        print(num)
    elif num <= 199:
        print(num - 20)
    else:
        print(num - 70)


if __name__ == '__main__':
    func()
