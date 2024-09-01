#! /usr/bin/env python
# coding=utf-8
"""
Author: Deean
Date: 2024-09-01 09:40
FileName: 
Description:B3924 [GESP202312 二级] 小杨的H字矩阵.py 
"""


def func():
    n = int(input().strip())
    ss = ['|' + 'a' * (n - 2) + '|' for _ in range(n)]
    ss[n // 2] = '|' + '-' * (n - 2) + '|'
    print('\n'.join(ss))

if __name__ == '__main__':
    func()
