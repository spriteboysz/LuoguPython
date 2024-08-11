#! /usr/bin/env python
# coding=utf-8
"""
Author: Deean
Date: 2024-08-11 14:15
FileName: 
Description:P5730 【深基5.例10】显示屏.py 
"""


def func():
    _ = input()
    digits = ['XXX...X.XXX.XXX.X.X.XXX.XXX.XXX.XXX.XXX.',
              'X.X...X...X...X.X.X.X...X.....X.X.X.X.X.',
              'X.X...X.XXX.XXX.XXX.XXX.XXX...X.XXX.XXX.',
              'X.X...X.X.....X...X...X.X.X...X.X.X...X.',
              'XXX...X.XXX.XXX...X.XXX.XXX...X.XXX.XXX.']
    idx = [(4 * x, 4 * x + 4) for x in range(10)]
    s = input().strip()
    display = ['' for _ in range(5)]
    for ch in s:
        for i in range(5):
            a, b = idx[int(ch)]
            display[i] += digits[i][a:b]
    print('\n'.join(map(lambda row: row[:-1], display)))


if __name__ == '__main__':
    func()
