#! /usr/bin/env python
# coding=utf-8
"""
Author: Deean
Date: 2024-08-03 10:36
FileName: 入门与面试
Description:B2013 温度表达转化.py 
"""


def func():
    f = float(input().strip())
    print(f'{5 * (f - 32) / 9:.5f}')


if __name__ == '__main__':
    func()
