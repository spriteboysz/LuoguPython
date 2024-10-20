#! /usr/bin/env python
# coding=utf-8
"""
Author: Deean
Date: 2024-08-03 09:52
FileName: 入门与面试
Description:B3736 [信息与未来 2018] 最大公约数
"""
import math


def func():
    x, y, z = map(int, input().strip().split())
    print(math.gcd(x, y, z))


if __name__ == '__main__':
    func()
