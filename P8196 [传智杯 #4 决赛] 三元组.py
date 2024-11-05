#! /usr/bin/env python
# coding=utf-8
"""
Author: Deean
Date: 2024-11-05 23:26
FileName: P8196 [传智杯 #4 决赛] 三元组
Description:
"""


def func():
    t = int(input().strip())
    data = [list(map(int, input().strip().split())) for _ in range(2 * t)]
    for x in range(0, 2 * t, 2):
        n, nums = data[x][0], data[x + 1]
        print(sum([1 for i in range(n) for j in range(i, n) for k in range(j, n) if nums[i] + nums[j] == nums[k]]))


if __name__ == '__main__':
    func()
