#! /usr/bin/env python
# coding=utf-8
"""
Author: Deean
Date: 2024-09-17 16:55
FileName: 
Description:B3875 [信息与未来 2015] 夏令营小旗手.py 
"""
from collections import defaultdict


def func():
    n, x = map(int, input().strip().split())
    count = defaultdict(int)
    count[x] += 1
    for _ in range(n - 1):
        xi = (x * 37 + 33031) % n + 1
        count[xi] += 1
        x = xi

    maximum = max(count.values())
    for i in range(1, n + 1):
        if count[i] == maximum:
            print(i)
            return
    raise ValueError('Error')


if __name__ == '__main__':
    func()
