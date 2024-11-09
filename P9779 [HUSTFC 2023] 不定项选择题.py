#! /usr/bin/env python
# coding=utf-8
"""
Author: Deean
Date: 2024-11-09 22:41
FileName: P9779 [HUSTFC 2023] 不定项选择题
Description:
"""
from functools import lru_cache


def func():
    @lru_cache()
    def process(num):
        if num == 1 or num == 0:
            return 1
        else:
            return num * process(num - 1)

    n = int(input().strip())
    cnt = 0
    for i in range(1, n + 1):
        cnt += process(n) // (process(i) * process(n - i))
    print(cnt)


if __name__ == '__main__':
    func()
