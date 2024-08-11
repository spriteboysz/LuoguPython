#! /usr/bin/env python
# coding=utf-8
"""
Author: Deean
Date: 2024-08-11 13:50
FileName: 
Description:P2550 [AHOI2001] 彩票摇奖.py 
"""


def func():
    n = int(input().strip())
    seen = set(map(int, input().strip().split()))
    grid = [set(map(int, input().strip().split())) for _ in range(n)]
    nums = [0] * 8
    for row in grid:
        nums[len(row & seen)] += 1
    print(' '.join(map(str, nums[1:][::-1])))


if __name__ == '__main__':
    func()
