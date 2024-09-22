#! /usr/bin/env python
# coding=utf-8
"""
Author: Deean
Date: 2024-09-22 19:22
FileName: 
Description:B3898 [NICA #3] 彩灯装饰.py 
"""


def func():
    n = int(input().strip())
    lst = [i * i for i in range(1, 101)]
    for i in range(1, n + 1):
        row = list('#' * ((2 * i) - 1))
        for j in range(len(row)):
            if j+1 in lst:
                row[j] = '!'
        print(' ' * (n - i) + ''.join(row))


if __name__ == '__main__':
    func()
