#! /usr/bin/env python
# coding=utf-8
"""
Author: Deean
Date: 2024-08-08 23:27
FileName: 入门与面试
Description:B2620 【深基3.例1】数字比较.py 
"""


def func():
    a, b = map(int, input().strip().split())
    print(int(a > b), int(a <= b), int(a != b))


if __name__ == '__main__':
    func()
