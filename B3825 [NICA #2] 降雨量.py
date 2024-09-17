#! /usr/bin/env python
# coding=utf-8
"""
Author: Deean
Date: 2024-09-17 12:20
FileName: 
Description:B3825 [NICA #2] 降雨量.py 
"""


def func():
    x, h = map(int, input().strip().split())
    if x < 10:
        print('Drizzle')
    elif 10 <= x < 25:
        print('Moderate Rain')
    elif 25 <= x < 50:
        print('Heavy Rain')
    else:
        print('Torrential Rain')
    if h == 1:
        print('YES' if x >= 20 else 'NO')


if __name__ == '__main__':
    func()
