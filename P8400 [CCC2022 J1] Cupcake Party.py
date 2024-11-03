#! /usr/bin/env python
# coding=utf-8
"""
Author: Deean
Date: 2024-11-03 09:34
FileName: P8400 [CCC2022 J1] Cupcake Party
Description:
"""


def func():
    n = int(input().strip())
    m = int(input().strip())
    # n, m = map(int, input().strip().split())
    print(max(0, 8 * n + 3 * m - 28))


if __name__ == '__main__':
    func()
