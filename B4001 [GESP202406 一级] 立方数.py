#! /usr/bin/env python
# coding=utf-8
"""
Author: Deean
Date: 2024-09-28 15:25
FileName: 
Description:B4001 [GESP202406 一级] 立方数.py 
"""


def func():
    n = int(input().strip())
    nums = [i ** 3 for i in range(11)]
    if n in nums:
        print('Yes')
    else:
        print('No')


if __name__ == '__main__':
    func()
