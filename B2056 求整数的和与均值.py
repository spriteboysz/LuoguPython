#! /usr/bin/env python
# coding=utf-8
"""
Author: Deean
Date: 2024-08-03 17:04
FileName: 入门与面试
Description:B2056 求整数的和与均值.py 
"""


def func():
    n = int(input().strip())
    nums = []
    for _ in range(n):
        nums.append(int(input().strip()))
    total = sum(nums)
    print(f'{total} {total / n:.5f}')


if __name__ == '__main__':
    func()
