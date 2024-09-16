#! /usr/bin/env python
# coding=utf-8
"""
Author: Deean
Date: 2024-09-16 11:34
FileName: 
Description:B3846 [GESP样题 一级] 闰年求和.py 
"""


def func():
    def check(year):
        if year % 100 == 0:
            return year % 400 == 0
        return year % 4 == 0

    start, end = map(int, input().strip().split())
    print(sum([yy for yy in range(start + 1, end) if check(yy)]))

if __name__ == '__main__':
    func()
