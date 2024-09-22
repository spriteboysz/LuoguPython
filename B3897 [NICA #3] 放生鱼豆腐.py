#! /usr/bin/env python
# coding=utf-8
"""
Author: Deean
Date: 2024-09-22 19:10
FileName: 
Description:B3897 [NICA #3] 放生鱼豆腐.py 
"""


def func():
    k, a, b, c = map(int, input().strip().split())
    nums = list(map(int, input().strip().split()))
    s = 0
    for num in nums:
        if num > 100:
            s += (num - 100) * c + 90 * b + 10 * a
        elif num > 10:
            s += (num - 10) * b + 10 * a
        else:
            s += num * a
    print(s)


if __name__ == '__main__':
    func()
