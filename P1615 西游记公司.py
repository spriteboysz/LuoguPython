#! /usr/bin/env python
# coding=utf-8
"""
Author: Deean
Date: 2024-08-17 21:32
FileName: 
Description:P1615 西游记公司.py 
"""


def func():
    start = list(map(int, input().strip().split(':')))
    end = list(map(int, input().strip().split(':')))
    n = int(input().strip())
    t = (end[0] - start[0]) * 3600 + (end[1] - start[1]) * 60 + end[2] - start[2]
    print(n * t)


if __name__ == '__main__':
    func()
