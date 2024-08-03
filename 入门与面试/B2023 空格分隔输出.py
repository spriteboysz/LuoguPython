#! /usr/bin/env python
# coding=utf-8
"""
Author: Deean
Date: 2024-08-03 11:14
FileName: 入门与面试
Description:B2023 空格分隔输出.py 
"""


def func():
    a = input().strip()
    b = int(input().strip())
    c = float(input().strip())
    d = float(input().strip())
    print(f'{a} {b} {c:.6f} {d:.6f}')


if __name__ == '__main__':
    func()
