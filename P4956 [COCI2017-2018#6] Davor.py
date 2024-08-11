#! /usr/bin/env python
# coding=utf-8
"""
Author: Deean
Date: 2024-08-11 12:19
FileName: 
Description:P4956 [COCI2017-2018#6] Davor.py 
"""


def func():
    num = int(input().strip())
    for k in range(1, 101):
        for x in range(1, 101):
            if (7 * x + 21 * k) * 52 == num:
                print(x)
                print(k)
                return
    raise ValueError('Error')


if __name__ == '__main__':
    func()
