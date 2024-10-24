#! /usr/bin/env python
# coding=utf-8
"""
Author: Deean
Date: 2024-10-23 21:56
FileName: B4045 [语言月赛 202410] 同桌
Description:
"""

def func():
    n = int(input().strip())
    nums = list(map(int, input().strip().split()))
    seen = set()
    for i, num in enumerate(nums):
        seen.add('#'.join(map(str, sorted([i + 1, num]))))
    if len(seen) == n:
        print('Yes')
    else:
        print('No')


if __name__ == '__main__':
    func()
