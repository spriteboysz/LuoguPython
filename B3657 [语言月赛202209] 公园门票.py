#! /usr/bin/env python
# coding=utf-8
"""
Author: Deean
Date: 2024-09-07 10:57
FileName: 
Description:B3657 [语言月赛202209] 公园门票.py 
"""


def func():
    x, y = map(int, input().strip().split())
    z = min(x, y)
    print(z * 90 + (x - z) * 60 + (y - z) * 40)


if __name__ == '__main__':
    func()
