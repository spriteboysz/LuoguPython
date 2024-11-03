#! /usr/bin/env python
# coding=utf-8
"""
Author: Deean
Date: 2024-11-03 09:27
FileName: P8401 [CCC2022 J2] Fergusonball Ratings
Description:
"""


def func():
    n = int(input().strip())
    nums = [int(input().strip()) for _ in range(2 * n)]
    score = []
    for i in range(0, n * 2, 2):
        a, b = nums[i], nums[i + 1]
        score.append(a * 5 - b * 3)
    count = sum([1 for s in score if s > 40])
    if count == n:
        print(f'{count}+')
    else:
        print(count)


if __name__ == '__main__':
    func()
