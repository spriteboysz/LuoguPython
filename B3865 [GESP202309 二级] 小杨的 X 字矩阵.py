#! /usr/bin/env python
# coding=utf-8
"""
Author: Deean
Date: 2024-09-17 13:04
FileName: 
Description:B3865 [GESP202309 二级] 小杨的 X 字矩阵.py 
"""


def func():
    n = int(input().strip())
    for i in range(n // 2, -n // 2, -1):
        row = ['-'] * n
        row[n // 2 - abs(i)] = '+'
        row[n - (n // 2 - abs(i)) - 1] = '+'
        print(''.join(row))


if __name__ == '__main__':
    func()
