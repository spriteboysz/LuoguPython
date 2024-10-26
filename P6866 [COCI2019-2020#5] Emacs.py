#! /usr/bin/env python
# coding=utf-8
"""
Author: Deean
Date: 2024-10-26 21:34
FileName: P6866 [COCI2019-2020#5] Emacs
Description:
"""


def func():
    n, m = map(int, input().strip().split())
    grid = [list(input().strip()) for _ in range(n)]
    cnt = 0
    for i in range(n):
        for j in range(m):
            if grid[i][j] != '*':
                continue
            if i == 0 and j == 0:
                cnt += 1
            elif i == 0 and grid[i][j - 1] == '.':
                cnt += 1
            elif j == 0 and grid[i - 1][j] == '.':
                cnt += 1
            elif grid[i][j - 1] == '.' and grid[i-1][j] == '.':
                cnt += 1
    print(cnt)


if __name__ == '__main__':
    func()
