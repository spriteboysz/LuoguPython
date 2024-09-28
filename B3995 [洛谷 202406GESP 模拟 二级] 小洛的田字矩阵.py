#! /usr/bin/env python
# coding=utf-8
"""
Author: Deean
Date: 2024-09-28 14:58
FileName: 
Description:B3995 [洛谷 202406GESP 模拟 二级] 小洛的田字矩阵.py 
"""


def func():
    n = int(input().strip())
    for i in range(n):
        if i == 0 or i == n - 1:
            print('|' + '-' * (n - 2) + '|')
        elif i == n // 2:
            print('|' + '-' * ((n - 2) // 2) + 'x' + '-' * ((n - 2) // 2) + '|')
        else:
            print('|' + 'x' * ((n - 2) // 2) + '|' + 'x' * ((n - 2) // 2) + '|')


if __name__ == '__main__':
    func()
