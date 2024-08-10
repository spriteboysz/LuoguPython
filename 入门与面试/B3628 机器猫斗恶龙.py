#! /usr/bin/env python
# coding=utf-8
"""
Author: Deean
Date: 2024-08-10 10:35
FileName: 入门与面试
Description:B3628 机器猫斗恶龙.py 
"""


def func():
    _ = int(input().strip())
    nums = list(map(int, input().strip().split()))
    minimum, curr = 0, 0
    for num in nums:
        curr += num
        minimum = min(minimum, curr)
    print(abs(minimum) + 1)


if __name__ == '__main__':
    func()
