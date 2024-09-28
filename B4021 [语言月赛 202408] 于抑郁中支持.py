#! /usr/bin/env python
# coding=utf-8
"""
Author: Deean
Date: 2024-09-28 16:33
FileName: 
Description:B4021 [语言月赛 202408] 于抑郁中支持.py 
"""


def func():
    n, t = map(int, input().strip().split())
    nums = list(map(int, input().strip().split()))
    seen = set()
    for num in nums:
        seen.add(num % (10 ** t))
    print(len(seen))


if __name__ == '__main__':
    func()
