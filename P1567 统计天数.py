#! /usr/bin/env python
# coding=utf-8
"""
Author: Deean
Date: 2024-08-17 21:26
FileName: 
Description:P1567 统计天数.py 
"""


def func():
    n = int(input().strip())
    nums = list(map(int, input().strip().split()))
    maximum, cur = 1, 1
    for i in range(1, n):
        if nums[i] > nums[i - 1]:
            cur += 1
        else:
            cur = 1
        maximum = max(maximum, cur)
    print(maximum)


if __name__ == '__main__':
    func()
