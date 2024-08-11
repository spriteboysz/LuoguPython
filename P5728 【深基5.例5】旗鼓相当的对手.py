#! /usr/bin/env python
# coding=utf-8
"""
Author: Deean
Date: 2024-08-11 12:52
FileName: 
Description:P5728 【深基5.例5】旗鼓相当的对手.py 
"""


def func():
    n = int(input().strip())
    grid = [list(map(int, input().strip().split())) for _ in range(n)]
    cnt = 0
    for i, row1 in enumerate(grid):
        for j, row2 in enumerate(grid[i + 1:]):
            if max([abs(n1 - n2) for n1, n2 in zip(row1, row2)]) <= 5 and abs(sum(row1) - sum(row2)) <= 10:
                cnt += 1
    print(cnt)


if __name__ == '__main__':
    func()
