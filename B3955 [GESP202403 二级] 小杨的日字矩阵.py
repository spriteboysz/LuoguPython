#! /usr/bin/env python
# coding=utf-8
"""
Author: Deean
Date: 2024-09-22 20:42
FileName: 
Description:B3955 [GESP202403 二级] 小杨的日字矩阵.py 
"""


def func():
    n = int(input().strip())
    for i in range(n):
        if i == 0 or i == n - 1 or i == n // 2:
            ch = '-'
        else:
            ch = 'x'
        print('|' + ch * (n - 2) + '|')


if __name__ == '__main__':
    func()
