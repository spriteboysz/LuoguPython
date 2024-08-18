#! /usr/bin/env python
# coding=utf-8
"""
Author: Deean
Date: 2024-08-18 11:18
FileName: 
Description:P2006 赵神牛的游戏.py 
"""


def func():
    k, m, n = map(int, input().strip().split())
    data = [list(map(int, input().strip().split())) for _ in range(m)]
    flag = False
    for i, row in enumerate(data, start=1):
        a, b = row
        if a == 0:
            if b != 0:
                flag = True
                print(i, end=' ')
        elif k // a * b >= n:
            flag = True
            print(i, end=' ')
    if not flag:
        print(-1)
    else:
        print()


if __name__ == '__main__':
    func()
