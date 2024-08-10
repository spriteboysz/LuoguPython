#! /usr/bin/env python
# coding=utf-8
"""
Author: Deean
Date: 2024-08-03 11:27
FileName: 入门与面试
Description:B2026 计算浮点数相除的余.py 
"""


def func():
    a, b = map(float, input().strip().split())
    print(f'{a % b:.4f}')


if __name__ == '__main__':
    func()
