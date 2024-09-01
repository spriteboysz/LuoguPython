#! /usr/bin/env python
# coding=utf-8
"""
Author: Deean
Date: 2024-09-01 09:37
FileName: 
Description:B3922 [GESP202312 一级] 小杨报数.py 
"""


def func():
    n = int(input().strip())
    m = int(input().strip())
    print('\n'.join(map(str, ([i for i in range(1, n + 1) if i % m != 0]))))


if __name__ == '__main__':
    func()
