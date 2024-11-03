#! /usr/bin/env python
# coding=utf-8
"""
Author: Deean
Date: 2024-11-03 09:16
FileName: P8410 「SvR-1」Don't Mozheng
Description:
"""


def func():
    n, a, b = map(int, input().strip().split())
    data = [input().strip() for _ in range(2 * n)]
    print(data.count('/oh') * a + data.count('/hsh') * b)


if __name__ == '__main__':
    func()
