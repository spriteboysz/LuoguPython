#! /usr/bin/env python
# coding=utf-8
"""
Author: Deean
Date: 2024-08-18 16:17
FileName: 
Description:P2689 东南西北.py 
"""

from _collections import defaultdict


def func():
    point1 = list(map(int, input().strip().split()))
    point2 = list(map(int, input().strip().split()))
    n = int(input().strip())
    directions = [input().strip() for _ in range(n)]
    count = defaultdict(int)
    for direction in directions:
        count[direction] += 1
    dx, dy = point2[0] - point1[0], point2[1] - point1[1]
    if dx > 0:
        flag1 = count['E'] >= dx
    elif dx < 0:
        flag1 = count['W'] >= dx
    else:
        flag1 = True
    if dy > 0:
        flag2 = count['N'] >= dy
    elif dy < 0:
        flag2 = count['S'] >= dy
    else:
        flag2 = True
    if flag1 and flag2:
        print(abs(dx) + abs(dy))
    else:
        print(-1)


if __name__ == '__main__':
    func()
