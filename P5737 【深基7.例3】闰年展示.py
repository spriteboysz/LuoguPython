#! /usr/bin/env python
# coding=utf-8
"""
Author: Deean
Date: 2024-08-15 23:58
FileName: 
Description:P5737 【深基7.例3】闰年展示.py 
"""


def func():
    def check(year):
        if year % 100 == 0:
            return year % 400 == 0
        else:
            return year % 4 == 0

    a, b = map(int, input().strip().split())
    years = [year for year in range(a, b + 1) if check(year)]
    print(len(years))
    print(' '.join(map(str, years)))


if __name__ == '__main__':
    func()
