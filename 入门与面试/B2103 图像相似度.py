#! /usr/bin/env python
# coding=utf-8
"""
Author: Deean
Date: 2024-08-04 19:00
FileName: 入门与面试
Description:B2103 图像相似度.py 
"""


def func():
    m, n = map(int, input().strip().split())
    grid1 = [list(map(int, input().strip().split())) for _ in range(m)]
    grid2 = [list(map(int, input().strip().split())) for _ in range(m)]
    cnt = 0
    for i in range(m):
        for j in range(n):
            if grid1[i][j] == grid2[i][j]:
                cnt += 1
    print(f'{cnt * 100 / (m * n):.2f}')


if __name__ == '__main__':
    func()
