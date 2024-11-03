#! /usr/bin/env python
# coding=utf-8
"""
Author: Deean
Date: 2024-11-02 15:13
FileName: P8534 「Wdoi-2」比赤色更红的梦
Description:
"""


def func():
    t = int(input().strip())
    grid = [input().strip() for _ in range(t)]
    for row in grid:
        x, s = map(int, row.split())
        cnt = 2
        if x >= 5:
            cnt += 2
        elif x >= 3:
            cnt += 1
        if s >= 6000 * (10 ** 4):
            cnt += 4
        elif s >= 4000 * (10 ** 4):
            cnt += 3
        elif s >= 2000 * (10 ** 4):
            cnt += 2
        elif s >= 1000 * (10 ** 4):
            cnt += 1
        print(cnt)


if __name__ == '__main__':
    func()
