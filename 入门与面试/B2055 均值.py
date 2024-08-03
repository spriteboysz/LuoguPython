#! /usr/bin/env python
# coding=utf-8
"""
Author: Deean
Date: 2024-08-03 17:02
FileName: 入门与面试
Description:B2055 均值.py 
"""


def func():
    n = int(input().strip())
    nums = list(map(float, input().strip().split()))
    print(f'{sum(nums) / n:.4f}')


if __name__ == '__main__':
    func()
