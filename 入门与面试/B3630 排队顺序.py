#! /usr/bin/env python
# coding=utf-8
"""
Author: Deean
Date: 2024-08-10 10:03
FileName: 入门与面试
Description:B3630 排队顺序.py 
"""


def func():
    _ = int(input().strip())
    nums = list(map(int, input().strip().split()))
    a = int(input().strip())
    cur = a
    while cur != 0:
        print(cur, end=' ')
        cur = nums[cur - 1]
    print()


if __name__ == '__main__':
    func()
