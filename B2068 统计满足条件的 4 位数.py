#! /usr/bin/env python
# coding=utf-8
"""
Author: Deean
Date: 2024-08-03 18:11
FileName: 入门与面试
Description:B2068 统计满足条件的 4 位数.py 
"""


def func():
    _ = int(input().strip())
    nums = input().strip().split()
    cnt = 0
    for num in nums:
        a, b, c, d = map(int, list(num))
        if d > a + b + c:
            cnt += 1
    print(cnt)


if __name__ == '__main__':
    func()
