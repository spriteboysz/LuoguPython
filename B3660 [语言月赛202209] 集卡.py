#! /usr/bin/env python
# coding=utf-8
"""
Author: Deean
Date: 2024-09-07 10:48
FileName: 
Description:B3660 [语言月赛202209] 集卡.py 
"""


def func():
    t = int(input().strip())
    for i in range(t):
        _ = input()
        nums = input().strip().split()
        print('yes' if '0' in nums else 'no')


if __name__ == '__main__':
    func()
