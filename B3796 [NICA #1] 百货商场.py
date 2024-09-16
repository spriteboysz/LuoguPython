#! /usr/bin/env python
# coding=utf-8
"""
Author: Deean
Date: 2024-09-16 20:06
FileName: 
Description:B3796 [NICA #1] 百货商场.py 
"""


def func():
    n, m = map(int, input().strip().split())
    nums = list(map(int, input().strip().split()))
    count = 0
    for num in nums:
        if num <= m:
            count += num
            m -= num
    print(count - int(count * 0.88))


if __name__ == '__main__':
    func()
