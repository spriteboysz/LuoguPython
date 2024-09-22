#! /usr/bin/env python
# coding=utf-8
"""
Author: Deean
Date: 2024-09-17 18:48
FileName: 
Description:B3887 [语言月赛 202311] 风球.py 
"""


def func():
    nums = list(map(int, input().strip().split()))
    g10, g08, g03 = 0, 0, 0
    for num in nums:
        if num >= 118:
            g10 += 1
        if num >= 63:
            g08 += 1
        if num >= 41:
            g03 += 1
    if g10 > 0:
        print('10')
    elif g08 >= 4:
        print('8')
    elif g03 >= 4:
        print('3')
    else:
        print('1')


if __name__ == '__main__':
    func()
