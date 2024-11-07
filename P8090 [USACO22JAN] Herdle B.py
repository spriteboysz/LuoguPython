#! /usr/bin/env python
# coding=utf-8
"""
Author: Deean
Date: 2024-11-06 22:41
FileName: P8090 [USACO22JAN] Herdle B
Description:
"""
from collections import Counter


def func():
    grid1 = [list(input().strip()) for _ in range(3)]
    grid2 = [list(input().strip()) for _ in range(3)]
    grid1, grid2 = sum(grid1, []), sum(grid2, [])
    cnt1, cnt2 = 0, 0
    for i in range(9):
        if grid1[i] == grid2[i]:
            cnt1 += 1
            grid1[i] = '*'
            grid2[i] = '*'
    print(cnt1)
    count1, count2 = Counter(grid1), Counter(grid2)
    for k in count1 & count2:
        cnt2 += min(count1[k], count2[k])
    print(cnt2 - cnt1)


if __name__ == '__main__':
    func()
