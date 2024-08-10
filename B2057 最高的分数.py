#! /usr/bin/env python
# coding=utf-8
"""
Author: Deean
Date: 2024-08-03 17:08
FileName: 入门与面试
Description:B2057 最高的分数.py 
"""


def func():
    _ = int(input().strip())
    nums = list(map(int, input().strip().split()))
    print(max(nums))


if __name__ == '__main__':
    func()
