#! /usr/bin/env python
# coding=utf-8
"""
Author: Deean
Date: 2024-09-28 12:30
FileName: 
Description:B3993 [洛谷 202406GESP 模拟 一级] 明日复明日.py 
"""


def func():
    mm, dd = map(int, input().strip().split())
    months = [0, 31, 28, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]
    if mm == 12 and dd == 31:
        print('1 1')
    elif dd == months[mm]:
        print(f'{mm + 1} 1')
    else:
        print(f'{mm} {dd + 1}')


if __name__ == '__main__':
    func()
