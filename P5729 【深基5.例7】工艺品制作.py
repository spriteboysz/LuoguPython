#! /usr/bin/env python
# coding=utf-8
"""
Author: Deean
Date: 2024-08-11 13:05
FileName: 
Description:P5729 【深基5.例7】工艺品制作.py 
"""


def func():
    w, x, h = map(int, input().strip().split())
    q = int(input().strip())
    cuts = [list(map(int, input().strip().split())) for _ in range(q)]
    cube = [[[1] * x for _ in range(w)] for _ in range(h)]
    for x1, y1, z1, x2, y2, z2 in cuts:
        for dz in range(z1, min(z2 + 1, h)):
            for dy in range(y1, min(y2 + 1, w)):
                for dx in range(x1, min(x2 + 1, x)):
                    cube[dz][dy][dx] = 0
    print(sum(sum(sum(cube, []), [])))


if __name__ == '__main__':
    func()
