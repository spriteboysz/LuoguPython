#! /usr/bin/env python
# coding=utf-8
"""
Author: Deean
Date: 2024-08-10 18:13
FileName: 
Description:P1424 小鱼的航程（改进版）.py 
"""


def func():
    x, n = map(int, input().strip().split())
    div, mod = divmod(n, 7)
    div *= 5
    if mod > 0:
        if mod + x == 7 or x == 7:
            mod -= 1
        elif mod + x >= 8:
            mod -= 2
    print((div + mod) * 250)


if __name__ == '__main__':
    func()
