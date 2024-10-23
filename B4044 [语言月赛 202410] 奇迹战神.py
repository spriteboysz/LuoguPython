#! /usr/bin/env python
# coding=utf-8
"""
Author: Deean
Date: 2024-10-23 21:40
FileName: B4044 [语言月赛 202410] 奇迹战神
Description:
"""


def func():
    n = int(input().strip())
    grid = [list(map(int, input().strip().split())) for _ in range(n)]
    seen = set()
    for w, d in grid:
        for i in range(15):
            seen.add(w + 7 * d * i)
    nums = [num for num in seen if num >= 6]
    print(min(nums) - 6)


if __name__ == '__main__':
    func()
