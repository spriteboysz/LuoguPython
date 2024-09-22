#! /usr/bin/env python
# coding=utf-8
"""
Author: Deean
Date: 2024-09-22 16:06
FileName: 
Description:B3895 [NICA #3] CPU.py 
"""


def func():
    c, t = map(int, input().strip().split())
    for x in range(1, c + 1):
        for y in range(c):
            if x + y == c and 2 * x + y == t:
                print(x, y)
                return
    print('Error')


if __name__ == '__main__':
    func()
