#! /usr/bin/env python
# coding=utf-8
"""
Author: Deean
Date: 2024-10-04 11:18
FileName: 
Description:P8753 [蓝桥杯 2021 省 AB2] 小平方.py 
"""


def func():
    n = int(input().strip())
    cnt, m = 0, n / 2
    for i in range(1, n):
        if (i * i) % n < m:
            cnt += 1
    print(cnt)


if __name__ == '__main__':
    func()
