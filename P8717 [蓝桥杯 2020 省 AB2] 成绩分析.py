#! /usr/bin/env python
# coding=utf-8
"""
Author: Deean
Date: 2024-10-04 11:08
FileName: 
Description:P8717 [蓝桥杯 2020 省 AB2] 成绩分析.py 
"""


def func():
    n = int(input().strip())
    nums = [int(input().strip()) for _ in range(n)]
    print(max(nums))
    print(min(nums))
    print(f'{sum(nums) / len(nums):.2f}')


if __name__ == '__main__':
    func()
