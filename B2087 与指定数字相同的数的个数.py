#! /usr/bin/env python
# coding=utf-8
"""
Author: Deean
Date: 2024-08-03 22:48
FileName: 入门与面试
Description:B2087 与指定数字相同的数的个数.py 
"""


def func():
    _ = int(input().strip())
    nums = list(map(int, input().strip().split()))
    m = int(input().strip())
    print(nums.count(m))


if __name__ == '__main__':
    func()
