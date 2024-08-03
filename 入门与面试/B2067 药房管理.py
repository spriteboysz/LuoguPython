#! /usr/bin/env python
# coding=utf-8
"""
Author: Deean
Date: 2024-08-03 18:07
FileName: 入门与面试
Description:B2067 药房管理.py 
"""


def func():
    m = int(input().strip())
    _ = int(input().strip())
    nums = list(map(int, input().strip().split()))
    cnt = 0
    for num in nums:
        if num > m:
            cnt += 1
        else:
            m -= num
    print(cnt)


if __name__ == '__main__':
    func()
