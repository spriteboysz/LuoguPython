#! /usr/bin/env python
# coding=utf-8
"""
Author: Deean
Date: 2024-11-03 20:41
FileName: P8225 「Wdoi-5」天才⑨与天才拆分
Description:
"""


def func():
    t = int(input().strip())
    grid = [map(int, input().strip().split()) for _ in range(t)]
    for k, n in grid:
        if n % int('9' * k) == 0:
            print('aya')
        else:
            print('baka')


if __name__ == '__main__':
    func()
