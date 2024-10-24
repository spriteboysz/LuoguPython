#! /usr/bin/env python
# coding=utf-8
"""
Author: Deean
Date: 2024-10-23 22:27
FileName: P6581 远大目标
Description:
"""


def func():
    num = int(input().strip())
    if num <= 0:
        print(0)
    else:
        print(num * 2 - 1)


if __name__ == '__main__':
    func()
