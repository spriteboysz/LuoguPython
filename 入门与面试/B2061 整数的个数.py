#! /usr/bin/env python
# coding=utf-8
"""
Author: Deean
Date: 2024-08-03 17:20
FileName: 入门与面试
Description:B2061 整数的个数.py 
"""


def func():
    _ = int(input().strip())
    nums = list(map(int, input().strip().split()))
    print('\n'.join(map(str, [nums.count(1), nums.count(5), nums.count(10)])))


if __name__ == '__main__':
    func()
