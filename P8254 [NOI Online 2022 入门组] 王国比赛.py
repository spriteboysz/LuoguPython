#! /usr/bin/env python
# coding=utf-8
"""
Author: Deean
Date: 2024-11-03 17:58
FileName: P8254 [NOI Online 2022 入门组] 王国比赛
Description:
"""


def func():
    n, m = map(int, input().strip().split())
    grid = [list(map(int, input().strip().split())) for _ in range(m)]
    nums1 = map(int, input().strip().split())
    nums2 = [int(sum(row) > m // 2) for row in zip(*grid)]
    cnt = 0
    for num1, num2 in zip(nums1, nums2):
        if num1 == num2:
            cnt += 1
    print(cnt)


if __name__ == '__main__':
    func()
