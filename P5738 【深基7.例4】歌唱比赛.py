#! /usr/bin/env python
# coding=utf-8
"""
Author: Deean
Date: 2024-08-16 00:01
FileName: 
Description:P5738 【深基7.例4】歌唱比赛.py 
"""


def func():
    n, m = map(int, input().strip().split())
    data = [list(map(int, input().strip().split())) for _ in range(n)]
    scores = [(sum(nums) - max(nums) - min(nums)) / (m - 2) for nums in data]
    print(f'{max(scores):.2f}')


if __name__ == '__main__':
    func()
