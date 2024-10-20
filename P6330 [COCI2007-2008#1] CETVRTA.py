#! /usr/bin/env python
# coding=utf-8
"""
Author: Deean
Date: 2024-10-19 18:16
FileName: 
Description:P6330 [COCI2007-2008#1] CETVRTA.py 
"""
from collections import Counter


def func():
    grid = [list(map(int, (input().strip().split()))) for _ in range(3)]
    lst1, lst2 = [], []
    for x, y in grid:
        lst1.append(x)
        lst2.append(y)
    for k, v in Counter(lst1).items():
        if v == 1:
            print(k, end=' ')
            break
    for k, v in Counter(lst2).items():
        if v == 1:
            print(k)
            return


if __name__ == '__main__':
    func()
