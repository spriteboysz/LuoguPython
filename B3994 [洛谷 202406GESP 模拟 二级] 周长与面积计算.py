#! /usr/bin/env python
# coding=utf-8
"""
Author: Deean
Date: 2024-09-28 14:55
FileName: 
Description:B3994 [洛谷 202406GESP 模拟 二级] 周长与面积计算.py 
"""


def func():
    n = int(input().strip())
    a, s = 0, 0
    for i in range(1, n + 1):
        a += i
        s += i * i
    print(a * 2 + n * 2)
    print(s)


if __name__ == '__main__':
    func()
