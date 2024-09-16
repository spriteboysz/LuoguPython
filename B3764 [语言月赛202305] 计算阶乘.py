#! /usr/bin/env python
# coding=utf-8
"""
Author: Deean
Date: 2024-09-16 14:58
FileName: 
Description:B3764 [语言月赛202305] 计算阶乘.py 
"""
from functools import lru_cache


def func():
    @lru_cache
    def process(n):
        if n == 1 or n == 0:
            return 1 * 2
        return (n - 1) * process(n - 2)

    t = int(input().strip())
    for _ in range(t):
        print(process(int(input().strip())))


if __name__ == '__main__':
    func()
