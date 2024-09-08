#! /usr/bin/env python
# coding=utf-8
"""
Author: Deean
Date: 2024-09-07 22:31
FileName: 
Description:B3698 [语言月赛202301] 一次函数.py 
"""


def func():
    data = {}

    def check(x, y):
        if (x, y) in data:
            return data[(x, y)]
        ret = (y == k * x + b)
        data[(x, y)] = ret
        return ret

    n, k, b = map(int, input().strip().split())
    points = [map(int, input().strip().split()) for _ in range(n)]
    cnt = 0
    for x, y in points:
        cnt += check(x, y)
    print(data)
    print(cnt)


if __name__ == '__main__':
    func()
