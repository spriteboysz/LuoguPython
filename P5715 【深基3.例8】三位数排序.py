#! /usr/bin/env python
# coding=utf-8
"""
Author: Deean
Date: 2024-08-10 17:32
FileName: 
Description:P5715 【深基3.例8】三位数排序.py 
"""


def func():
    nums = list(map(int, input().strip().split()))
    print(' '.join(map(str, sorted(nums))))


if __name__ == '__main__':
    func()
