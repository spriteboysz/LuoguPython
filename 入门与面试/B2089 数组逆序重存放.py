#! /usr/bin/env python
# coding=utf-8
"""
Author: Deean
Date: 2024-08-03 22:54
FileName: 入门与面试
Description:B2089 数组逆序重存放.py 
"""


def func():
    _ = int(input().strip())
    nums = input().strip().split()
    print(' '.join(nums[::-1]))


if __name__ == '__main__':
    func()
