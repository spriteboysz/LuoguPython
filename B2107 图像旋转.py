#! /usr/bin/env python
# coding=utf-8
"""
Author: Deean
Date: 2024-08-04 19:20
FileName: 入门与面试
Description:B2107 图像旋转.py 
"""


def func():
    n, m = map(int, input().strip().split())
    grid = [list(map(int, input().strip().split())) for _ in range(n)]
    for row in zip(*grid):
        print(' '.join(map(str, row[::-1])))


if __name__ == '__main__':
    func()
