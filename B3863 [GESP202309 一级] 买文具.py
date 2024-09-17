#! /usr/bin/env python
# coding=utf-8
"""
Author: Deean
Date: 2024-09-17 12:31
FileName: 
Description:B3863 [GESP202309 一级] 买文具.py 
"""


def func():
    x, y, z, q = [int(input().strip()) for _ in range(4)]
    total = x * 2 + 5 * y + 3 * z
    if q >= total:
        print('Yes')
        print(q - total)
    else:
        print('No')
        print(total - q)


if __name__ == '__main__':
    func()
