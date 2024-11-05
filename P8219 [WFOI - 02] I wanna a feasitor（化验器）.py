#! /usr/bin/env python
# coding=utf-8
"""
Author: Deean
Date: 2024-11-05 23:21
FileName: P8219 [WFOI - 02] I wanna a feasitor（化验器）
Description:
"""


def func():
    left, right = map(int, input().strip().split())
    for num in range(right, left - 1, -1):
        if num % 2 == 0:
            print(num // 2)
            return


if __name__ == '__main__':
    func()
