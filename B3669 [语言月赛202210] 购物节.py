#! /usr/bin/env python
# coding=utf-8
"""
Author: Deean
Date: 2024-10-21 23:02
FileName: B3669 [语言月赛202210] 购物节
Description:
"""


def func():
    x, y, n = map(int, input().strip().split())
    if x - 1 <= (y - 1) / 10:
        print(n * (x - 1))
    else:
        div, mod = divmod(n, 10)
        print((y - 1) * div + (x - 1) * mod)


if __name__ == '__main__':
    func()
