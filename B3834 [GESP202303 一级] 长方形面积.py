#! /usr/bin/env python
# coding=utf-8
"""
Author: Deean
Date: 2024-09-16 10:38
FileName: 
Description:B3834 [GESP202303 一级] 长方形面积.py 
"""


def func():
    area = int(input().strip())
    cnt = 0
    for a in range(1, 1001):
        for b in range(a, 1001):
            if a * b == area:
                cnt += 1
    print(cnt)


if __name__ == '__main__':
    func()
