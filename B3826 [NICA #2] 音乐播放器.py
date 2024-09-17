#! /usr/bin/env python
# coding=utf-8
"""
Author: Deean
Date: 2024-09-17 12:25
FileName: 
Description:B3826 [NICA #2] 音乐播放器.py 
"""


def func():
    n = int(input().strip())
    data = [list(map(int, input().strip().split())) for _ in range(n)]
    total = 0
    for a, b in data:
        if b == 1:
            total += a
        else:
            total += 10
    print(total)


if __name__ == '__main__':
    func()
