#! /usr/bin/env python
# coding=utf-8
"""
Author: Deean
Date: 2024-08-11 12:12
FileName: 
Description:P1089 [NOIP2004 提高组] 津津的储蓄计划.py 
"""


def func():
    nums = [int(input().strip()) for _ in range(12)]
    m, cur = 0, 0
    for i, num in enumerate(nums):
        cur += 300 - num
        if cur < 0:
            print(-(i + 1))
            return
        div, cur = divmod(cur, 100)
        m += div * 100
    print(int(m * 1.2 + cur))


if __name__ == '__main__':
    func()
