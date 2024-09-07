#! /usr/bin/env python
# coding=utf-8
"""
Author: Deean
Date: 2024-09-07 11:00
FileName: 
Description:B3653 [语言月赛202208] 俊俏地鼠的远亲.py 
"""


def func():
    data = {}

    def process(x1, y1, x2, y2):
        if (x1, y1, x2, y2) in data:
            return data.get((x1, y1, x2, y2))
        if (x2, y2, x1, y1) in data:
            return data.get((x2, y2, x1, y1))
        ret = (x1 - x2) ** 2 + (y1 - y2) ** 2
        data[(x1, y1, x2, y2)] = ret
        return ret

    n, m = map(int, input().strip().split())
    grid = [list(map(int, input().strip().split())) for _ in range(n)]
    dis = [[0] * m for _ in range(n)]
    for i, row1 in enumerate(grid):
        for j, num1 in enumerate(row1):
            for x, row2 in enumerate(grid):
                for y, num2 in enumerate(row2):
                    if num1 == num2:
                        dis[i][j] = max(dis[i][j], process(i, j, x, y))
    print('\n'.join([' '.join(map(str, row)) for row in dis]))


if __name__ == '__main__':
    func()
