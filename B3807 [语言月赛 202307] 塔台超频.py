#! /usr/bin/env python
# coding=utf-8
"""
Author: Deean
Date: 2024-09-16 20:41
FileName: 
Description:B3807 [语言月赛 202307] 塔台超频.py 
"""
import sys

def func():
    n = int(input().strip())
    lines = [sys.stdin.readline() for _ in range(n)]
    data = [list(map(int, line.strip().split())) for line in lines]
    minimum = max(0, *[data[i][0] - sum(data[i - 1]) for i in range(1, n)])
    print(minimum)


if __name__ == '__main__':
    func()
