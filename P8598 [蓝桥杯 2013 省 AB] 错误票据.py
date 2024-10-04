#! /usr/bin/env python
# coding=utf-8
"""
Author: Deean
Date: 2024-10-04 10:48
FileName: 
Description:P8598 [蓝桥杯 2013 省 AB] 错误票据.py 
"""


def func():
    n = int(input())
    nums = []
    for _ in range(n):
        nums.extend(list(map(int, input().strip().split())))
    nums.sort()
    m, n = -1, -1
    for i in range(1, len(nums)):
        if nums[i] == nums[i - 1]:
            n = nums[i]
        elif nums[i] - nums[i - 1] == 2:
            m = nums[i] - 1
        if m != -1 and n != -1:
            break
    print(m, n)


if __name__ == '__main__':
    func()
