#! /usr/bin/env python
# coding=utf-8
"""
Author: Deean
Date: 2024-08-11 12:42
FileName: 
Description:P1047 [NOIP2005 普及组] 校门外的树.py 
"""


def func():
    n, m = map(int, input().strip().split())
    points = [list(map(int, input().strip().split())) for _ in range(m)]
    trees = [1] * (n + 1)
    for u, v in points:
        trees[u:v + 1] = [0] * (v + 1 - u)
    print(sum(trees))


if __name__ == '__main__':
    func()
